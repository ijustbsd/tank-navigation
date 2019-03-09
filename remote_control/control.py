# -*- coding: utf-8 -*-

import socket
import time

from . import protocol_pb2

class Control:
    def __init__(self, ui, vehicle):
        self.ui = ui
        self.vehicle = vehicle

        self.is_connected = False

    def _connect(self, host):
        self.sender_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.sender_sock.connect((host, 1488))
        except ConnectionRefusedError:
            self.events_listener()
            return
        self.is_connected = True
        print(f'{host} connected!')

    def _create_listener_socket(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.bind(('0.0.0.0', 1488))
        sock.listen(1)
        return sock

    def _disconnect(self):
        print(456)
        self.is_connected = False

    def _event_parser(self, data):
        act = protocol_pb2.Action()
        act.ParseFromString(data)
        try:
            getattr(self.ui, act.action + '_click')()
        except AttributeError:
            pass

    def events_listener(self):
        sock = self._create_listener_socket()
        print('Listening...')
        conn, addr = sock.accept()
        while True:
            data = conn.recv(1024)
            if not self.is_connected:
                self._connect(addr[0])
            if not data and self.is_connected:
                print(f'{addr[0]} disconnected!')
                self._disconnect()
                sock.close()
                sock = self._create_listener_socket()
                print('Listening...')
                conn, addr = sock.accept()
                continue
            self._event_parser(data)

    def events_sender(self):
        while True:
            if self.is_connected:
                data = protocol_pb2.Data()
                data.speed = self.vehicle.speed
                data.distance = self.vehicle.distance
                data.km_left = self.vehicle.km_left
                data.ammo = self.vehicle.ammo
                data.gun_angle = self.vehicle.gun_angle
                data.protect = self.vehicle.protect
                data.machine_turn = self.ui.vehicle_direction
                data.gun_turn = self.ui.gun_direction
                data.x = self.vehicle.x
                data.y = self.vehicle.y
                try:
                    self.sender_sock.sendall(data.SerializeToString())
                except BrokenPipeError:
                    pass
            time.sleep(1 / 60)