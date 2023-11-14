# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window_updated.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QLabel,
    QLineEdit, QProgressBar, QPushButton, QRadioButton,
    QSizePolicy, QTabWidget, QWidget)
import icons_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(450, 390)
        self.BG = QFrame(Form)
        self.BG.setObjectName(u"BG")
        self.BG.setGeometry(QRect(10, 10, 430, 370))
        self.BG.setStyleSheet(u"QFrame#BG{border-radius:10px;\n"
"background-color: rgba(97, 75, 195, 255)}")
        self.BG.setFrameShape(QFrame.StyledPanel)
        self.BG.setFrameShadow(QFrame.Raised)
        self.tabWidget = QTabWidget(self.BG)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(10, 60, 410, 300))
        self.tabWidget.setStyleSheet(u"QTabWidget {\n"
"	background-color: #333333;\n"
"	border: none;\n"
"}\n"
"QTabBar::tab {\n"
"	background-color: #865DFF;\n"
"	color: #191825;\n"
"	border-top-left-radius: 10px;\n"
"	border-top-right-radius: 10px;\n"
"	padding: 8px;\n"
"}\n"
"QTabBar::tab:selected {\n"
"	background-color: #E384FF;\n"
"}\n"
"QTabWidget::pane {\n"
"	background-color: #222222;\n"
"}")
        self.Downloader = QWidget()
        self.Downloader.setObjectName(u"Downloader")
        self.frame_2 = QFrame(self.Downloader)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(0, 0, 411, 271))
        self.frame_2.setStyleSheet(u"QFrame{background-color: rgb(70, 53, 144);}")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.MainFrame = QFrame(self.frame_2)
        self.MainFrame.setObjectName(u"MainFrame")
        self.MainFrame.setGeometry(QRect(10, 60, 390, 200))
        self.MainFrame.setStyleSheet(u"QFrame{border-radius: 10px;\n"
"border-color: rgba(0, 0, 0, 0);\n"
"background-color: rgba(30, 30, 30, 150);}")
        self.MainFrame.setFrameShape(QFrame.StyledPanel)
        self.MainFrame.setFrameShadow(QFrame.Raised)
        self.video_id = QLineEdit(self.MainFrame)
        self.video_id.setObjectName(u"video_id")
        self.video_id.setGeometry(QRect(30, 10, 310, 20))
        self.video_id.setStyleSheet(u"font: 75 10pt \"MS Shell Dlg 2\";\n"
"border-radius: 10px;\n"
"border-color: rgba(0, 0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.517273, x2:1, y2:0.5625, stop:0 rgba(49, 56, 102, 255), stop:1 rgba(151, 78, 195, 255));")
        self.video_id.setAlignment(Qt.AlignCenter)
        self.audio = QRadioButton(self.MainFrame)
        self.audio.setObjectName(u"audio")
        self.audio.setGeometry(QRect(60, 170, 100, 17))
        self.audio.setStyleSheet(u"font: 75 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgba(0, 0, 0, 0);\n"
"border-color: rgba(0, 0, 0, 0);")
        self.download = QPushButton(self.MainFrame)
        self.download.setObjectName(u"download")
        self.download.setGeometry(QRect(220, 150, 80, 30))
        self.download.setStyleSheet(u"QPushButton{font: 75 10pt \"MS Shell Dlg 2\";\n"
"border-radius: 10px;\n"
"color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.511364, x2:0.966, y2:0.511364, stop:0 rgba(49, 56, 102, 255), stop:1 rgba(151, 78, 195, 255));\n"
"border-color: rgba(0, 0, 0, 0);}\n"
"\n"
"QPushButton:hover{color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);}\n"
"QPushButton:pressed{color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);}")
        self.video = QRadioButton(self.MainFrame)
        self.video.setObjectName(u"video")
        self.video.setGeometry(QRect(60, 140, 100, 17))
        self.video.setStyleSheet(u"font: 75 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgba(0, 0, 0, 0);\n"
"border-color: rgba(0, 0, 0, 0);")
        self.download_folder = QLineEdit(self.MainFrame)
        self.download_folder.setObjectName(u"download_folder")
        self.download_folder.setGeometry(QRect(30, 40, 310, 20))
        self.download_folder.setStyleSheet(u"font: 75 10pt \"MS Shell Dlg 2\";\n"
"border-radius: 10px;\n"
"border-color: rgba(0, 0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.517273, x2:1, y2:0.5625, stop:0 rgba(49, 56, 102, 255), stop:1 rgba(151, 78, 195, 255));")
        self.download_folder.setAlignment(Qt.AlignCenter)
        self.download_prog = QProgressBar(self.MainFrame)
        self.download_prog.setObjectName(u"download_prog")
        self.download_prog.setGeometry(QRect(40, 70, 290, 20))
        self.download_prog.setStyleSheet(u"QProgressBar{border-radius: 10px;\n"
"border-color: rgba(0, 0, 0, 0);\n"
"background-color: rgb(85, 0, 255);\n"
"font: 75 10pt \"MS Shell Dlg 2\";}\n"
"\n"
"QProgressBar:chunk{background-color: qlineargradient(spread:pad, x1:0, y1:0.482955, x2:1, y2:0.528409, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(43, 43, 65, 255));\n"
"border-radius: 10px;\n"
"border-color: rgba(0, 0, 0, 0);}")
        self.download_prog.setValue(24)
        self.download_prog.setAlignment(Qt.AlignCenter)
        self.download_stat = QLabel(self.MainFrame)
        self.download_stat.setObjectName(u"download_stat")
        self.download_stat.setGeometry(QRect(90, 100, 190, 20))
        self.download_stat.setStyleSheet(u"font: 75 8pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"border-color: rgba(0, 0, 0, 0);")
        self.download_stat.setAlignment(Qt.AlignCenter)
        self.MainTab = QFrame(self.frame_2)
        self.MainTab.setObjectName(u"MainTab")
        self.MainTab.setGeometry(QRect(20, 10, 370, 41))
        self.MainTab.setStyleSheet(u"QFrame{border-radius: 10px;\n"
"border-color: rgba(0, 0, 0, 0);\n"
"background-color: rgb(49, 56, 102);}")
        self.MainTab.setFrameShape(QFrame.StyledPanel)
        self.MainTab.setFrameShadow(QFrame.Raised)
        self.MainLabel = QLabel(self.MainTab)
        self.MainLabel.setObjectName(u"MainLabel")
        self.MainLabel.setGeometry(QRect(10, 10, 351, 21))
        self.MainLabel.setStyleSheet(u"font: 75 13pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"border-color: rgba(0, 0, 0, 0)")
        self.MainLabel.setAlignment(Qt.AlignCenter)
        self.tabWidget.addTab(self.Downloader, "")
        self.Finder = QWidget()
        self.Finder.setObjectName(u"Finder")
        self.frame = QFrame(self.Finder)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 411, 271))
        self.frame.setStyleSheet(u"QFrame{background-color: rgb(70, 53, 144);}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(10, 60, 390, 200))
        self.frame_3.setStyleSheet(u"QFrame{border-radius: 10px;\n"
"background-color: rgba(30, 30, 30, 150);\n"
"border-color: rgba(255, 255, 255, 0);}")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.video_name = QLineEdit(self.frame_3)
        self.video_name.setObjectName(u"video_name")
        self.video_name.setGeometry(QRect(30, 10, 320, 20))
        self.video_name.setStyleSheet(u"font: 75 10pt \"MS Shell Dlg 2\";\n"
"border-radius: 10px;\n"
"border-color: rgba(0, 0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.517273, x2:1, y2:0.5625, stop:0 rgba(49, 56, 102, 255), stop:1 rgba(151, 78, 195, 255));")
        self.video_name.setAlignment(Qt.AlignCenter)
        self.result = QLabel(self.frame_3)
        self.result.setObjectName(u"result")
        self.result.setGeometry(QRect(30, 110, 60, 30))
        self.result.setStyleSheet(u"font: 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);\n"
"border-color: rgba(0, 0, 0, 0);")
        self.results = QComboBox(self.frame_3)
        self.results.setObjectName(u"results")
        self.results.setGeometry(QRect(80, 110, 270, 30))
        self.results.setStyleSheet(u"QComboBox {\n"
"	border: 2px solid rgb(227, 132, 255);\n"
"	border-radius: 8px;\n"
"	padding: 2px 20px 2px 10px;\n"
"	background-color: rgb(227, 132, 255);\n"
"}\n"
"QComboBox::drop-down {\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: right;\n"
"	width: 25px;\n"
"	border-left: 2px solid rgb(227, 132, 255);\n"
"	border-radius: 8px;\n"
"	background-color: rgb(227, 132, 255);\n"
"}\n"
"QComboBox::down-arrow {\n"
"	image: url(:/feather_dark/feather-dark/chevron-down.svg)\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"	background-color: rgb(134, 93, 255);\n"
"	border-radius: 6px;\n"
"}")
        self.copy_video_id = QPushButton(self.frame_3)
        self.copy_video_id.setObjectName(u"copy_video_id")
        self.copy_video_id.setGeometry(QRect(30, 160, 320, 30))
        self.copy_video_id.setStyleSheet(u"QPushButton{font: 75 10pt \"MS Shell Dlg 2\";\n"
"border-radius: 10px;\n"
"color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.511364, x2:0.966, y2:0.511364, stop:0 rgba(49, 56, 102, 255), stop:1 rgba(151, 78, 195, 255));\n"
"border-color: rgba(0, 0, 0, 0);}\n"
"\n"
"QPushButton:hover{color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);}\n"
"QPushButton:pressed{color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);}")
        self.search_video = QPushButton(self.frame_3)
        self.search_video.setObjectName(u"search_video")
        self.search_video.setGeometry(QRect(170, 50, 170, 30))
        self.search_video.setStyleSheet(u"QPushButton{font: 75 10pt \"MS Shell Dlg 2\";\n"
"border-radius: 10px;\n"
"color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.511364, x2:0.966, y2:0.511364, stop:0 rgba(49, 56, 102, 255), stop:1 rgba(151, 78, 195, 255));\n"
"border-color: rgba(0, 0, 0, 0);}\n"
"\n"
"QPushButton:hover{color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);}\n"
"QPushButton:pressed{color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);}")
        self.limit_2 = QLabel(self.frame_3)
        self.limit_2.setObjectName(u"limit_2")
        self.limit_2.setGeometry(QRect(30, 50, 40, 30))
        self.limit_2.setStyleSheet(u"font: 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);\n"
"border-color: rgba(0, 0, 0, 0);")
        self.limit = QLineEdit(self.frame_3)
        self.limit.setObjectName(u"limit")
        self.limit.setGeometry(QRect(70, 50, 80, 30))
        self.limit.setStyleSheet(u"font: 75 10pt \"MS Shell Dlg 2\";\n"
"border-radius: 10px;\n"
"border-color: rgba(0, 0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.517273, x2:1, y2:0.5625, stop:0 rgba(49, 56, 102, 255), stop:1 rgba(151, 78, 195, 255));")
        self.limit.setAlignment(Qt.AlignCenter)
        self.MainTab_2 = QFrame(self.frame)
        self.MainTab_2.setObjectName(u"MainTab_2")
        self.MainTab_2.setGeometry(QRect(10, 10, 389, 41))
        self.MainTab_2.setStyleSheet(u"QFrame{border-radius: 10px;\n"
"background-color: rgb(49, 56, 102);\n"
"border-color: rgba(255, 255, 255, 0);}")
        self.MainTab_2.setFrameShape(QFrame.StyledPanel)
        self.MainTab_2.setFrameShadow(QFrame.Raised)
        self.MainLabel_2 = QLabel(self.MainTab_2)
        self.MainLabel_2.setObjectName(u"MainLabel_2")
        self.MainLabel_2.setGeometry(QRect(10, 10, 360, 21))
        self.MainLabel_2.setStyleSheet(u"font: 75 13pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"border-color: rgba(0, 0, 0, 0)")
        self.MainLabel_2.setAlignment(Qt.AlignCenter)
        self.tabWidget.addTab(self.Finder, "")
        self.TitleBar = QFrame(self.BG)
        self.TitleBar.setObjectName(u"TitleBar")
        self.TitleBar.setGeometry(QRect(30, 10, 380, 40))
        self.TitleBar.setStyleSheet(u"border-radius: 10px;\n"
"background-color: rgb(49, 56, 102);")
        self.TitleBar.setFrameShape(QFrame.StyledPanel)
        self.TitleBar.setFrameShadow(QFrame.Raised)
        self.Title = QLabel(self.TitleBar)
        self.Title.setObjectName(u"Title")
        self.Title.setGeometry(QRect(30, 10, 310, 21))
        self.Title.setStyleSheet(u"font: 75 13pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.Title.setAlignment(Qt.AlignCenter)
        self.Close = QPushButton(self.TitleBar)
        self.Close.setObjectName(u"Close")
        self.Close.setGeometry(QRect(340, 10, 30, 23))
        self.Close.setStyleSheet(u"QPushButton{image: url(:/feather_pink/feather-pink/x.svg);}\n"
"QPushButton:hover{image: url(:/feather_purple/feather-purple/x.svg);}\n"
"QPushButton:pressed{image: url(:/feather_dark/feather-dark/x.svg);}")

        self.retranslateUi(Form)

        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.video_id.setText(QCoreApplication.translate("Form", u"video id | ex: ????", None))
        self.audio.setText(QCoreApplication.translate("Form", u"Audio | mp3", None))
        self.download.setText(QCoreApplication.translate("Form", u"Download", None))
        self.video.setText(QCoreApplication.translate("Form", u"Video | mp4", None))
        self.download_folder.setText(QCoreApplication.translate("Form", u"download folder | ex: C:/???", None))
        self.download_prog.setFormat(QCoreApplication.translate("Form", u"%p%", None))
        self.download_stat.setText(QCoreApplication.translate("Form", u"Status: None", None))
        self.MainLabel.setText(QCoreApplication.translate("Form", u"Downloader", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Downloader), QCoreApplication.translate("Form", u"Downloader", None))
        self.video_name.setText(QCoreApplication.translate("Form", u"Video Name", None))
        self.result.setText(QCoreApplication.translate("Form", u"Results: ", None))
        self.copy_video_id.setText(QCoreApplication.translate("Form", u"Copy Selected Result Video ID", None))
        self.search_video.setText(QCoreApplication.translate("Form", u"Search Video", None))
        self.limit_2.setText(QCoreApplication.translate("Form", u"Limit: ", None))
        self.limit.setText(QCoreApplication.translate("Form", u"1", None))
        self.MainLabel_2.setText(QCoreApplication.translate("Form", u"Finder", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Finder), QCoreApplication.translate("Form", u"Finder", None))
        self.Title.setText(QCoreApplication.translate("Form", u"<strong>Youtube</strong> Video/Audio Converter", None))
        self.Close.setText("")
    # retranslateUi

