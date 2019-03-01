# -*- coding: utf-8 -*-

import sys

from PyQt5 import QtCore, QtGui, QtWidgets


class NavigationUI(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.compass_angle = 0
        self.gun_angle = 0
        self.dangers = ()

    def paintEvent(self, e):
        self.center = round(self.width() / 2), round(self.height() / 2)

        self.paint = QtGui.QPainter()
        self.paint.begin(self)
        self.paint.setRenderHint(QtGui.QPainter.HighQualityAntialiasing)
        self.paint.translate(*self.center)
        self.draw_tank()
        self.draw_compass()
        self.draw_dangers()
        self.paint.end()

    def draw_compass(self):
        margin = 15
        radius = min(self.center) - margin
        long_mark_len = 20
        short_mark_len = 10
        step = 10
        pointText = {0: 'N', 90: 'E', 180: 'S', 270: 'W'}

        pen = QtGui.QPen(QtCore.Qt.black, 3, QtCore.Qt.SolidLine)
        self.paint.setPen(pen)

        self.paint.drawArc(-radius, -radius, radius * 2, radius * 2, 0, 360 * 16)

        font = QtGui.QFont('Times New Roman', 18)
        self.paint.setFont(font)
        metrics = QtGui.QFontMetricsF(font)
        self.paint.rotate(self.compass_angle)
        for i in range(0, 360, step):
            if i in pointText:
                self.paint.drawLine(0, -radius + 1, 0, -radius + long_mark_len)
                self.paint.drawText(-metrics.width(pointText[i]) / 2, -radius + metrics.height() + long_mark_len, pointText[i])
            else:
                self.paint.drawLine(0, -radius + 1, 0, -radius + short_mark_len)
            self.paint.rotate(step)

    def rotate_compass(self, angle):
        self.compass_angle = (self.compass_angle + angle) % 360

    def draw_tank(self):
        pen = QtGui.QPen(QtCore.Qt.black, 3, QtCore.Qt.SolidLine)
        self.paint.setPen(pen)

        # Body
        tank = QtGui.QPolygon([
            QtCore.QPoint(0, -80),
            QtCore.QPoint(-40, -40),
            QtCore.QPoint(-40, 80),
            QtCore.QPoint(40, 80),
            QtCore.QPoint(40, -40)
        ])
        self.paint.drawConvexPolygon(tank)

        # Gun
        self.paint.rotate(self.gun_angle)
        self.paint.setBrush(QtGui.QColor(0, 0, 0))
        self.paint.drawEllipse(-30, -30, 60, 60)
        self.paint.drawRect(-4, -90, 8, 90)
        self.paint.rotate(-self.gun_angle)

    def rotate_tank_gun(self, angle):
        self.gun_angle = (self.gun_angle + angle) % 360

    def draw_dangers(self):
        self.paint.setPen(QtGui.QPen(QtCore.Qt.red, 3, QtCore.Qt.SolidLine))
        self.paint.setBrush(QtGui.QColor(255, 0, 0, 127))

        for x in self.dangers:
            self.paint.rotate(x)
            self.paint.drawEllipse(-10, -min(self.center) + 5, 20, 20)
            self.paint.rotate(-x)

        # self.paint.setBrush(QtGui.QColor(255, 0, 0, 127))
        # pen = QtGui.QPen(QtCore.Qt.red, 3, QtCore.Qt.SolidLine)
        # self.paint.setPen(pen)
        # size = 220
        # self.paint.rotate(127)
        # self.paint.drawPie(-size / 2, -size / 2, size, size, 16 * 60, 16 * 60)
        # self.paint.rotate(-127)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = NavigationUI()
    window.show()
    app.exec_()