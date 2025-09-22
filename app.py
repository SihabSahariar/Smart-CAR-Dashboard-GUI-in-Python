# Developed By Sihab Sahariar
import io
import sys
import argparse

# import OpenCV module
import cv2

import folium # pip install folium

# PyQt5 imports - Core
from PyQt5.QtCore import QRect, QSize, QTimer, Qt, QCoreApplication, QMetaObject
# PyQt5 imports - GUI
from PyQt5.QtGui import QPixmap, QImage, QFont
# PyQt5 imports - Widgets
from PyQt5.QtWidgets import (
    QApplication, QWidget, QHBoxLayout, QLabel, QFrame, QPushButton,
    QSizePolicy, QProgressBar, QDial, QSlider, QMainWindow, QGridLayout
)

# PyQt5 Web Engine
from PyQt5.QtWebEngineWidgets import QWebEngineView # pip install PyQtWebEngine

# Custom widgets
from gauge import AnalogGaugeWidget
from qtwidgets import AnimatedToggle


class Ui_MainWindow(object):
    def __init__(self, video_path=None):
        self.video_path = video_path
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(1117, 636)
        MainWindow.setStyleSheet("background-color: rgb(30, 31, 40);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setGeometry(QRect(0, 0, 1111, 651))
        self.label.setText("")
        self.label.setPixmap(QPixmap(":/bg/Untitled (1).png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.frame = QFrame(self.centralwidget)
        self.frame.setGeometry(QRect(306, 60, 521, 61))
        self.frame.setStyleSheet("QFrame{\n"
"background:None;\n"
"}\n"
"\n"
"QPushButton{\n"
"    \n"
"    background-color: rgb(43,87,151,70);\n"
"    border:None;\n"
"    color:#fff;\n"
"    font: 10pt;\n"
"\n"
"}\n"
"QPushButton:Hover{\n"
"\n"
"    \n"
"    background-color: rgba(43,87,151,120);\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:Pressed{\n"
"    \n"
"    \n"
"background-color: rgba(43,87,120,100);\n"
"\n"
"}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_dash = QPushButton(self.frame)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_dash.sizePolicy().hasHeightForWidth())
        self.btn_dash.setSizePolicy(sizePolicy)
        self.btn_dash.setObjectName("btn_dash")
        self.horizontalLayout.addWidget(self.btn_dash)
        self.btn_ac = QPushButton(self.frame)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_ac.sizePolicy().hasHeightForWidth())
        self.btn_ac.setSizePolicy(sizePolicy)
        self.btn_ac.setObjectName("btn_ac")
        self.horizontalLayout.addWidget(self.btn_ac)
        self.btn_music = QPushButton(self.frame)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_music.sizePolicy().hasHeightForWidth())
        self.btn_music.setSizePolicy(sizePolicy)
        self.btn_music.setObjectName("btn_music")
        self.horizontalLayout.addWidget(self.btn_music)
        self.btn_map = QPushButton(self.frame)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_map.sizePolicy().hasHeightForWidth())
        self.btn_map.setSizePolicy(sizePolicy)
        self.btn_map.setObjectName("btn_map")
        self.horizontalLayout.addWidget(self.btn_map)
        self.frame_dashboard = QFrame(self.centralwidget)
        self.frame_dashboard.setEnabled(True)
        self.frame_dashboard.setGeometry(QRect(70, 120, 971, 411))
        self.frame_dashboard.setStyleSheet("QFrame{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(34, 46, 61), stop:1 rgba(34, 34, 47));\n"
"\n"
"border-radius:200px;\n"
"\n"
"}")
        self.frame_dashboard.setFrameShape(QFrame.StyledPanel)
        self.frame_dashboard.setFrameShadow(QFrame.Raised)
        self.frame_dashboard.setObjectName("frame_dashboard")
        self.speed = AnalogGaugeWidget(self.frame_dashboard)
        self.speed.setGeometry(QRect(30, 50, 311, 281))
        self.speed.setStyleSheet("background-color: rgb(85, 85, 127);\n"
"border-radius:o px;")
        self.speed.setObjectName("speed")
        self.rpm = AnalogGaugeWidget(self.frame_dashboard)
        self.rpm.setGeometry(QRect(630, 50, 311, 281))
        self.rpm.setStyleSheet("background-color: rgb(85, 85, 127);\n"
"border-radius:o px;")
        self.rpm.setObjectName("rpm")
        self.frame_2 = QFrame(self.frame_dashboard)
        self.frame_2.setGeometry(QRect(350, 30, 263, 38))
        self.frame_2.setStyleSheet("QFrame{\n"
"background-color: rgba(85, 85, 127,80);\n"
"border-radius:15px;\n"
"}\n"
"\n"
"QLabel{\n"
"background:None;\n"
"}")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setContentsMargins(0, 3, 0, 3)
        self.horizontalLayout_2.setSpacing(20)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_10 = QLabel(self.frame_2)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        self.label_10.setMaximumSize(QSize(40, 35))
        self.label_10.setText("")
        self.label_10.setPixmap(QPixmap(":/icon/steering.png"))
        self.label_10.setScaledContents(True)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_2.addWidget(self.label_10)
        self.label_13 = QLabel(self.frame_2)
        self.label_13.setMaximumSize(QSize(40, 35))
        self.label_13.setText("")
        self.label_13.setPixmap(QPixmap(":/icon/702814.png"))
        self.label_13.setScaledContents(True)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_2.addWidget(self.label_13)
        self.label_11 = QLabel(self.frame_2)
        self.label_11.setMaximumSize(QSize(40, 35))
        self.label_11.setText("")
        self.label_11.setPixmap(QPixmap(":/icon/748151.png"))
        self.label_11.setScaledContents(True)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_2.addWidget(self.label_11)
        self.label_12 = QLabel(self.frame_2)
        self.label_12.setMaximumSize(QSize(40, 35))
        self.label_12.setText("")
        self.label_12.setPixmap(QPixmap(":/icon/1442194.png"))
        self.label_12.setScaledContents(True)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_2.addWidget(self.label_12)
        self.frame_3 = QFrame(self.frame_dashboard)
        self.frame_3.setGeometry(QRect(370, 360, 221, 41))
        self.frame_3.setStyleSheet("background-color: rgba(85, 85, 127,80);\n"
"border-radius:15px;")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.date = QLabel(self.frame_3)
        self.date.setGeometry(QRect(30, 0, 171, 41))
        self.date.setStyleSheet("color:#fff;\n"
"font: 12pt \"MS UI Gothic\";\n"
"background:None;")
        self.date.setAlignment(Qt.AlignCenter)
        self.date.setObjectName("date")
        self.car_state = QFrame(self.frame_dashboard)
        self.car_state.setGeometry(QRect(350, 80, 271, 251))
        self.car_state.setStyleSheet("background:None;\n"
"color:#ee1111;")
        self.car_state.setFrameShape(QFrame.StyledPanel)
        self.car_state.setFrameShadow(QFrame.Raised)
        self.car_state.setObjectName("car_state")
        self.label_3 = QLabel(self.car_state)
        self.label_3.setGeometry(QRect(50, 10, 181, 231))
        self.label_3.setStyleSheet("background:None")
        self.label_3.setText("")
        self.label_3.setPixmap(QPixmap(":/icon/car.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.label_7 = QLabel(self.car_state)
        self.label_7.setGeometry(QRect(200, 150, 41, 16))
        self.label_7.setObjectName("label_7")
        self.label_5 = QLabel(self.car_state)
        self.label_5.setGeometry(QRect(200, 110, 31, 16))
        self.label_5.setStyleSheet("color:green;")
        self.label_5.setObjectName("label_5")
        self.label_4 = QLabel(self.car_state)
        self.label_4.setGeometry(QRect(40, 110, 41, 16))
        self.label_4.setObjectName("label_4")
        self.label_8 = QLabel(self.car_state)
        self.label_8.setGeometry(QRect(120, 50, 41, 16))
        self.label_8.setObjectName("label_8")
        self.label_9 = QLabel(self.car_state)
        self.label_9.setGeometry(QRect(120, 190, 55, 16))
        self.label_9.setStyleSheet("")
        self.label_9.setObjectName("label_9")
        self.label_6 = QLabel(self.car_state)
        self.label_6.setGeometry(QRect(40, 150, 41, 16))
        self.label_6.setObjectName("label_6")
        self.frame_4 = QFrame(self.frame_dashboard)
        self.frame_4.setGeometry(QRect(730, 340, 141, 42))
        self.frame_4.setStyleSheet("background-color: rgb(0, 85, 127,130);\n"
"border-radius:15px;")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_3 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_14 = QLabel(self.frame_4)
        self.label_14.setStyleSheet("color:#fff;\n"
"font: 12pt \"MS UI Gothic\";\n"
"background:None;")
        self.label_14.setAlignment(Qt.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_3.addWidget(self.label_14)
        self.progressBar_2 = QProgressBar(self.frame_4)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.progressBar_2.sizePolicy().hasHeightForWidth())
        self.progressBar_2.setSizePolicy(sizePolicy)
        self.progressBar_2.setMinimumSize(QSize(75, 0))
        self.progressBar_2.setStyleSheet("QProgressBar{\n"
"    background-color : rgb(141, 144, 147);\n"
"    \n"
"    color: rgb(0, 0, 0);\n"
"    border-style: none;\n"
"    border-radius: 5px;\n"
"    text-align: center;\n"
"}\n"
"\n"
"QProgressBar::chunk{\n"
"    border-radius: 5px;\n"
"    \n"
"    background-color: rgb(227,162,26,150);\n"
"}")
        self.progressBar_2.setProperty("value", 67)
        self.progressBar_2.setTextVisible(False)
        self.progressBar_2.setOrientation(Qt.Horizontal)
        self.progressBar_2.setInvertedAppearance(False)
        self.progressBar_2.setTextDirection(QProgressBar.TopToBottom)
        self.progressBar_2.setFormat("")
        self.progressBar_2.setObjectName("progressBar_2")
        self.horizontalLayout_3.addWidget(self.progressBar_2)
        self.frame_5 = QFrame(self.frame_dashboard)
        self.frame_5.setGeometry(QRect(100, 340, 141, 42))
        self.frame_5.setStyleSheet("background-color: rgb(152, 57, 38,100);\n"
"border-radius:15px;")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_4 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_15 = QLabel(self.frame_5)
        self.label_15.setStyleSheet("color:#fff;\n"
"font: 10pt \"MS UI Gothic\";\n"
"background:None;")
        self.label_15.setAlignment(Qt.AlignCenter)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_4.addWidget(self.label_15)
        self.label_16 = QLabel(self.centralwidget)
        self.label_16.setGeometry(QRect(460, 579, 181, 31))
        self.label_16.setStyleSheet("background:None;\n"
"color:#fff;")
        self.label_16.setAlignment(Qt.AlignCenter)
        self.label_16.setObjectName("label_16")
        self.frame_AC = QFrame(self.centralwidget)
        self.frame_AC.setGeometry(QRect(70, 120, 971, 411))
        self.frame_AC.setStyleSheet("QFrame{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(34, 46, 61), stop:1 rgba(34, 34, 47));\n"
"\n"
"border-radius:200px;\n"
"\n"
"}")
        self.frame_AC.setFrameShape(QFrame.StyledPanel)
        self.frame_AC.setFrameShadow(QFrame.Raised)
        self.frame_AC.setObjectName("frame_AC")
        self.circularProgressCPU = QFrame(self.frame_AC)
        self.circularProgressCPU.setGeometry(QRect(720, 80, 220, 220))
        self.circularProgressCPU.setStyleSheet("QFrame{\n"
"    border-radius: 110px;    \n"
"    background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:0.68 rgba(85, 170, 255, 255), stop:0.612 rgba(255, 255, 255, 0));\n"
"}")
        self.circularProgressCPU.setFrameShape(QFrame.StyledPanel)
        self.circularProgressCPU.setFrameShadow(QFrame.Raised)
        self.circularProgressCPU.setObjectName("circularProgressCPU")
        self.circularOutdoor = QFrame(self.circularProgressCPU)
        self.circularOutdoor.setGeometry(QRect(15, 15, 190, 190))
        self.circularOutdoor.setBaseSize(QSize(0, 0))
        self.circularOutdoor.setStyleSheet("QFrame{\n"
"    border-radius: 95px;    \n"
"    background-color: rgb(58, 58, 102);\n"
"}")
        self.circularOutdoor.setFrameShape(QFrame.StyledPanel)
        self.circularOutdoor.setFrameShadow(QFrame.Raised)
        self.circularOutdoor.setObjectName("circularOutdoor")
        self.labelPercentageCPU = QLabel(self.circularOutdoor)
        self.labelPercentageCPU.setGeometry(QRect(40, 50, 132, 100))
        font = QFont()
        font.setFamily("Roboto Thin")
        font.setPointSize(30)
        self.labelPercentageCPU.setFont(font)
        self.labelPercentageCPU.setStyleSheet("color: rgb(115, 185, 255); padding: 0px; background-color: none;")
        self.labelPercentageCPU.setAlignment(Qt.AlignCenter)
        self.labelPercentageCPU.setIndent(-1)
        self.labelPercentageCPU.setObjectName("labelPercentageCPU")
        self.label_19 = QLabel(self.circularOutdoor)
        self.label_19.setGeometry(QRect(40, 30, 131, 51))
        font = QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(10)
        self.label_19.setFont(font)
        self.label_19.setStyleSheet("QLabel\n"
"{\n"
"background:None;\n"
"color:rgb(255,255,255,100);\n"
"}")
        self.label_19.setAlignment(Qt.AlignCenter)
        self.label_19.setObjectName("label_19")
        self.weather = QFrame(self.frame_AC)
        self.weather.setGeometry(QRect(330, 10, 341, 351))
        self.weather.setStyleSheet("QFrame{\n"
"border-radius:5px;\n"
"background-color: rgb(14, 22, 39);\n"
"}")
        self.weather.setFrameShape(QFrame.StyledPanel)
        self.weather.setFrameShadow(QFrame.Raised)
        self.weather.setObjectName("weather")
        self.label_18 = QLabel(self.weather)
        self.label_18.setGeometry(QRect(50, 10, 261, 20))
        font = QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(12)
        self.label_18.setFont(font)
        self.label_18.setStyleSheet("QLabel\n"
"{\n"
"background:None;\n"
"color:rgb(227,162,26);\n"
"}")
        self.label_18.setAlignment(Qt.AlignCenter)
        self.label_18.setObjectName("label_18")
        self.label_2 = QLabel(self.weather)
        self.label_2.setGeometry(QRect(10, 60, 101, 81))
        self.label_2.setText("")
        self.label_2.setPixmap(QPixmap(":/icons/p.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_17 = QLabel(self.weather)
        self.label_17.setGeometry(QRect(210, 60, 121, 81))
        self.label_17.setStyleSheet("color:#fff")
        self.label_17.setObjectName("label_17")
        self.frame_6 = QFrame(self.weather)
        self.frame_6.setGeometry(QRect(30, 250, 281, 81))
        self.frame_6.setStyleSheet("color:#fff;")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.gridLayout = QGridLayout(self.frame_6)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setHorizontalSpacing(30)
        self.gridLayout.setVerticalSpacing(11)
        self.gridLayout.setObjectName("gridLayout")
        self.label_24 = QLabel(self.frame_6)
        self.label_24.setText("")
        self.label_24.setPixmap(QPixmap(":/bg/289759.png"))
        self.label_24.setScaledContents(True)
        self.label_24.setObjectName("label_24")
        self.gridLayout.addWidget(self.label_24, 0, 2, 1, 1)
        self.label_23 = QLabel(self.frame_6)
        self.label_23.setText("")
        self.label_23.setPixmap(QPixmap(":/icons/95252.png"))
        self.label_23.setScaledContents(True)
        self.label_23.setObjectName("label_23")
        self.gridLayout.addWidget(self.label_23, 0, 1, 1, 1)
        self.label_22 = QLabel(self.frame_6)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_22.sizePolicy().hasHeightForWidth())
        self.label_22.setSizePolicy(sizePolicy)
        self.label_22.setStyleSheet("")
        self.label_22.setText("")
        self.label_22.setPixmap(QPixmap(":/icons/567255.png"))
        self.label_22.setScaledContents(True)
        self.label_22.setObjectName("label_22")
        self.gridLayout.addWidget(self.label_22, 0, 0, 1, 1)
        self.label_25 = QLabel(self.frame_6)
        self.label_25.setAlignment(Qt.AlignCenter)
        self.label_25.setObjectName("label_25")
        self.gridLayout.addWidget(self.label_25, 1, 0, 1, 1)
        self.label_26 = QLabel(self.frame_6)
        self.label_26.setAlignment(Qt.AlignCenter)
        self.label_26.setObjectName("label_26")
        self.gridLayout.addWidget(self.label_26, 1, 1, 1, 1)
        self.label_27 = QLabel(self.frame_6)
        self.label_27.setAlignment(Qt.AlignCenter)
        self.label_27.setObjectName("label_27")
        self.gridLayout.addWidget(self.label_27, 1, 2, 1, 1)
        self.labelPercentageCPU_4 = QLabel(self.weather)
        self.labelPercentageCPU_4.setGeometry(QRect(110, 80, 71, 41))
        font = QFont()
        font.setFamily("Roboto Thin")
        font.setPointSize(13)
        self.labelPercentageCPU_4.setFont(font)
        self.labelPercentageCPU_4.setStyleSheet("color: rgb(115, 185, 255,70); \n"
"padding: 0px;\n"
" background-color: none;")
        self.labelPercentageCPU_4.setAlignment(Qt.AlignCenter)
        self.labelPercentageCPU_4.setIndent(-1)
        self.labelPercentageCPU_4.setObjectName("labelPercentageCPU_4")
        self.line = QFrame(self.weather)
        self.line.setGeometry(QRect(194, 81, 3, 40))
        self.line.setStyleSheet("background-color: rgba(85, 85, 255,120);")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.line.setObjectName("line")
        self.circularIndoor = QFrame(self.frame_AC)
        self.circularIndoor.setGeometry(QRect(70, 90, 220, 220))
        self.circularIndoor.setStyleSheet("QFrame{\n"
"    border-radius: 110px;    \n"
"    background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:0.88 rgba(255,196,13,255), stop:0.712 rgba(255, 255, 255, 0));\n"
"}")
        self.circularIndoor.setFrameShape(QFrame.StyledPanel)
        self.circularIndoor.setFrameShadow(QFrame.Raised)
        self.circularIndoor.setObjectName("circularIndoor")
        self.circularOutdoor_2 = QFrame(self.circularIndoor)
        self.circularOutdoor_2.setGeometry(QRect(15, 15, 190, 190))
        self.circularOutdoor_2.setBaseSize(QSize(0, 0))
        self.circularOutdoor_2.setStyleSheet("QFrame{\n"
"    border-radius: 95px;    \n"
"    background-color: rgb(43,87,151);\n"
"}")
        self.circularOutdoor_2.setFrameShape(QFrame.StyledPanel)
        self.circularOutdoor_2.setFrameShadow(QFrame.Raised)
        self.circularOutdoor_2.setObjectName("circularOutdoor_2")
        self.labelPercentageCPU_3 = QLabel(self.circularOutdoor_2)
        self.labelPercentageCPU_3.setGeometry(QRect(40, 50, 132, 100))
        font = QFont()
        font.setFamily("Roboto Thin")
        font.setPointSize(30)
        self.labelPercentageCPU_3.setFont(font)
        self.labelPercentageCPU_3.setStyleSheet("color: rgb(115, 185, 255); padding: 0px; background-color: none;")
        self.labelPercentageCPU_3.setAlignment(Qt.AlignCenter)
        self.labelPercentageCPU_3.setIndent(-1)
        self.labelPercentageCPU_3.setObjectName("labelPercentageCPU_3")
        self.label_21 = QLabel(self.circularOutdoor_2)
        self.label_21.setGeometry(QRect(40, 30, 131, 51))
        font = QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(10)
        self.label_21.setFont(font)
        self.label_21.setStyleSheet("QLabel\n"
"{\n"
"background:None;\n"
"color:rgb(255,255,255,100);\n"
"}")
        self.label_21.setAlignment(Qt.AlignCenter)
        self.label_21.setObjectName("label_21")
        self.checked = AnimatedToggle(self.frame_AC)
        self.checked.setGeometry(QRect(140, 310, 100, 50))
        self.frame_music = QFrame(self.centralwidget)
        self.frame_music.setGeometry(QRect(70, 120, 971, 411))
        self.frame_music.setStyleSheet("QFrame{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(34, 46, 61), stop:1 rgba(34, 34, 47));\n"
"\n"
"border-radius:200px;\n"
"\n"
"}")
        self.frame_music.setFrameShape(QFrame.StyledPanel)
        self.frame_music.setFrameShadow(QFrame.Raised)
        self.frame_music.setObjectName("frame_music")
        self.dial = QDial(self.frame_music)
        self.dial.setGeometry(QRect(40, 100, 220, 220))
        self.dial.setProperty("value", 16)
        self.dial.setInvertedAppearance(False)
        self.dial.setInvertedControls(False)
        self.dial.setWrapping(False)
        self.dial.setNotchesVisible(False)
        self.dial.setObjectName("dial")
        self.horizontalSlider = QSlider(self.frame_music)
        self.horizontalSlider.setGeometry(QRect(150, 360, 651, 21))
        self.horizontalSlider.setStyleSheet("\n"
"QSlider::groove:horizontal {\n"
"background-color: rgb(31, 119, 180);\n"
"height: 20px;\n"
"\n"
"border-radius: 9px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    width: 20px;\n"
"    background-image: url(:/icon/pin.png);\n"
"}\n"
"\n"
"QSlider::add-page:qlineargradient {\n"
"background: lightgrey;\n"
"border-top-right-radius: 9px;\n"
"border-bottom-right-radius: 9px;\n"
"border-top-left-radius: 0px;\n"
"border-bottom-left-radius: 0px;\n"
"}\n"
"\n"
"")
        self.horizontalSlider.setMaximum(100)
        self.horizontalSlider.setProperty("value", 35)
        self.horizontalSlider.setOrientation(Qt.Horizontal)
        self.horizontalSlider.setInvertedAppearance(False)
        self.horizontalSlider.setInvertedControls(False)
        self.horizontalSlider.setTickInterval(0)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.dial_2 = QDial(self.frame_music)
        self.dial_2.setGeometry(QRect(730, 100, 220, 220))
        self.dial_2.setProperty("value", 55)
        self.dial_2.setInvertedAppearance(False)
        self.dial_2.setInvertedControls(False)
        self.dial_2.setWrapping(False)
        self.dial_2.setNotchesVisible(False)
        self.dial_2.setObjectName("dial_2")
        self.label_20 = QLabel(self.frame_music)
        self.label_20.setGeometry(QRect(100, 80, 91, 31))
        self.label_20.setStyleSheet("color: rgb(23, 190, 207);\n"
"font: 75 12pt \"Nirmala UI\";\n"
"background:None;")
        self.label_20.setAlignment(Qt.AlignCenter)
        self.label_20.setObjectName("label_20")
        self.label_28 = QLabel(self.frame_music)
        self.label_28.setGeometry(QRect(820, 70, 51, 31))
        self.label_28.setStyleSheet("color: rgb(23, 190, 207);\n"
"font: 75 12pt \"Nirmala UI\";\n"
"background:None;")
        self.label_28.setObjectName("label_28")
        self.label_29 = QLabel(self.frame_music)
        self.label_29.setGeometry(QRect(400, 80, 161, 161))
        self.label_29.setStyleSheet("background:None;")
        self.label_29.setText("")
        self.label_29.setPixmap(QPixmap(":/music/music.png"))
        self.label_29.setScaledContents(True)
        self.label_29.setObjectName("label_29")
        self.label_30 = QLabel(self.frame_music)
        self.label_30.setGeometry(QRect(400, 310, 32, 32))
        self.label_30.setStyleSheet("background:None;")
        self.label_30.setText("")
        self.label_30.setPixmap(QPixmap(":/music/2.png"))
        self.label_30.setScaledContents(True)
        self.label_30.setObjectName("label_30")
        self.label_31 = QLabel(self.frame_music)
        self.label_31.setGeometry(QRect(460, 300, 40, 40))
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_31.sizePolicy().hasHeightForWidth())
        self.label_31.setSizePolicy(sizePolicy)
        self.label_31.setMinimumSize(QSize(40, 40))
        self.label_31.setMaximumSize(QSize(40, 40))
        self.label_31.setStyleSheet("background:None;")
        self.label_31.setText("")
        self.label_31.setPixmap(QPixmap(":/music/151859.png"))
        self.label_31.setScaledContents(True)
        self.label_31.setObjectName("label_31")
        self.label_32 = QLabel(self.frame_music)
        self.label_32.setGeometry(QRect(530, 310, 32, 32))
        self.label_32.setStyleSheet("background:None;")
        self.label_32.setText("")
        self.label_32.setPixmap(QPixmap(":/music/3.png"))
        self.label_32.setScaledContents(True)
        self.label_32.setObjectName("label_32")
        self.label_33 = QLabel(self.frame_music)
        self.label_33.setGeometry(QRect(260, 260, 481, 31))
        self.label_33.setStyleSheet("color: rgb(23, 190, 207);\n"
"font: 75 12pt \"Nirmala UI\";\n"
"background:None;")
        self.label_33.setAlignment(Qt.AlignCenter)
        self.label_33.setObjectName("label_33")
        self.frame_map = QFrame(self.centralwidget)
        self.frame_map.setGeometry(QRect(70, 120, 971, 411))
        self.frame_map.setStyleSheet("QFrame{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(34, 46, 61), stop:1 rgba(34, 34, 47));\n"
"\n"
"border-radius:200px;\n"
"\n"
"}\n"
"QPushButton{\n"
"    \n"
"    background-color: rgba(0,171,169,80);\n"
"    border:None;\n"
"    color:#fff;\n"
"    font: 10pt;\n"
"\n"
"}\n"
"QPushButton:Hover{\n"
"\n"
"    \n"
"    background-color: rgba(0,171,169,120);\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:Pressed{\n"
"    \n"
"    \n"
"background-color: rgba(0,171,169,100);\n"
"\n"
"}")
        self.frame_map.setFrameShape(QFrame.NoFrame)
        self.frame_map.setFrameShadow(QFrame.Raised)
        self.frame_map.setObjectName("frame_map")

        coordinate = (24.413274773214205, 88.96567734902074)
        m = folium.Map(
            tiles='OpenStreetMap',
            zoom_start=10,
            location=coordinate
        )

        # save map data to data object
        data = io.BytesIO()
        m.save(data, close_file=False)

        self.map_plot = QWebEngineView(self.frame_map)
        self.map_plot.setHtml(data.getvalue().decode())
        self.map_plot.setObjectName(u"map_plot")
        self.map_plot.setGeometry(QRect(100, 40, 391, 331))
        self.pushButton_5 = QPushButton(self.frame_map)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(830, 240, 119, 37))
        sizePolicy.setHeightForWidth(self.pushButton_5.sizePolicy().hasHeightForWidth())
        self.pushButton_5.setSizePolicy(sizePolicy)
        self.pushButton_6 = QPushButton(self.frame_map)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setGeometry(QRect(830, 190, 119, 37))
        sizePolicy.setHeightForWidth(self.pushButton_6.sizePolicy().hasHeightForWidth())
        self.pushButton_6.setSizePolicy(sizePolicy)
        global timer
        self.timer = QTimer()
        # set timer timeout callback function
        self.timer.timeout.connect(self.view_video)

        self.webcam = QLabel(self.frame_map)
        self.webcam.setObjectName(u"webcam")
        self.webcam.setGeometry(QRect(500, 40, 321, 331))

        MainWindow.setCentralWidget(self.centralwidget)
        self.show_dashboard()
        self.progress()
        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)
        self.label_km = QLabel(self.speed)
        self.label_km.setText("Km/h")
        self.label_km.setGeometry(QRect(130, 190, 57, 16))
        self.label_km.setStyleSheet(u"\n"
"color:#fff;\n"
"    font: 15pt;\n"
"background:None;\n"
"\n"
)
        self.label_km.setAlignment(Qt.AlignCenter)

    def view_video(self):
        ret, image = cap.read()
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        height, width, channel = image.shape
        step = channel * width
        qImg = QImage(image.data, width, height, step, QImage.Format_RGB888)
        self.webcam.setPixmap(QPixmap.fromImage(qImg))

    def quit_video(self):
        self.timer.stop()
        # TODO: using globals() to avoid application crash might be not the most elegant solution (re-design???).
        if "cap" in globals():
            cap.release()

    def controlTimer(self):
        global cap
        # TODO: this method toggles the timer state, is it really needed, what is the scenario?
        if self.timer.isActive():
            self.quit_video()
        else:
            # Use video file if provided, otherwise use camera device 0
            if self.video_path:
                cap = cv2.VideoCapture(self.video_path)
            else:
                cap = cv2.VideoCapture(0)
            self.timer.start(20)

    def retranslateUi(self, MainWindow):
        _translate = QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("CAR DASHBOARD", "MainWindow"))
        self.btn_dash.setText(_translate("MainWindow", "DASHBOARD"))
        self.btn_ac.setText(_translate("MainWindow", "AC"))
        self.btn_music.setText(_translate("MainWindow", "MUSIC"))
        self.btn_map.setText(_translate("MainWindow", "MAP"))
        self.date.setText(_translate("MainWindow", "Date - Time-"))
        self.label_7.setText(_translate("MainWindow", "Locked"))
        self.label_5.setText(_translate("MainWindow", "Open"))
        self.label_4.setText(_translate("MainWindow", "Locked"))
        self.label_8.setText(_translate("MainWindow", "Locked"))
        self.label_9.setText(_translate("MainWindow", "Locked"))
        self.label_6.setText(_translate("MainWindow", "Locked"))
        self.label_14.setText(_translate("MainWindow", "Fuel:"))
        self.label_15.setText(_translate("MainWindow", "Door Unlocked"))
        self.label_16.setText(_translate("MainWindow", "(C)2021-Sihab Sahariar"))
        self.labelPercentageCPU.setText(_translate("MainWindow", "<html><head/><body><p>29°C</p></body></html>"))
        self.label_19.setText(_translate("MainWindow", "Outdoor\n"
"Temperature"))
        self.label_18.setText(_translate("MainWindow", "Weather Forecast"))
        self.label_17.setText(_translate("MainWindow", "Precipitation: 20%\n"
"Humidity: 70%\n"
"Wind: 32 km/h"))
        self.label_25.setText(_translate("MainWindow", "Mode1"))
        self.label_26.setText(_translate("MainWindow", "Mode2"))
        self.label_27.setText(_translate("MainWindow", "Mode3"))
        self.labelPercentageCPU_4.setText(_translate("MainWindow", "<html><head/><body><p>Cloudy</p></body></html>"))
        self.labelPercentageCPU_3.setText(_translate("MainWindow", "<html><head/><body><p>20°C</p></body></html>"))
        self.label_21.setText(_translate("MainWindow", "Indoor\n"
"Temperature"))
        self.checked.setText(_translate("MainWindow", "PushButton"))
        self.label_20.setText(_translate("MainWindow", "Volume"))
        self.label_28.setText(_translate("MainWindow", "Mixer"))
        self.label_33.setText(_translate("MainWindow", "02. Mrittu Utpadon Karkhana - Shonar Bangla Circus"))
        self.pushButton_5.setText(_translate("MainWindow", "Start"))
        self.pushButton_6.setText(_translate("MainWindow", "Stop"))
        # btn function
        self.btn_dash.clicked.connect(self.show_dashboard)
        self.btn_ac.clicked.connect(self.show_AC)
        self.btn_music.clicked.connect(self.show_Music)
        self.btn_map.clicked.connect(self.show_Map)

    def show_dashboard(self):
        if self.frame_dashboard.isVisible():
            return
        self.quit_video()
        self.frame_dashboard.setVisible(True)
        self.frame_AC.setVisible(False)
        self.frame_music.setVisible(False)
        self.frame_map.setVisible(False)

    def show_AC(self):
        if self.frame_AC.isVisible():
            return
        self.quit_video()
        self.frame_dashboard.setVisible(False)
        self.frame_AC.setVisible(True)
        self.frame_music.setVisible(False)
        self.frame_map.setVisible(False)

    def show_Music(self):
        if self.frame_music.isVisible():
            return
        self.quit_video()
        self.frame_dashboard.setVisible(False)
        self.frame_AC.setVisible(False)
        self.frame_music.setVisible(True)
        self.frame_map.setVisible(False)

    def show_Map(self):
        if self.frame_map.isVisible():
            return
        self.frame_dashboard.setVisible(False)
        self.frame_AC.setVisible(False)
        self.frame_music.setVisible(False)
        self.frame_map.setVisible(True)
        self.controlTimer()

    def progress(self):
        self.speed.set_MaxValue(100)
        self.speed.set_DisplayValueColor(200,200,200)
        self.speed.set_CenterPointColor(255,255,255)
        self.speed.set_NeedleColor(255,255,200)
        self.speed.set_NeedleColorDrag(255,255,255)
        self.speed.set_ScaleValueColor(255,200,255)
        self.speed.set_enable_big_scaled_grid(True)
        self.speed.set_enable_barGraph(False)
        self.speed.set_enable_filled_Polygon(False)
        self.speed.update_value(65)

        self.rpm.set_scala_main_count(6)
        self.rpm.set_MaxValue(6)
        self.rpm.set_MinValue(0)
        self.rpm.update_value(3.5)
        self.rpm.set_DisplayValueColor(200,200,200)
        self.rpm.set_enable_big_scaled_grid(True)
        self.rpm.set_ScaleValueColor(255,255,255)
        self.rpm.set_NeedleColorDrag(255,255,255)
        self.rpm.set_CenterPointColor(255,255,255)


# This import is very much needed! It's a compiled Qt resource file.
# The file contains embedded binary data for all the images and assets used in the Smart Car Dashboard GUI.
# The GUI uses resource paths extensively via references to Qt resource paths like:
# ":/bg/Untitled (1).png" (background images)
# ":/icon/steering.png" (steering wheel icon)
# And many more icons and images.
# Without it, the GUI would be broken: the application would run, but all images would be missing,
# leaving some UI screens with a blank/broken interface.
# The "resources.py" file was generated by PyQt5's resource compiler and
# contains all the visual assets the dashboard needs.

# noinspection PyUnusedImports
import resources

if __name__ == "__main__":
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description='Smart Car Dashboard GUI')
    parser.add_argument('--play-video', metavar='path', type=str, help='[Optional] path to video file to play instead of camera')
    args = parser.parse_args()
    
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow(video_path=args.play_video)
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
