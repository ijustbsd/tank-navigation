# -*- coding: utf-8 -*-

import math
import sys
import time
from threading import Thread

from PyQt5 import QtCore, QtGui, QtWidgets

import ui.main_form
import ui.navigation
from remote_control.control import Control

dangers = ()

# dangers = (
#     (20, 20),
#     (-10, -50),
#     (40, 5),
#     (-45, 150)
# )

# import random
# dangers = [(random.randint(-50, 50), random.randint(-50, 50)) for x in range(250)]


class Vehicle:
    def __init__(self):
        # Параметры движения
        self.max_speed = 42
        self.acceleration = 0.6
        self.back_acceleration = 1.8
        self.turn_speed = 15
        self.has_tracks = True

        # Параметры вооружения
        self.ammo = 10
        self.gun_turn_speed = 30  # в секунду
        self.gun_vertical_speed = 7  # в секунду
        self.gun_max_angle = 20
        self.gun_min_angle = -15

        # Параметры защиты
        self.protect = 12

        # Расход топлива
        self.km_left = 160
        self.fuel_cons = 345

        # Внутренние параметры
        self.x = 0
        self.y = 0
        self.speed = 0
        self.distance = 0
        self.direction = math.radians(90)
        self.gun_angle = 0

        self._update_frequency = 60  # в секунду

        self._main_timer = QtCore.QTimer()
        self._main_timer.timeout.connect(self._timer_tick)
        self._main_timer.start(1000 / self._update_frequency)

    def _timer_tick(self):
        d_km = self.speed / (3600 * self._update_frequency)
        self.km_left -= self.fuel_cons / 100 * d_km
        if self.km_left <= 0:
            self.km_left = 0
            self.speed = 0
            d_km = 0
        self.distance += abs(d_km)
        d_km *= 1000  # переводим в метры
        self.x += d_km * math.cos(self.direction)
        self.y += d_km * math.sin(self.direction)

