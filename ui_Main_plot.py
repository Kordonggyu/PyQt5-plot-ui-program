# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Main_plot.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QCheckBox, QDoubleSpinBox,
    QFrame, QGridLayout, QHBoxLayout, QHeaderView,
    QLabel, QLayout, QLineEdit, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QSlider, QSpacerItem, QSplitter, QStackedWidget,
    QStatusBar, QTabWidget, QTreeWidget, QTreeWidgetItem,
    QVBoxLayout, QWidget)
import Main_resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1066, 808)
        icon = QIcon()
        icon.addFile(u":/icons/icons/free-icon-line-chart-179121.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        self.actionHide = QAction(MainWindow)
        self.actionHide.setObjectName(u"actionHide")
        self.actionDelete_All = QAction(MainWindow)
        self.actionDelete_All.setObjectName(u"actionDelete_All")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_10 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.splitter = QSplitter(self.centralwidget)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setMinimumSize(QSize(0, 0))
        self.splitter.setMaximumSize(QSize(16777215, 16777215))
        self.splitter.setOrientation(Qt.Horizontal)
        self.splitter.setHandleWidth(1)
        self.splitter.setChildrenCollapsible(False)
        self.verticalFrame = QFrame(self.splitter)
        self.verticalFrame.setObjectName(u"verticalFrame")
        self.verticalFrame.setFrameShape(QFrame.Box)
        self.verticalLayout = QVBoxLayout(self.verticalFrame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalWidget_4 = QWidget(self.verticalFrame)
        self.horizontalWidget_4.setObjectName(u"horizontalWidget_4")
        self.horizontalWidget_4.setMinimumSize(QSize(0, 28))
        self.horizontalWidget_4.setMaximumSize(QSize(16777215, 28))
        self.horizontalLayout_4 = QHBoxLayout(self.horizontalWidget_4)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label = QLabel(self.horizontalWidget_4)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 16))
        self.label.setMaximumSize(QSize(16777215, 16))
        self.label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.label)

        self.Hide_Show_btn = QPushButton(self.horizontalWidget_4)
        self.Hide_Show_btn.setObjectName(u"Hide_Show_btn")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Hide_Show_btn.sizePolicy().hasHeightForWidth())
        self.Hide_Show_btn.setSizePolicy(sizePolicy)
        self.Hide_Show_btn.setMinimumSize(QSize(18, 18))
        self.Hide_Show_btn.setMaximumSize(QSize(18, 18))
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/substract.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Hide_Show_btn.setIcon(icon1)
        self.Hide_Show_btn.setFlat(True)

        self.horizontalLayout_4.addWidget(self.Hide_Show_btn)


        self.verticalLayout.addWidget(self.horizontalWidget_4)

        self.Data_load = QFrame(self.verticalFrame)
        self.Data_load.setObjectName(u"Data_load")
        self.Data_Load = QVBoxLayout(self.Data_load)
        self.Data_Load.setObjectName(u"Data_Load")
        self.horizontalWidget_3 = QWidget(self.Data_load)
        self.horizontalWidget_3.setObjectName(u"horizontalWidget_3")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.horizontalWidget_3.sizePolicy().hasHeightForWidth())
        self.horizontalWidget_3.setSizePolicy(sizePolicy1)
        self.horizontalWidget_3.setMinimumSize(QSize(0, 30))
        self.horizontalWidget_3.setMaximumSize(QSize(16777215, 30))
        self.horizontalLayout_3 = QHBoxLayout(self.horizontalWidget_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_2 = QLabel(self.horizontalWidget_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(0, 16))
        self.label_2.setMaximumSize(QSize(16777215, 16))

        self.horizontalLayout_3.addWidget(self.label_2)

        self.OpenFile_btn = QPushButton(self.horizontalWidget_3)
        self.OpenFile_btn.setObjectName(u"OpenFile_btn")
        self.OpenFile_btn.setMinimumSize(QSize(20, 20))
        self.OpenFile_btn.setMaximumSize(QSize(20, 20))
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/free-icon-folder-149334.png", QSize(), QIcon.Normal, QIcon.Off)
        self.OpenFile_btn.setIcon(icon2)
        self.OpenFile_btn.setFlat(True)

        self.horizontalLayout_3.addWidget(self.OpenFile_btn)


        self.Data_Load.addWidget(self.horizontalWidget_3)

        self.horizontalWidget = QWidget(self.Data_load)
        self.horizontalWidget.setObjectName(u"horizontalWidget")
        sizePolicy1.setHeightForWidth(self.horizontalWidget.sizePolicy().hasHeightForWidth())
        self.horizontalWidget.setSizePolicy(sizePolicy1)
        self.horizontalWidget.setMinimumSize(QSize(0, 30))
        self.horizontalWidget.setMaximumSize(QSize(16777215, 30))
        self.horizontalLayout_5 = QHBoxLayout(self.horizontalWidget)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_4 = QLabel(self.horizontalWidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(0, 16))
        self.label_4.setMaximumSize(QSize(16777215, 16))

        self.horizontalLayout_5.addWidget(self.label_4)

        self.pushButton_9 = QPushButton(self.horizontalWidget)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setMinimumSize(QSize(20, 20))
        self.pushButton_9.setMaximumSize(QSize(20, 20))
        self.pushButton_9.setIcon(icon2)
        self.pushButton_9.setFlat(True)

        self.horizontalLayout_5.addWidget(self.pushButton_9)


        self.Data_Load.addWidget(self.horizontalWidget)


        self.verticalLayout.addWidget(self.Data_load)

        self.horizontalWidget_2 = QWidget(self.verticalFrame)
        self.horizontalWidget_2.setObjectName(u"horizontalWidget_2")
        self.horizontalWidget_2.setMinimumSize(QSize(0, 40))
        self.horizontalWidget_2.setMaximumSize(QSize(16777215, 40))
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalWidget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pushButton_3 = QPushButton(self.horizontalWidget_2)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(30, 30))
        self.pushButton_3.setMaximumSize(QSize(30, 30))
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/free-icon-garbage-149343.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_3.setIcon(icon3)
        self.pushButton_3.setFlat(True)

        self.horizontalLayout_2.addWidget(self.pushButton_3)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.checkBox = QCheckBox(self.horizontalWidget_2)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setMinimumSize(QSize(80, 30))
        self.checkBox.setMaximumSize(QSize(80, 30))

        self.horizontalLayout_2.addWidget(self.checkBox)


        self.verticalLayout.addWidget(self.horizontalWidget_2)

        self.horizontalWidget1 = QWidget(self.verticalFrame)
        self.horizontalWidget1.setObjectName(u"horizontalWidget1")
        self.horizontalWidget1.setMinimumSize(QSize(0, 30))
        self.horizontalWidget1.setMaximumSize(QSize(16777215, 30))
        self.horizontalLayout = QHBoxLayout(self.horizontalWidget1)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_3 = QLabel(self.horizontalWidget1)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(100, 25))
        self.label_3.setMaximumSize(QSize(100, 25))
        self.label_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label_3)


        self.verticalLayout.addWidget(self.horizontalWidget1)

        self.Treelayout = QVBoxLayout()
        self.Treelayout.setObjectName(u"Treelayout")
        self.listwidget_01 = QTreeWidget(self.verticalFrame)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setText(0, u"1");
        self.listwidget_01.setHeaderItem(__qtreewidgetitem)
        self.listwidget_01.setObjectName(u"listwidget_01")
        self.listwidget_01.setDragDropMode(QAbstractItemView.DragOnly)
        self.listwidget_01.header().setVisible(False)

        self.Treelayout.addWidget(self.listwidget_01)


        self.verticalLayout.addLayout(self.Treelayout)

        self.splitter.addWidget(self.verticalFrame)
        self.verticalFrame_2 = QFrame(self.splitter)
        self.verticalFrame_2.setObjectName(u"verticalFrame_2")
        self.verticalFrame_2.setFrameShape(QFrame.Box)
        self.verticalLayout_3 = QVBoxLayout(self.verticalFrame_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.stackedWidget = QStackedWidget(self.verticalFrame_2)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.verticalLayout_6 = QVBoxLayout(self.page)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalWidget_7 = QWidget(self.page)
        self.horizontalWidget_7.setObjectName(u"horizontalWidget_7")
        self.horizontalWidget_7.setMinimumSize(QSize(0, 35))
        self.horizontalWidget_7.setMaximumSize(QSize(16777215, 35))
        self.horizontalLayout_7 = QHBoxLayout(self.horizontalWidget_7)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.spacer = QWidget(self.horizontalWidget_7)
        self.spacer.setObjectName(u"spacer")
        self.spacer.setMinimumSize(QSize(40, 0))

        self.horizontalLayout_7.addWidget(self.spacer)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_2)

        self.splitVer_btn = QPushButton(self.horizontalWidget_7)
        self.splitVer_btn.setObjectName(u"splitVer_btn")
        self.splitVer_btn.setMinimumSize(QSize(20, 20))
        self.splitVer_btn.setMaximumSize(QSize(20, 20))
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/split (1).png", QSize(), QIcon.Normal, QIcon.Off)
        self.splitVer_btn.setIcon(icon4)
        self.splitVer_btn.setFlat(True)

        self.horizontalLayout_7.addWidget(self.splitVer_btn)

        self.splitHor_btn = QPushButton(self.horizontalWidget_7)
        self.splitHor_btn.setObjectName(u"splitHor_btn")
        self.splitHor_btn.setMinimumSize(QSize(20, 20))
        self.splitHor_btn.setMaximumSize(QSize(20, 20))
        icon5 = QIcon()
        icon5.addFile(u":/icons/icons/split2.png", QSize(), QIcon.Normal, QIcon.Off)
        self.splitHor_btn.setIcon(icon5)
        self.splitHor_btn.setFlat(True)

        self.horizontalLayout_7.addWidget(self.splitHor_btn)


        self.verticalLayout_5.addWidget(self.horizontalWidget_7)

        self.tab_layout = QHBoxLayout()
        self.tab_layout.setObjectName(u"tab_layout")
        self.tabWidget = QTabWidget(self.page)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setTabsClosable(True)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_2 = QVBoxLayout(self.tab)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.graphlayout = QGridLayout()
        self.graphlayout.setObjectName(u"graphlayout")
        self.graphlayout.setSizeConstraint(QLayout.SetDefaultConstraint)

        self.verticalLayout_2.addLayout(self.graphlayout)

        self.tabWidget.addTab(self.tab, "")

        self.tab_layout.addWidget(self.tabWidget)


        self.verticalLayout_5.addLayout(self.tab_layout)

        self.horizontalWidget_8 = QWidget(self.page)
        self.horizontalWidget_8.setObjectName(u"horizontalWidget_8")
        self.horizontalWidget_8.setMinimumSize(QSize(0, 50))
        self.horizontalWidget_8.setMaximumSize(QSize(16777215, 50))
        self.horizontalLayout_6 = QHBoxLayout(self.horizontalWidget_8)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.displayTime = QLineEdit(self.horizontalWidget_8)
        self.displayTime.setObjectName(u"displayTime")
        sizePolicy2 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.displayTime.sizePolicy().hasHeightForWidth())
        self.displayTime.setSizePolicy(sizePolicy2)
        self.displayTime.setMinimumSize(QSize(80, 30))
        self.displayTime.setMaximumSize(QSize(200, 30))
        font = QFont()
        font.setPointSize(11)
        self.displayTime.setFont(font)
        self.displayTime.setAlignment(Qt.AlignCenter)
        self.displayTime.setReadOnly(True)

        self.horizontalLayout_6.addWidget(self.displayTime)

        self.pushButton_7 = QPushButton(self.horizontalWidget_8)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setMinimumSize(QSize(30, 30))
        self.pushButton_7.setMaximumSize(QSize(30, 30))
        icon6 = QIcon()
        icon6.addFile(u":/icons/icons/free-icon-repeat-134180.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_7.setIcon(icon6)
        self.pushButton_7.setFlat(True)

        self.horizontalLayout_6.addWidget(self.pushButton_7)

        self.plotplay_btn = QPushButton(self.horizontalWidget_8)
        self.plotplay_btn.setObjectName(u"plotplay_btn")
        self.plotplay_btn.setMinimumSize(QSize(30, 30))
        self.plotplay_btn.setMaximumSize(QSize(30, 30))
        icon7 = QIcon()
        icon7.addFile(u":/icons/icons/free-icon-play-button-134186.png", QSize(), QIcon.Normal, QIcon.Off)
        self.plotplay_btn.setIcon(icon7)
        self.plotplay_btn.setFlat(True)

        self.horizontalLayout_6.addWidget(self.plotplay_btn)

        self.horizontalSlider = QSlider(self.horizontalWidget_8)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.horizontalSlider.sizePolicy().hasHeightForWidth())
        self.horizontalSlider.setSizePolicy(sizePolicy3)
        self.horizontalSlider.setMinimumSize(QSize(0, 30))
        self.horizontalSlider.setMaximumSize(QSize(16777215, 30))
        self.horizontalSlider.setOrientation(Qt.Horizontal)

        self.horizontalLayout_6.addWidget(self.horizontalSlider)

        self.label_5 = QLabel(self.horizontalWidget_8)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(60, 35))
        self.label_5.setMaximumSize(QSize(60, 35))
        font1 = QFont()
        font1.setFamilies([u"Yu Gothic UI Semilight"])
        font1.setPointSize(9)
        self.label_5.setFont(font1)
        self.label_5.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.label_5)

        self.doubleSpinBox = QDoubleSpinBox(self.horizontalWidget_8)
        self.doubleSpinBox.setObjectName(u"doubleSpinBox")
        self.doubleSpinBox.setMinimumSize(QSize(0, 30))
        self.doubleSpinBox.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout_6.addWidget(self.doubleSpinBox)


        self.verticalLayout_5.addWidget(self.horizontalWidget_8)


        self.verticalLayout_6.addLayout(self.verticalLayout_5)

        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.stackedWidget.addWidget(self.page_2)

        self.verticalLayout_3.addWidget(self.stackedWidget)

        self.splitter.addWidget(self.verticalFrame_2)

        self.horizontalLayout_10.addWidget(self.splitter)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1066, 26))
        self.menuApps = QMenu(self.menubar)
        self.menuApps.setObjectName(u"menuApps")
        self.menuTools = QMenu(self.menubar)
        self.menuTools.setObjectName(u"menuTools")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuApps.menuAction())
        self.menubar.addAction(self.menuTools.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuApps.addAction(self.actionExit)
        self.menuApps.addAction(self.actionDelete_All)
        self.menuApps.addSeparator()

        self.retranslateUi(MainWindow)
        self.actionExit.triggered.connect(MainWindow.slot1)
        self.Hide_Show_btn.clicked.connect(self.Data_load.hide)
        self.OpenFile_btn.clicked.connect(MainWindow.OpenFile)

        self.stackedWidget.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Project_Window", None))
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.actionHide.setText(QCoreApplication.translate("MainWindow", u"Hide", None))
        self.actionDelete_All.setText(QCoreApplication.translate("MainWindow", u"Delete All", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"File", None))
        self.Hide_Show_btn.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Data :", None))
        self.OpenFile_btn.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Recent Data :", None))
        self.pushButton_9.setText("")
        self.pushButton_3.setText("")
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"Value", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Data List", None))
        self.splitVer_btn.setText("")
        self.splitHor_btn.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Tab 1", None))
        self.pushButton_7.setText("")
        self.plotplay_btn.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Speed", None))
        self.menuApps.setTitle(QCoreApplication.translate("MainWindow", u"Apps", None))
        self.menuTools.setTitle(QCoreApplication.translate("MainWindow", u"Tools", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi

