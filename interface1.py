from PyQt5 import QtWidgets, QtCore, QtGui , uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QWidget()
MainWindow.setStyleSheet("background-color: #FFFFFF")
MainWindow.setWindowIcon(QtGui.QIcon("PFA2.png"))
class Ui(QWidget):
    def setupUi(self, MainWindow):
        MainWindow.setWindowTitle("PFA")
        MainWindow.resize(1500,750)
        ##MainWindow.move(400,20)
        
        
        self.titre=QtWidgets.QLabel("Abbulkassis \n DR-AI",MainWindow)
        self.titre.setStyleSheet("color: #96C0B3 ; font-size: 25px ; font-family : Inter;")
        self.titre.resize(200,100)
        self.titre.move(400,0)
        ##self.btn=QtWidgets.QPushButton(MainWindow)
        ##self.btn.setIcon(QtGui.QIcon('PFA3.png'))
        self.photo=QtWidgets.QLabel(MainWindow)
        self.photo.move(280,-5)
        self.photo.resize(100,110)
        pic=QPixmap("c:/Users/pc/Desktop/inpt/pfa/PFA1/PFA/PFA3.png").scaled(90,95)
        self.photo.setPixmap(pic)
        self.label=QtWidgets.QLabel("  Nom du patient:  ",MainWindow)
        self.label.setStyleSheet('background-color: #96C0B3; color: white ; font-size:12px ; border: 2px solid #96C0B3 ; border-radius:18px ; font family: Inter;')
        self.label.move(70,140)
        self.label.resize(120,40)
        self.label1=QtWidgets.QLabel("    Date:  ",MainWindow)
        self.label1.setStyleSheet('background-color: #96C0B3; color: white ; font-size:12px ; border: 2px solid #96C0B3 ; border-radius:18px ; font family: Inter;')
        self.label1.move(70,190)
        self.label1.resize(120,40)
        self.label2=QtWidgets.QLabel("  Commentaire:  ",MainWindow)
        self.label2.setStyleSheet('background-color: #96C0B3; color: white ; font-size:12px ; border: 2px solid #96C0B3 ; border-radius:18px ; font family: Inter;')
        self.label2.move(70,240)
        self.label2.resize(120,40)
        self.line=QtWidgets.QLineEdit(MainWindow)
        self.line.move(225,140)
        self.line.resize(420,40)
        self.line.setStyleSheet("background-color: white ; font-size: 12px ; color: black; border : 2px solid #96C0B3 ; border-radius:18px")
        self.line1=QtWidgets.QDateEdit(MainWindow)
        self.line1.move(225,190)
        self.line1.resize(420,40)
        self.line1.setStyleSheet("background-color: white ; font-size: 12px ; color: black; border : 2px solid #96C0B3 ; border-radius:18px")
        self.line2=QtWidgets.QLineEdit(MainWindow)
        self.line2.move(225,240)
        self.line2.resize(420,100)
        self.line2.setStyleSheet("background-color: white ; font-size: 12px ; color: black; border : 2px solid #96C0B3 ; border-radius:18px")
        self.valider=QtWidgets.QPushButton("  Valider  ",MainWindow)
        self.valider.move(370,350)
        self.valider.resize(120,40)
        self.valider.setStyleSheet('background-color: #96C0B3; color: white ; font-size:12px ; border: 2px solid #96C0B3 ; border-radius:18px ; font family: Inter;')
#####################################################################################################################################################################
        self.photo1=QtWidgets.QLabel(MainWindow)
        self.valider.hide()
        self.photo1.move(820,50)
        self.photo1.resize(420,420)
        ##self.photo1.setStyleSheet(" border : 2px solid # ; border-radius: 18px ")
        ##pic1=QPixmap("").scaled(415,400)
        self.photo1.setStyleSheet(" border : 2px solid #000000 ; border-radius: 18px ")
        ##self.photo1.setPixmap(pic1)
        self.Parcourir=QtWidgets.QPushButton("  Parcourir  ",MainWindow)
        self.Parcourir.move(355,430)
        self.Parcourir.resize(150,45)
        self.Parcourir.setStyleSheet('background-color: #96C0B3; color: white ; font-size:15px ; border: 2px solid #96C0B3 ; border-radius:18px ; font family: Inter;')
        self.Parcourir.clicked.connect(self.getImage)
        self.Segmentation=QtWidgets.QPushButton("  Segmentation  ",MainWindow)
        self.Segmentation.move(225,530)
        self.Segmentation.resize(150,45)
        self.Segmentation.hide()
        self.Segmentation.setStyleSheet('background-color: #96C0B3; color: white ; font-size:15px ; border: 2px solid #96C0B3 ; border-radius:18px ; font family: Inter;')
        self.Detection=QtWidgets.QPushButton("  Detection  ",MainWindow)
        self.Detection.move(495,530)
        self.Detection.resize(150,45)
        self.Detection.setStyleSheet('background-color: #96C0B3; color: white ; font-size:15px ; border: 2px solid #96C0B3 ; border-radius:18px ; font family: Inter;')
        self.Detection.hide()
        
        
        
        self.photo7 = QtWidgets.QPushButton("Back",MainWindow)
        self.photo7.move(0, 10)
        self.photo7.resize(150, 20)
        self.photo7.setStyleSheet(' border: none ;font-size:15px')
        self.photo7.setIcon(QtGui.QIcon("c:/Users/pc/Desktop/inpt/pfa/PFA1/PFA/retour.png"))


    def getImage(self):
        print("hi")
        ##_translate = QtCore.QCoreApplication.translate
        print("hi")
        fname = QFileDialog.getOpenFileName(self, 'Open file', 'C:/Users/pc/Desktop/inpt/pfa/AI_INPT2/AI_INPT', "Image files (*.jpg *.gif *.png)")
        self.imagePath = fname[0]
        self.pixmap1 = QtGui.QPixmap(self.imagePath).scaled(415,400)
        self.photo1.setPixmap(QtGui.QPixmap(self.pixmap1))
        self.photo1.setScaledContents(True)
        self.Segmentation.show()
        self.Detection.show()


if __name__=="__main__":
    
    ui = Ui()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
