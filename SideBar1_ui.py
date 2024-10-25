# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SideBar1.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QStackedWidget, QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1145, 842)
        MainWindow.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"\n"
"\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.icon_only_widget = QWidget(self.centralwidget)
        self.icon_only_widget.setObjectName(u"icon_only_widget")
        self.icon_only_widget.setMinimumSize(QSize(61, 791))
        self.icon_only_widget.setStyleSheet(u"QWidget{\n"
"background-color:#1F95EF;\n"
"}\n"
"\n"
"QPushButton{\n"
"	color:White ;\n"
"	border:none;\n"
"   height:30px;\n"
"border-top-left-radius:10px;\n"
"	border-bottom-left-radius:10px;	\n"
"}\n"
"QPushButton:checked{\n"
"	background-color:#F5FAFE;\n"
"	color:#1F95EF;\n"
"	font-weight:bold;\n"
"}")
        self.label = QLabel(self.icon_only_widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 20, 40, 40))
        self.label.setMaximumSize(QSize(40, 40))
        self.label.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.label.setPixmap(QPixmap(u"../../Learn-PyQt6/Assets.qrc/profile_pic.png"))
        self.label.setScaledContents(True)
        self.label.setWordWrap(False)
        self.pushButton_6 = QPushButton(self.icon_only_widget)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setGeometry(QRect(10, 710, 41, 26))
        icon = QIcon()
        icon.addFile(u"../../Learn-PyQt6/Gestion_De_Stock/resources.qrc/log_out_white.png", QSize(), QIcon.Normal, QIcon.Off)
        icon.addFile(u"../../Learn-PyQt6/Gestion_De_Stock/resources.qrc/log_out.png", QSize(), QIcon.Normal, QIcon.On)
        self.pushButton_6.setIcon(icon)
        self.pushButton_6.setCheckable(True)
        self.pushButton_6.setChecked(False)
        self.layoutWidget = QWidget(self.icon_only_widget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 100, 41, 221))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.Dashbor = QPushButton(self.layoutWidget)
        self.Dashbor.setObjectName(u"Dashbor")
        self.Dashbor.setStyleSheet(u"QPushButton{\n"
"	\n"
"	border:none;\n"
"   height:30px;\n"
"border-top-left-radius:10px;\n"
"	border-bottom-left-radius:10px;	\n"
"}\n"
"QPushButton:checked{\n"
"		background-color:#F5FAFE;\n"
"	color:#1F95EF;\n"
"	font-weight:bold;\n"
"}\n"
"")
        icon1 = QIcon()
        icon1.addFile(u"../../Learn-PyQt6/Gestion_De_Stock/resources.qrc/dashboard_white.png", QSize(), QIcon.Normal, QIcon.Off)
        icon1.addFile(u"../../Learn-PyQt6/Gestion_De_Stock/resources.qrc/dashboard.png", QSize(), QIcon.Normal, QIcon.On)
        self.Dashbor.setIcon(icon1)
        self.Dashbor.setCheckable(True)
        self.Dashbor.setChecked(True)
        self.Dashbor.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.Dashbor)

        self.Profil = QPushButton(self.layoutWidget)
        self.Profil.setObjectName(u"Profil")
        icon2 = QIcon()
        icon2.addFile(u"../../Learn-PyQt6/Gestion_De_Stock/resources.qrc/profile_white.png", QSize(), QIcon.Normal, QIcon.Off)
        icon2.addFile(u"../../Learn-PyQt6/Gestion_De_Stock/resources.qrc/profile.png", QSize(), QIcon.Normal, QIcon.On)
        self.Profil.setIcon(icon2)
        self.Profil.setCheckable(True)
        self.Profil.setChecked(False)
        self.Profil.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.Profil)

        self.Message = QPushButton(self.layoutWidget)
        self.Message.setObjectName(u"Message")
        icon3 = QIcon()
        icon3.addFile(u"../../Learn-PyQt6/Assets.qrc/messages_white.png", QSize(), QIcon.Normal, QIcon.Off)
        icon3.addFile(u"../../Learn-PyQt6/Assets.qrc/messages.png", QSize(), QIcon.Normal, QIcon.On)
        self.Message.setIcon(icon3)
        self.Message.setCheckable(True)
        self.Message.setChecked(False)
        self.Message.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.Message)

        self.Notification = QPushButton(self.layoutWidget)
        self.Notification.setObjectName(u"Notification")
        icon4 = QIcon()
        icon4.addFile(u"../../Learn-PyQt6/Gestion_De_Stock/resources.qrc/notifications_white.png", QSize(), QIcon.Normal, QIcon.Off)
        icon4.addFile(u"../../Learn-PyQt6/Gestion_De_Stock/resources.qrc/notifications.png", QSize(), QIcon.Normal, QIcon.On)
        self.Notification.setIcon(icon4)
        self.Notification.setCheckable(True)
        self.Notification.setChecked(False)
        self.Notification.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.Notification)

        self.Settings_2 = QPushButton(self.layoutWidget)
        self.Settings_2.setObjectName(u"Settings_2")
        icon5 = QIcon()
        icon5.addFile(u"../../Learn-PyQt6/Gestion_De_Stock/resources.qrc/settings_white.png", QSize(), QIcon.Normal, QIcon.Off)
        icon5.addFile(u"../../Learn-PyQt6/Gestion_De_Stock/resources.qrc/settings.png", QSize(), QIcon.Normal, QIcon.On)
        self.Settings_2.setIcon(icon5)
        self.Settings_2.setCheckable(True)
        self.Settings_2.setChecked(False)
        self.Settings_2.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.Settings_2)


        self.gridLayout.addWidget(self.icon_only_widget, 0, 0, 1, 1)

        self.main_menu = QWidget(self.centralwidget)
        self.main_menu.setObjectName(u"main_menu")
        self.verticalLayout_3 = QVBoxLayout(self.main_menu)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.widget = QWidget(self.main_menu)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton_13 = QPushButton(self.widget)
        self.pushButton_13.setObjectName(u"pushButton_13")
        self.pushButton_13.setStyleSheet(u"border:none;")
        icon6 = QIcon()
        icon6.addFile(u"../../Learn-PyQt6/Gestion_De_Stock/resources.qrc/menu.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_13.setIcon(icon6)
        self.pushButton_13.setIconSize(QSize(20, 20))
        self.pushButton_13.setCheckable(True)
        self.pushButton_13.setChecked(False)
        self.pushButton_13.setAutoRepeat(False)
        self.pushButton_13.setAutoExclusive(False)

        self.horizontalLayout.addWidget(self.pushButton_13)

        self.lineEdit = QLineEdit(self.widget)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout.addWidget(self.lineEdit)

        self.pushButton_15 = QPushButton(self.widget)
        self.pushButton_15.setObjectName(u"pushButton_15")
        self.pushButton_15.setStyleSheet(u"border:none;")
        icon7 = QIcon()
        icon7.addFile(u"../../Learn-PyQt6/Gestion_De_Stock/resources.qrc/search.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_15.setIcon(icon7)
        self.pushButton_15.setCheckable(True)
        self.pushButton_15.setAutoExclusive(True)

        self.horizontalLayout.addWidget(self.pushButton_15)

        self.pushButton_14 = QPushButton(self.widget)
        self.pushButton_14.setObjectName(u"pushButton_14")
        self.pushButton_14.setStyleSheet(u"border:none;")
        icon8 = QIcon()
        icon8.addFile(u"../../Learn-PyQt6/Gestion_De_Stock/resources.qrc/image.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_14.setIcon(icon8)
        self.pushButton_14.setCheckable(True)
        self.pushButton_14.setAutoExclusive(True)

        self.horizontalLayout.addWidget(self.pushButton_14)


        self.verticalLayout_3.addWidget(self.widget)

        self.stackedWidget = QStackedWidget(self.main_menu)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.Dashbord_page = QWidget()
        self.Dashbord_page.setObjectName(u"Dashbord_page")
        self.label_4 = QLabel(self.Dashbord_page)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(320, 190, 211, 71))
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.stackedWidget.addWidget(self.Dashbord_page)
        self.Profile_page = QWidget()
        self.Profile_page.setObjectName(u"Profile_page")
        self.label_5 = QLabel(self.Profile_page)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(290, 220, 211, 71))
        self.label_5.setFont(font)
        self.label_5.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.stackedWidget.addWidget(self.Profile_page)
        self.essages_page = QWidget()
        self.essages_page.setObjectName(u"essages_page")
        self.label_6 = QLabel(self.essages_page)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(300, 220, 211, 71))
        self.label_6.setFont(font)
        self.label_6.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.stackedWidget.addWidget(self.essages_page)
        self.Notifications_page = QWidget()
        self.Notifications_page.setObjectName(u"Notifications_page")
        self.label_7 = QLabel(self.Notifications_page)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(320, 220, 241, 71))
        self.label_7.setFont(font)
        self.label_7.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.stackedWidget.addWidget(self.Notifications_page)
        self.Settings_Page = QWidget()
        self.Settings_Page.setObjectName(u"Settings_Page")
        self.label_8 = QLabel(self.Settings_Page)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(300, 220, 181, 71))
        self.label_8.setFont(font)
        self.label_8.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.stackedWidget.addWidget(self.Settings_Page)

        self.verticalLayout_3.addWidget(self.stackedWidget)


        self.gridLayout.addWidget(self.main_menu, 0, 3, 1, 1)

        self.icon_name_widget = QWidget(self.centralwidget)
        self.icon_name_widget.setObjectName(u"icon_name_widget")
        self.icon_name_widget.setMinimumSize(QSize(241, 791))
        self.icon_name_widget.setStyleSheet(u"\n"
"QWidget{\n"
"	background-color:#1F95EF;\n"
"}\n"
"\n"
"QPushButton{\n"
"	color:White ;\n"
"   text-align:left; \n"
"   height:30px;\n"
"   border:none;	\n"
"	padding-left:10px;\n"
"	border-top-left-radius:10px;\n"
"	border-bottom-left-radius:10px;	\n"
"\n"
"}\n"
"QPushButton:checked{\n"
"	background-color:#F5FAFE;\n"
"	color:#1F95EF;\n"
"	font-weight:bold;\n"
"}")
        self.pushButton_12 = QPushButton(self.icon_name_widget)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setGeometry(QRect(50, 710, 89, 26))
        self.pushButton_12.setCheckable(True)
        self.pushButton_12.setChecked(False)
        self.layoutWidget1 = QWidget(self.icon_name_widget)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(20, 20, 171, 42))
        self.horizontalLayout_2 = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setSpacing(7)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.layoutWidget1)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setEnabled(True)
        self.label_2.setMaximumSize(QSize(40, 40))
        self.label_2.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.label_2.setPixmap(QPixmap(u"../../Learn-PyQt6/Gestion_De_Stock/resources.qrc/profile_pic.png"))
        self.label_2.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.label_3 = QLabel(self.layoutWidget1)
        self.label_3.setObjectName(u"label_3")
        font1 = QFont()
        font1.setPointSize(18)
        font1.setBold(True)
        font1.setItalic(False)
        font1.setStrikeOut(False)
        font1.setKerning(True)
        self.label_3.setFont(font1)
        self.label_3.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_2.addWidget(self.label_3)

        self.layoutWidget2 = QWidget(self.icon_name_widget)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(20, 100, 221, 221))
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_2.setSpacing(15)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.Dashbord = QPushButton(self.layoutWidget2)
        self.Dashbord.setObjectName(u"Dashbord")
        self.Dashbord.setStyleSheet(u"\n"
"\n"
"QPushButton:checked{\n"
"	background-color:#F5FAFE;\n"
"	color:#1F95EF;\n"
"	font-weight:bold;\n"
"}")
        icon9 = QIcon()
        icon9.addFile(u"../../Learn-PyQt6/Assets.qrc/dashboard_white.png", QSize(), QIcon.Normal, QIcon.Off)
        icon9.addFile(u"../../Learn-PyQt6/Assets.qrc/dashboard.png", QSize(), QIcon.Normal, QIcon.On)
        self.Dashbord.setIcon(icon9)
        self.Dashbord.setIconSize(QSize(16, 16))
        self.Dashbord.setCheckable(True)
        self.Dashbord.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.Dashbord)

        self.Profile = QPushButton(self.layoutWidget2)
        self.Profile.setObjectName(u"Profile")
        self.Profile.setIcon(icon2)
        self.Profile.setCheckable(True)
        self.Profile.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.Profile)

        self.Messages = QPushButton(self.layoutWidget2)
        self.Messages.setObjectName(u"Messages")
        icon10 = QIcon()
        icon10.addFile(u"../../Learn-PyQt6/Gestion_De_Stock/resources.qrc/messages_white.png", QSize(), QIcon.Normal, QIcon.Off)
        icon10.addFile(u"../../Learn-PyQt6/Gestion_De_Stock/resources.qrc/messages.png", QSize(), QIcon.Normal, QIcon.On)
        self.Messages.setIcon(icon10)
        self.Messages.setCheckable(True)
        self.Messages.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.Messages)

        self.Notifications = QPushButton(self.layoutWidget2)
        self.Notifications.setObjectName(u"Notifications")
        self.Notifications.setIcon(icon4)
        self.Notifications.setCheckable(True)
        self.Notifications.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.Notifications)

        self.Settings = QPushButton(self.layoutWidget2)
        self.Settings.setObjectName(u"Settings")
        self.Settings.setIcon(icon5)
        self.Settings.setCheckable(True)
        self.Settings.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.Settings)


        self.gridLayout.addWidget(self.icon_name_widget, 0, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton_13.toggled.connect(self.icon_only_widget.setHidden)
        self.pushButton_13.toggled.connect(self.icon_name_widget.setVisible)
        self.Settings_2.toggled.connect(self.Settings.setChecked)
        self.Notification.toggled.connect(self.Notifications.setChecked)
        self.Message.toggled.connect(self.Messages.setChecked)
        self.Profil.toggled.connect(self.Profile.setChecked)
        self.Dashbor.toggled.connect(self.Dashbord.setChecked)
        self.Settings.toggled.connect(self.Settings_2.setChecked)
        self.Notifications.toggled.connect(self.Notification.setChecked)
        self.Messages.toggled.connect(self.Message.setChecked)
        self.Profile.toggled.connect(self.Profil.setChecked)
        self.Dashbord.toggled.connect(self.Dashbor.setChecked)
        self.pushButton_6.toggled.connect(MainWindow.close)
        self.pushButton_12.toggled.connect(MainWindow.close)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText("")
        self.pushButton_6.setText("")
        self.Dashbor.setText("")
        self.Profil.setText("")
        self.Message.setText("")
        self.Notification.setText("")
        self.Settings_2.setText("")
        self.pushButton_13.setText("")
        self.pushButton_15.setText("")
        self.pushButton_14.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Dashbord Page", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Profile Page", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Messages Page", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Notifications Page", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Settings Page", None))
        self.pushButton_12.setText(QCoreApplication.translate("MainWindow", u"Sign Out", None))
        self.label_2.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Side Bar", None))
        self.Dashbord.setText(QCoreApplication.translate("MainWindow", u"  Dashbord", None))
        self.Profile.setText(QCoreApplication.translate("MainWindow", u"  Profile", None))
        self.Messages.setText(QCoreApplication.translate("MainWindow", u"  Messages", None))
        self.Notifications.setText(QCoreApplication.translate("MainWindow", u" Notifications", None))
        self.Settings.setText(QCoreApplication.translate("MainWindow", u"  Settings", None))
    # retranslateUi

