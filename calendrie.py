# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SecondWindow(object):
  

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(511, 416)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(30, 10, 451, 321))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        
        
        
        self.calendarWidget = QtWidgets.QCalendarWidget(self.verticalLayoutWidget)

        #self.calendarWidget.selectionChanged.connect(self.calendar_date)
        self.calendarWidget.setStyleSheet("  /*Tool button styles */\n"
"QCalendarWidget QToolButton {\n"
" \n"
" \n"
"height:40px;\n"
"width:150px;\n"
"color:white;\n"
"font-size:20px;\n"
"icon-size:56px,56px;\n"
"background-color:black;\n"
" \n"
" \n"
" \n"
"}\n"
" \n"
" \n"
" \n"
"  /* header row */\n"
"QCalendarWidget  QWidget{\n"
" \n"
"alternate-background-color:rgb(128,128,128)\n"
" \n"
" \n"
" \n"
"}\n"
" \n"
" \n"
"  /*normal days */\n"
"QCalendarWidget QAbstractItemView:enabled {\n"
" \n"
" \n"
"font-size:18px;\n"
"color:rgb(180,180,180);\n"
"background-color:black;\n"
"selection-background-color:rgb(64,64,64);\n"
"selection-color:rgb(0,255,0);\n"
" \n"
" \n"
" \n"
"}")
        self.calendarWidget.setObjectName("calendarWidget")
        self.verticalLayout.addWidget(self.calendarWidget)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(100, 350, 331, 31))
        self.label.setStyleSheet("\n"
"QLabel {\n"
" \n"
"color:rgb(255, 0, 0)\n"
" \n"
" \n"
"}")
        self.label.setStyleSheet("color: rgb(255, 0, 0) ; font-size: 15px ; font-family : Inter;")
        
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 511, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def calendar_date(self):
        dateselected = self.calendarWidget.selectedDate()
        date_in_string = str(dateselected.toPyDate())
         
        self.label.setText("Date Is : " + date_in_string)        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Date Is : 2022-06-16"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
