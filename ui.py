# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1024, 768)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox_6 = QtWidgets.QGroupBox(self.frame)
        self.groupBox_6.setMinimumSize(QtCore.QSize(0, 450))
        self.groupBox_6.setObjectName("groupBox_6")
        self.verticalLayout_2.addWidget(self.groupBox_6)
        self.groupBox_7 = QtWidgets.QGroupBox(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_7.sizePolicy().hasHeightForWidth())
        self.groupBox_7.setSizePolicy(sizePolicy)
        self.groupBox_7.setObjectName("groupBox_7")
        self.verticalLayout_2.addWidget(self.groupBox_7)
        self.horizontalLayout_2.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.groupBox_8 = QtWidgets.QGroupBox(self.frame_2)
        self.groupBox_8.setMinimumSize(QtCore.QSize(500, 500))
        self.groupBox_8.setObjectName("groupBox_8")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.groupBox_8)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.frame_14 = QtWidgets.QFrame(self.groupBox_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_14.sizePolicy().hasHeightForWidth())
        self.frame_14.setSizePolicy(sizePolicy)
        self.frame_14.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_14.setObjectName("frame_14")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.frame_14)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label_16 = QtWidgets.QLabel(self.frame_14)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_16.sizePolicy().hasHeightForWidth())
        self.label_16.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setAlignment(QtCore.Qt.AlignCenter)
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_12.addWidget(self.label_16)
        self.turn_label = QtWidgets.QLabel(self.frame_14)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.turn_label.sizePolicy().hasHeightForWidth())
        self.turn_label.setSizePolicy(sizePolicy)
        self.turn_label.setObjectName("turn_label")
        self.horizontalLayout_12.addWidget(self.turn_label)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem)
        self.label_14 = QtWidgets.QLabel(self.frame_14)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_12.addWidget(self.label_14)
        self.gun_turn_label = QtWidgets.QLabel(self.frame_14)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gun_turn_label.sizePolicy().hasHeightForWidth())
        self.gun_turn_label.setSizePolicy(sizePolicy)
        self.gun_turn_label.setMinimumSize(QtCore.QSize(32, 0))
        self.gun_turn_label.setObjectName("gun_turn_label")
        self.horizontalLayout_12.addWidget(self.gun_turn_label)
        self.verticalLayout_5.addWidget(self.frame_14)
        self.frame_10 = QtWidgets.QFrame(self.groupBox_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_10.sizePolicy().hasHeightForWidth())
        self.frame_10.setSizePolicy(sizePolicy)
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame_10)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_9 = QtWidgets.QLabel(self.frame_10)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_7.addWidget(self.label_9)
        self.coord_label = QtWidgets.QLabel(self.frame_10)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.coord_label.sizePolicy().hasHeightForWidth())
        self.coord_label.setSizePolicy(sizePolicy)
        self.coord_label.setObjectName("coord_label")
        self.horizontalLayout_7.addWidget(self.coord_label)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem1)
        self.label_10 = QtWidgets.QLabel(self.frame_10)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_7.addWidget(self.label_10)
        self.label_12 = QtWidgets.QLabel(self.frame_10)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy)
        self.label_12.setMinimumSize(QtCore.QSize(32, 0))
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_7.addWidget(self.label_12)
        self.verticalLayout_5.addWidget(self.frame_10)
        self.verticalLayout_3.addWidget(self.groupBox_8)
        self.groupBox_9 = QtWidgets.QGroupBox(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_9.sizePolicy().hasHeightForWidth())
        self.groupBox_9.setSizePolicy(sizePolicy)
        self.groupBox_9.setMinimumSize(QtCore.QSize(0, 200))
        self.groupBox_9.setObjectName("groupBox_9")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox_9)
        self.gridLayout.setObjectName("gridLayout")
        self.gun_left = QtWidgets.QPushButton(self.groupBox_9)
        self.gun_left.setMinimumSize(QtCore.QSize(107, 38))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.gun_left.setFont(font)
        self.gun_left.setStyleSheet("background: rgb(255, 255, 127)")
        self.gun_left.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/arrow_left.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.gun_left.setIcon(icon)
        self.gun_left.setAutoRepeat(True)
        self.gun_left.setAutoRepeatDelay(100)
        self.gun_left.setAutoRepeatInterval(16)
        self.gun_left.setObjectName("gun_left")
        self.gridLayout.addWidget(self.gun_left, 2, 3, 1, 1)
        self.gun_right = QtWidgets.QPushButton(self.groupBox_9)
        self.gun_right.setMinimumSize(QtCore.QSize(107, 38))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.gun_right.setFont(font)
        self.gun_right.setStyleSheet("background: rgb(255, 255, 127)")
        self.gun_right.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images/arrow_right.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.gun_right.setIcon(icon1)
        self.gun_right.setAutoRepeat(True)
        self.gun_right.setAutoRepeatDelay(100)
        self.gun_right.setAutoRepeatInterval(16)
        self.gun_right.setObjectName("gun_right")
        self.gridLayout.addWidget(self.gun_right, 2, 5, 1, 1)
        self.tank_left = QtWidgets.QPushButton(self.groupBox_9)
        self.tank_left.setMinimumSize(QtCore.QSize(107, 38))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.tank_left.setFont(font)
        self.tank_left.setText("")
        self.tank_left.setIcon(icon)
        self.tank_left.setAutoRepeat(True)
        self.tank_left.setAutoRepeatDelay(100)
        self.tank_left.setAutoRepeatInterval(16)
        self.tank_left.setObjectName("tank_left")
        self.gridLayout.addWidget(self.tank_left, 0, 3, 1, 1)
        self.tank_right = QtWidgets.QPushButton(self.groupBox_9)
        self.tank_right.setMinimumSize(QtCore.QSize(107, 38))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.tank_right.setFont(font)
        self.tank_right.setText("")
        self.tank_right.setIcon(icon1)
        self.tank_right.setAutoRepeat(True)
        self.tank_right.setAutoRepeatDelay(100)
        self.tank_right.setAutoRepeatInterval(16)
        self.tank_right.setObjectName("tank_right")
        self.gridLayout.addWidget(self.tank_right, 0, 5, 1, 1)
        self.gun_fire = QtWidgets.QPushButton(self.groupBox_9)
        self.gun_fire.setMinimumSize(QtCore.QSize(107, 38))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        self.gun_fire.setFont(font)
        self.gun_fire.setStyleSheet("background: rgb(255, 255, 127); color: red")
        self.gun_fire.setObjectName("gun_fire")
        self.gridLayout.addWidget(self.gun_fire, 2, 2, 1, 1)
        self.tank_forward = QtWidgets.QPushButton(self.groupBox_9)
        self.tank_forward.setMinimumSize(QtCore.QSize(107, 38))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.tank_forward.setFont(font)
        self.tank_forward.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("images/arrow_up.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tank_forward.setIcon(icon2)
        self.tank_forward.setAutoRepeat(True)
        self.tank_forward.setAutoRepeatDelay(0)
        self.tank_forward.setAutoRepeatInterval(100)
        self.tank_forward.setObjectName("tank_forward")
        self.gridLayout.addWidget(self.tank_forward, 0, 0, 1, 1)
        self.tank_back = QtWidgets.QPushButton(self.groupBox_9)
        self.tank_back.setMinimumSize(QtCore.QSize(107, 38))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.tank_back.setFont(font)
        self.tank_back.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("images/arrow_down.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tank_back.setIcon(icon3)
        self.tank_back.setAutoRepeat(True)
        self.tank_back.setAutoRepeatDelay(0)
        self.tank_back.setAutoRepeatInterval(100)
        self.tank_back.setObjectName("tank_back")
        self.gridLayout.addWidget(self.tank_back, 0, 1, 1, 1)
        self.gun_down = QtWidgets.QPushButton(self.groupBox_9)
        self.gun_down.setMinimumSize(QtCore.QSize(107, 38))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.gun_down.setFont(font)
        self.gun_down.setStyleSheet("background: rgb(255, 255, 127)")
        self.gun_down.setText("")
        self.gun_down.setIcon(icon3)
        self.gun_down.setAutoRepeat(True)
        self.gun_down.setAutoRepeatDelay(100)
        self.gun_down.setAutoRepeatInterval(16)
        self.gun_down.setObjectName("gun_down")
        self.gridLayout.addWidget(self.gun_down, 2, 1, 1, 1)
        self.gun_up = QtWidgets.QPushButton(self.groupBox_9)
        self.gun_up.setMinimumSize(QtCore.QSize(107, 38))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.gun_up.setFont(font)
        self.gun_up.setStyleSheet("background: rgb(255, 255, 127)")
        self.gun_up.setText("")
        self.gun_up.setIcon(icon2)
        self.gun_up.setAutoRepeat(True)
        self.gun_up.setAutoRepeatDelay(100)
        self.gun_up.setAutoRepeatInterval(16)
        self.gun_up.setObjectName("gun_up")
        self.gridLayout.addWidget(self.gun_up, 2, 0, 1, 1)
        self.pushButton_11 = QtWidgets.QPushButton(self.groupBox_9)
        self.pushButton_11.setMinimumSize(QtCore.QSize(107, 38))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        self.pushButton_11.setFont(font)
        self.pushButton_11.setStyleSheet("background: rgb(255, 255, 127)")
        self.pushButton_11.setObjectName("pushButton_11")
        self.gridLayout.addWidget(self.pushButton_11, 3, 2, 1, 1)
        self.tank_stop = QtWidgets.QPushButton(self.groupBox_9)
        self.tank_stop.setEnabled(True)
        self.tank_stop.setMinimumSize(QtCore.QSize(107, 38))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        self.tank_stop.setFont(font)
        self.tank_stop.setObjectName("tank_stop")
        self.gridLayout.addWidget(self.tank_stop, 0, 2, 1, 1)
        self.verticalLayout_3.addWidget(self.groupBox_9)
        self.horizontalLayout_2.addWidget(self.frame_2)
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setMinimumSize(QtCore.QSize(250, 0))
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox_4 = QtWidgets.QGroupBox(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_4.sizePolicy().hasHeightForWidth())
        self.groupBox_4.setSizePolicy(sizePolicy)
        self.groupBox_4.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.groupBox_4.setFont(font)
        self.groupBox_4.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_4.setFlat(False)
        self.groupBox_4.setCheckable(False)
        self.groupBox_4.setObjectName("groupBox_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox_4)
        self.verticalLayout_4.setContentsMargins(3, 3, 3, 3)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frame_4 = QtWidgets.QFrame(self.groupBox_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_3.setContentsMargins(3, 3, 3, 3)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(self.frame_4)
        self.label.setMinimumSize(QtCore.QSize(125, 0))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.speed_label = QtWidgets.QLabel(self.frame_4)
        self.speed_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.speed_label.setObjectName("speed_label")
        self.horizontalLayout_3.addWidget(self.speed_label)
        self.verticalLayout_4.addWidget(self.frame_4)
        self.frame_5 = QtWidgets.QFrame(self.groupBox_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_4.setContentsMargins(3, 3, 3, 3)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_2 = QtWidgets.QLabel(self.frame_5)
        self.label_2.setMinimumSize(QtCore.QSize(125, 0))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_4.addWidget(self.label_2)
        self.distance_label = QtWidgets.QLabel(self.frame_5)
        self.distance_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.distance_label.setObjectName("distance_label")
        self.horizontalLayout_4.addWidget(self.distance_label)
        self.verticalLayout_4.addWidget(self.frame_5)
        self.frame_6 = QtWidgets.QFrame(self.groupBox_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_6)
        self.horizontalLayout_5.setContentsMargins(3, 3, 3, 3)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_3 = QtWidgets.QLabel(self.frame_6)
        self.label_3.setMinimumSize(QtCore.QSize(125, 0))
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_5.addWidget(self.label_3)
        self.fuel_cons_label = QtWidgets.QLabel(self.frame_6)
        self.fuel_cons_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.fuel_cons_label.setObjectName("fuel_cons_label")
        self.horizontalLayout_5.addWidget(self.fuel_cons_label)
        self.verticalLayout_4.addWidget(self.frame_6)
        self.frame_7 = QtWidgets.QFrame(self.groupBox_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy)
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_7)
        self.horizontalLayout_6.setContentsMargins(3, 3, 3, 3)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_4 = QtWidgets.QLabel(self.frame_7)
        self.label_4.setMinimumSize(QtCore.QSize(125, 0))
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_6.addWidget(self.label_4)
        self.km_left_label = QtWidgets.QLabel(self.frame_7)
        self.km_left_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.km_left_label.setObjectName("km_left_label")
        self.horizontalLayout_6.addWidget(self.km_left_label)
        self.verticalLayout_4.addWidget(self.frame_7)
        self.verticalLayout.addWidget(self.groupBox_4)
        self.groupBox = QtWidgets.QGroupBox(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_6.setContentsMargins(3, 3, 3, 3)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.frame_8 = QtWidgets.QFrame(self.groupBox)
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_8)
        self.horizontalLayout.setContentsMargins(3, 3, 3, 3)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_5 = QtWidgets.QLabel(self.frame_8)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout.addWidget(self.label_5)
        self.ammo_label = QtWidgets.QLabel(self.frame_8)
        self.ammo_label.setObjectName("ammo_label")
        self.horizontalLayout.addWidget(self.ammo_label)
        self.verticalLayout_6.addWidget(self.frame_8)
        self.frame_12 = QtWidgets.QFrame(self.groupBox)
        self.frame_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.frame_12)
        self.horizontalLayout_10.setContentsMargins(3, 3, 3, 3)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_13 = QtWidgets.QLabel(self.frame_12)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_10.addWidget(self.label_13)
        self.gun_angle_label = QtWidgets.QLabel(self.frame_12)
        self.gun_angle_label.setObjectName("gun_angle_label")
        self.horizontalLayout_10.addWidget(self.gun_angle_label)
        self.verticalLayout_6.addWidget(self.frame_12)
        self.verticalLayout.addWidget(self.groupBox)
        self.groupBox_5 = QtWidgets.QGroupBox(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_5.sizePolicy().hasHeightForWidth())
        self.groupBox_5.setSizePolicy(sizePolicy)
        self.groupBox_5.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_5.setObjectName("groupBox_5")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.groupBox_5)
        self.verticalLayout_7.setContentsMargins(3, 3, 3, 3)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.frame_9 = QtWidgets.QFrame(self.groupBox_5)
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.frame_9)
        self.horizontalLayout_8.setContentsMargins(3, 3, 3, 3)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_6 = QtWidgets.QLabel(self.frame_9)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_8.addWidget(self.label_6)
        self.comboBox = QtWidgets.QComboBox(self.frame_9)
        self.comboBox.setObjectName("comboBox")
        self.horizontalLayout_8.addWidget(self.comboBox)
        self.verticalLayout_7.addWidget(self.frame_9)
        self.frame_11 = QtWidgets.QFrame(self.groupBox_5)
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.frame_11)
        self.horizontalLayout_9.setContentsMargins(3, 3, 3, 3)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_11 = QtWidgets.QLabel(self.frame_11)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_9.addWidget(self.label_11)
        self.comboBox_2 = QtWidgets.QComboBox(self.frame_11)
        self.comboBox_2.setObjectName("comboBox_2")
        self.horizontalLayout_9.addWidget(self.comboBox_2)
        self.verticalLayout_7.addWidget(self.frame_11)
        self.frame_13 = QtWidgets.QFrame(self.groupBox_5)
        self.frame_13.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_13.setObjectName("frame_13")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.frame_13)
        self.horizontalLayout_11.setContentsMargins(3, 3, 3, 3)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_15 = QtWidgets.QLabel(self.frame_13)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_11.addWidget(self.label_15)
        self.comboBox_3 = QtWidgets.QComboBox(self.frame_13)
        self.comboBox_3.setObjectName("comboBox_3")
        self.horizontalLayout_11.addWidget(self.comboBox_3)
        self.verticalLayout_7.addWidget(self.frame_13)
        self.verticalLayout.addWidget(self.groupBox_5)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.horizontalLayout_2.addWidget(self.frame_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1025, 21))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        MainWindow.setMenuBar(self.menubar)
        self.action = QtWidgets.QAction(MainWindow)
        self.action.setObjectName("action")
        self.action_2 = QtWidgets.QAction(MainWindow)
        self.action_2.setObjectName("action_2")
        self.action_3 = QtWidgets.QAction(MainWindow)
        self.action_3.setObjectName("action_3")
        self.action_4 = QtWidgets.QAction(MainWindow)
        self.action_4.setObjectName("action_4")
        self.action_5 = QtWidgets.QAction(MainWindow)
        self.action_5.setObjectName("action_5")
        self.action_7 = QtWidgets.QAction(MainWindow)
        self.action_7.setObjectName("action_7")
        self.menu.addAction(self.action_2)
        self.menu.addAction(self.action_4)
        self.menu.addSeparator()
        self.menu.addAction(self.action_3)
        self.menu.addAction(self.action_5)
        self.menu.addSeparator()
        self.menu.addAction(self.action_7)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Main UI Example"))
        self.groupBox_6.setTitle(_translate("MainWindow", "Управление защитой:"))
        self.groupBox_7.setTitle(_translate("MainWindow", "Параметры Пс-II:"))
        self.groupBox_8.setTitle(_translate("MainWindow", "Навигация:"))
        self.label_16.setText(_translate("MainWindow", "Угол поворота машины:"))
        self.turn_label.setText(_translate("MainWindow", "0"))
        self.label_14.setText(_translate("MainWindow", "Угол поворота пушки:"))
        self.gun_turn_label.setText(_translate("MainWindow", "0"))
        self.label_9.setText(_translate("MainWindow", "Координаты:"))
        self.coord_label.setText(_translate("MainWindow", "0, 0"))
        self.label_10.setText(_translate("MainWindow", "Высота (м):"))
        self.label_12.setText(_translate("MainWindow", "110"))
        self.groupBox_9.setTitle(_translate("MainWindow", "Управление движением:"))
        self.gun_fire.setText(_translate("MainWindow", "ОГОНЬ!"))
        self.pushButton_11.setText(_translate("MainWindow", "СТОП!"))
        self.tank_stop.setText(_translate("MainWindow", "СТОП!"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Параметры движения:"))
        self.label.setText(_translate("MainWindow", "Скорость (км/ч):"))
        self.speed_label.setText(_translate("MainWindow", "0"))
        self.label_2.setText(_translate("MainWindow", "Расстояние (км):"))
        self.distance_label.setText(_translate("MainWindow", "0"))
        self.label_3.setText(_translate("MainWindow", "Расход (л/100 км):"))
        self.fuel_cons_label.setText(_translate("MainWindow", "345"))
        self.label_4.setText(_translate("MainWindow", "Осталось (км):"))
        self.km_left_label.setText(_translate("MainWindow", "160"))
        self.groupBox.setTitle(_translate("MainWindow", "Параметры вооружения:"))
        self.label_5.setText(_translate("MainWindow", "Снарядов (шт):"))
        self.ammo_label.setText(_translate("MainWindow", "0"))
        self.label_13.setText(_translate("MainWindow", "Угол наклона пушки:"))
        self.gun_angle_label.setText(_translate("MainWindow", "0"))
        self.groupBox_5.setTitle(_translate("MainWindow", "Управление вооружением:"))
        self.label_6.setText(_translate("MainWindow", "Тип орудия:"))
        self.label_11.setText(_translate("MainWindow", "Боеприпасы:"))
        self.label_15.setText(_translate("MainWindow", "Тип стрельбы:"))
        self.menu.setTitle(_translate("MainWindow", "Файл"))
        self.menu_2.setTitle(_translate("MainWindow", "Тип УО"))
        self.action.setText(_translate("MainWindow", "Выход"))
        self.action_2.setText(_translate("MainWindow", "Старт..."))
        self.action_3.setText(_translate("MainWindow", "Сохранить"))
        self.action_4.setText(_translate("MainWindow", "Открыть..."))
        self.action_5.setText(_translate("MainWindow", "Сохранить как..."))
        self.action_7.setText(_translate("MainWindow", "Выход"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

