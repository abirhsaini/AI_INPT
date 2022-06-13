

from cProfile import label
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget
from PyQt5.QtWidgets import *

class AnotherWindow(QWidget):
    """
    This "window" is a QWidget. If it has no parent, it
    will appear as a free-floating window as we want.
    """
    def __init__(self):
        super().__init__()
       
        layout = QVBoxLayout()
        self.setLayout(layout)
        self.label_13 = QtWidgets.QLabel()
        self.pixmap=QtGui.QPixmap("c:/Users/pc/Desktop/inpt/pfa/Capture.PNG")
        self.smaller_pixmap = self.pixmap.scaled(131, 101)
        self.label_13.setPixmap(self.smaller_pixmap)
        self.label_13.setScaledContents(True)
        self.label_11 = QtWidgets.QLabel()
        self.pixmap1=QtGui.QPixmap("c:/Users/pc/Desktop/inpt/pfa/El_ayachi-El_kacemi--2021-07-23T12_51_35Z-eidon_20551-right-0-visible-2021-07-23T12_51_33Z-2021-12-06_083318-image.gif")
        self.smaller_pixmap1=self.pixmap1.scaled(711, 501)
        self.label_11.setPixmap(self.smaller_pixmap1)
        self.label_11.setScaledContents(True)
        
       # self.pixmap2 = self.label_13.scaledToWidth(7131)
        #self.pixmap3 = self.label_13.scaledToHeight(101)
        #layout.addWidget(self.label_13)
        layout.addWidget(self.label_11)
