# -*- coding: utf-8 -*-

import socket
import time

from . import protocol_pb2

class Control:
    def __init__(self, host, port, ui, vehicle):
        self.ui = ui
        self.vehicle = vehicle

        self.is_connected = False

    def _event_parser(self, data):
        act = protocol_pb2.Action()
        act.ParseFromString(data)
        try:
            getattr(self.ui, act.action + '_click')()
        except AttributeError:
            pass

    def _connect(self, host):
        self.sender_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sender_sock.connect((host, 1488))
        self.is_connected = True

    def _disconnect(self):
        self.is_connected = False

    def events_listener(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(('0.0.0.0', 1488))
        sock.listen(1)
        conn, addr = sock.accept()
        while True:
            data = conn.recv(1024)
            if not self.is_connected:
                self._connect(addr[0])
            if not data and self.is_connected:
                self._disconnect()
                conn, addr = sock.accept()
                continue
            self._event_parser(data)

    def events_sender(self):
        while True:
            if self.is_connected:
                data = protocol_pb2.Data()
                data.speed = self.vehicle.speed
                data.distance = self.vehicle.distance
                data.ammo = self.vehicle.ammo
                data.gun_angle = self.vehicle.gun_angle
                data.protect = self.vehicle.protect
                data.machine_turn = self.ui.vehicle_direction
                data.gun_turn = self.ui.gun_direction
                data.coords.x = self.vehicle.x
                data.coords.y = self.vehicle.y
                try:
                    self.sender_sock.sendall(data.SerializeToString())
                except BrokenPipeError:
                    pass
            time.sleep(1 / 60)