class MainUI(QtWidgets.QMainWindow, ui.main_form.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.navigation = ui.navigation.NavigationUI(self.groupBox_8)
        self.verticalLayout_5.insertWidget(1, self.navigation)
        self.is_nav_need_update = True

        self.tank_forward.clicked.connect(self.tank_forward_click)
        self.tank_back.clicked.connect(self.tank_back_click)
        self.tank_left.clicked.connect(self.tank_left_click)
        self.tank_right.clicked.connect(self.tank_right_click)
        self.tank_stop.clicked.connect(self.tank_stop_click)
        self.gun_left.clicked.connect(self.gun_left_click)
        self.gun_right.clicked.connect(self.gun_right_click)
        self.gun_up.clicked.connect(self.gun_up_click)
        self.gun_down.clicked.connect(self.gun_down_click)
        self.gun_fire.clicked.connect(self.gun_fire_click)
        self.tank_protect.clicked.connect(self.protect_click)

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.timer_tick)
        self.timer.start(1000 / 60)

        self.fps_timer = QtCore.QTimer()
        self.fps_timer.timeout.connect(self.show_fps)
        self.fps_timer.start(1000)

        self.vehicle = Vehicle()
        self.ammo_label.setText(str(self.vehicle.ammo))
        self.protect_label.setText(str(self.vehicle.protect))

        self.vehicle_direction = 0
        self.gun_direction = 0

        self.cache = {}
        self._update_cache()

        self.fps = 0

        control = Control('192.168.1.62', 1488, self, self.vehicle)
        control_listener = Thread(target=control.events_listener)
        control_listener.daemon = True
        control_listener.start()
        control_sender = Thread(target=control.events_sender)
        control_sender.daemon = True
        control_sender.start()

    def _update_cache(self):
        self.cache = {
            'speed': self.vehicle.speed,
            'distance': self.vehicle.distance,
            'x': self.vehicle.x,
            'y': self.vehicle.y,
            'vehicle_direct': self.vehicle_direction,
            'gun_direct': self.gun_direction,
            'km_left': self.vehicle.km_left
        }


    def timer_tick(self):
        if self.cache['speed'] != self.vehicle.speed:
            self.speed_label.setText('{:.2f}'.format(abs(self.vehicle.speed)))
        if self.cache['distance'] != self.vehicle.distance:
            self.distance_label.setText('{:.3f}'.format(self.vehicle.distance)[:-1])
        if self.cache['x'] != self.vehicle.x or self.cache['y'] != self.vehicle.y:
            self.coord_label.setText('{:.2f}, {:.2f}'.format(self.vehicle.x, self.vehicle.y))
        if self.cache['vehicle_direct'] != self.vehicle_direction:
            self.turn_label.setText('{:.2f}'.format(self.vehicle_direction))
        if self.cache['gun_direct'] != self.gun_direction:
            self.gun_turn_label.setText('{:.2f}'.format(self.gun_direction))
        if self.cache['km_left'] != self.vehicle.km_left:
            self.km_left_label.setText('{:.2f}'.format(self.vehicle.km_left))

        self._update_cache()

        self.navigation.dangers = []
        for x, y in dangers:
            d = math.sqrt((self.vehicle.x - x) ** 2 + (self.vehicle.y - y) ** 2)
            if d < 100:
                d_x = self.vehicle.x - x
                d_y = self.vehicle.y - y
                a = math.acos((abs(d_x) / d))
                a = math.degrees(a)
                result = {
                    (True, True): 270 + a,
                    (True, False): 270 - a,
                    (False, True): 90 - a,
                    (False, False): 90 + a,
                }[d_x > 0, d_y < 0]
                self.navigation.dangers.append(result)
        if self.is_nav_need_update:
            self.navigation.update()
            self.is_nav_need_update = False
        self.fps += 1

    def show_fps(self):
        self.setWindowTitle(f'Main UI Example [{self.fps} FPS]')
        self.fps = 0

    def tank_forward_click(self):
        self.vehicle.speed += self.vehicle.acceleration
        if self.vehicle.speed > self.vehicle.max_speed:
            self.vehicle.speed = self.vehicle.max_speed

    def tank_back_click(self):
        self.vehicle.speed -= self.vehicle.back_acceleration
        if self.vehicle.speed < 0:
            self.vehicle.speed = 0

    def tank_stop_click(self):
        self.vehicle.speed = 0

    def tank_left_click(self):  # 60 в секунду
        if not self.vehicle.km_left:
            return
        if not (self.vehicle.speed or self.vehicle.has_tracks):
            return
        self.vehicle_direction = (self.vehicle_direction - self.vehicle.turn_speed / 60) % 360
        # self.gun_direction = (self.gun_direction - self.vehicle.turn_speed / 60) % 360
        self.vehicle.direction += math.radians(self.vehicle.turn_speed / 60)
        self.navigation.rotate_compass(self.vehicle.turn_speed / 60)
        self.is_nav_need_update = True

    def tank_right_click(self):  # 60 в секунду
        if not self.vehicle.km_left:
            return
        if not (self.vehicle.speed or self.vehicle.has_tracks):
            return
        self.vehicle_direction = (self.vehicle_direction + self.vehicle.turn_speed / 60) % 360
        # self.gun_direction = (self.gun_direction + self.vehicle.turn_speed / 60) % 360
        self.vehicle.direction += math.radians(-self.vehicle.turn_speed / 60)
        self.navigation.rotate_compass(-self.vehicle.turn_speed / 60)
        self.is_nav_need_update = True

    def gun_left_click(self):
        self.gun_direction = (self.gun_direction - self.vehicle.gun_turn_speed / 60) % 360
        self.navigation.rotate_tank_gun(-self.vehicle.gun_turn_speed / 60)
        self.is_nav_need_update = True

    def gun_right_click(self):
        self.gun_direction = (self.gun_direction + self.vehicle.gun_turn_speed / 60) % 360
        self.navigation.rotate_tank_gun(self.vehicle.gun_turn_speed / 60)
        self.is_nav_need_update = True

    def gun_up_click(self):
        self.vehicle.gun_angle += self.vehicle.gun_vertical_speed / 60
        if self.vehicle.gun_angle > self.vehicle.gun_max_angle:
            self.vehicle.gun_angle = self.vehicle.gun_max_angle
        self.gun_angle_label.setText('{:.2f}'.format(self.vehicle.gun_angle))

    def gun_down_click(self):
        self.vehicle.gun_angle -= self.vehicle.gun_vertical_speed / 60
        if self.vehicle.gun_angle < self.vehicle.gun_min_angle:
            self.vehicle.gun_angle = self.vehicle.gun_min_angle
        self.gun_angle_label.setText('{:.2f}'.format(self.vehicle.gun_angle))

    def gun_fire_click(self):
        if self.vehicle.ammo:
            self.vehicle.ammo -= 1
            self.ammo_label.setText(str(self.vehicle.ammo))

    def protect_click(self):
        if self.vehicle.protect:
            self.vehicle.protect -= 1
            self.protect_label.setText(str(self.vehicle.protect))


def run():
    app = QtWidgets.QApplication(sys.argv)
    window = MainUI()
    window.show()
    app.exec_()


if __name__ == '__main__':
    run()
