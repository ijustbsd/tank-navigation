# -*- coding: utf-8 -*-

import socket
import time

from . import protocol_pb2


class Control:
    def __init__(self, ui, vehicle):
        self.ui = ui
        self.vehicle = vehicle

        self.is_connected = False

        self.sender_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sender_sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

    def _create_listener_socket(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.bind(('0.0.0.0', 1400))
        sock.listen(1)
        return sock

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
            if not data:
                print(f'{addr[0]} disconnected!')
                sock.close()
                sock = self._create_listener_socket()
                print('Listening...')
                conn, addr = sock.accept()
                continue
            self._event_parser(data)

    def events_sender(self):
        print(f'ID: {self.vehicle.id_}. Sending...')
        while True:
            data = protocol_pb2.Data()
            data.id = str(self.vehicle.id_)
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
            self.sender_sock.sendto(data.SerializeToString(), ('255.255.255.255', 4242))
            time.sleep(1 / 60)
