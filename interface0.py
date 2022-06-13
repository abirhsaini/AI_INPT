from PyQt5 import QtWidgets, QtCore, QtGui , uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QWidget()
MainWindow.setStyleSheet("background-color: #FFFFFF")
MainWindow.setWindowIcon(QtGui.QIcon("PFA2.png"))
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setWindowTitle("PFA")
        MainWindow.resize(1500,750)
        ##MainWindow.move(400,20)
        self.titre=QtWidgets.QLabel("Abbulkassis \n DR-AI",MainWindow)
        self.titre.setStyleSheet("color: #96C0B3 ; font-size: 25px ; font-family : Inter;")
        self.titre.resize(200,100)
        self.titre.move(690,35)
        ##self.btn=QtWidgets.QPushButton(MainWindow)
        ##self.btn.setIcon(QtGui.QIcon('PFA3.png'))
        self.photo=QtWidgets.QLabel(MainWindow)
        self.photo.move(570,30)
        self.photo.resize(100,110)
        pic=QPixmap("c:/Users/pc/Desktop/inpt/pfa/PFA1/PFA/PFA3.png").scaled(90,95)
        self.photo.setPixmap(pic)
        self.label=QtWidgets.QLabel("  Nom du patient:  ",MainWindow)
        self.label.setStyleSheet('background-color: #96C0B3; color: white ; font-size:12px ; border: 2px solid #96C0B3 ; border-radius:18px ; font family: Inter;')
        self.label.move(360,190)
        self.label.resize(120,40)
        self.label1=QtWidgets.QLabel("    Date:  ",MainWindow)
        self.label1.setStyleSheet('background-color: #96C0B3; color: white ; font-size:12px ; border: 2px solid #96C0B3 ; border-radius:18px ; font family: Inter;')
        self.label1.move(360,240)
        self.label1.resize(120,40)
        self.label2=QtWidgets.QLabel("  Commentaire:  ",MainWindow)
        self.label2.setStyleSheet('background-color: #96C0B3; color: white ; font-size:12px ; border: 2px solid #96C0B3 ; border-radius:18px ; font family: Inter;')
        self.label2.move(360,290)
        self.label2.resize(120,40)
        self.line=QtWidgets.QLineEdit(MainWindow)
        self.line.move(515,190)
        self.line.resize(420,40)
        self.line.setStyleSheet("background-color: white ; font-size: 12px ; color: black; border : 2px solid #96C0B3 ; border-radius:18px")
        self.line1=QtWidgets.QDateEdit(MainWindow)
        #self.line1 =QtWidgets.QLineEdit(MainWindow)
        self.line1.move(515,240)
        self.line1.resize(420,40)
        self.line1.setStyleSheet("background-color: white ; font-size: 12px ; color: black; border : 2px solid #96C0B3 ; border-radius:18px")
        self.line2=QtWidgets.QLineEdit(MainWindow)
        self.line2.move(515,290)
        self.line2.resize(420,100)
        self.line2.setStyleSheet("background-color: white ; font-size: 12px ; color: black; border : 2px solid #96C0B3 ; border-radius:18px")
        self.valider=QtWidgets.QPushButton("  Valider  ",MainWindow)
        self.valider.move(615,400)
        self.valider.resize(120,40)
        self.valider.setStyleSheet('background-color: #96C0B3; color: white ; font-size:12px ; border: 2px solid #96C0B3 ; border-radius:18px ; font family: Inter;')
#####################################################################################################################################################################




            
if __name__=="__main__":
    
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
