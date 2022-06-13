#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2


# In[2]:




# In[3]:


import os
import glob as glob
from tqdm import tqdm


# In[4]:




# In[1]:



# In[6]:




# In[7]:


import utils
display = utils.notebook_init()
display.Image(filename='runs/detect/exp/106.jpg', width=600)


# In[1]:



# In[1]:


from cProfile import label
from PyQt5 import QtWidgets, QtCore, QtGui , uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from interface1 import Ui
from interface0 import Ui_MainWindow
from interface2 import Ui_MainWindow2
from petitWindow import AnotherWindow
import sys
import os
import utils

##from abc1 import Ui_MainWindow2 as aaa



    
def navigate_1ere_interface():
    msg=QtWidgets.QMessageBox(None)
    msg.setWindowIcon(QIcon("C:/Users/pc/Desktop/inpt/pfa/PFA1/PFA/PFA3.png"))
    msg.setWindowTitle("alerte")

    if (interface1.line.text()=="")   :
        msg.setText("veuiller entrer le nom du patient ")
        msg.show()
        msg.raise_()
        msg.exec_()
        print(interface1.line1.date())  
       
    elif (interface1.line1.date()=="PyQt5.QtCore.QDate(2000, 1, 1)"):
        msg.setText("veuiller entrer la date ")
        msg.show()
        msg.raise_()
        msg.exec_()      
    elif (" " in interface1.line.text() ):
        msg.setText("veuiller ecrire le nom sans espace ")
        msg.show()
        msg.raise_()
        msg.exec_()  
    else :
        widget.setCurrentIndex(widget.currentIndex()+1)
        interface2.line.setText(interface1.line.text())
        interface2.line1.setDate(interface1.line1.date())
        interface2.line2.setText(interface1.line2.text())  

def navigate_2eme_interface():
    msg=QtWidgets.QMessageBox(None)
    msg.setWindowIcon(QIcon("C:/Users/pc/Desktop/inpt/pfa/PFA1/PFA/PFA3.png"))
    msg.setWindowTitle("alerte")
    if (interface1.line.text()=="")   :
        msg.setText("veuiller entrer le nom du patient ")
        msg.show()
        msg.raise_()
        msg.exec_()
        print(interface1.line1.date())
    elif (" " in interface1.line.text() ):
        msg.setText("veuiller ecrire le nom sans espace ")
        msg.show()
        msg.raise_()
        msg.exec_()       
    else:
        interface3.line.setText(interface2.line.text())
        interface3.line1.setDate(interface2.line1.date())
        interface3.line4.setText(interface2.line2.text())   
        name= interface3.line.text()+""+ str(interface3.line1.date().month())+"-"+str(interface3.line1.date().day())+"-"+str(interface3.line1.date().year())
        source=interface2.imagePath
        sourceName=os.path.basename(source)
        get_ipython().system('python C:/Users/pc/Desktop/inpt/pfa/AI_INPT2/AI_INPT/detect.py --weights C:/Users/pc/Desktop/inpt/pfa/AI_INPT2/AI_INPT/best.pt --source $source  --name $name --save-txt  --save-conf --conf 0.40')
        widget.setCurrentIndex(widget.currentIndex()+1)
        print("C:/Users/pc/Desktop/inpt/pfa/AI_INPT2/AI_INPT/runs/detect/"+name+"/"+sourceName)
        interface3.photo1.setPixmap(QPixmap("C:/Users/pc/Desktop/inpt/pfa/AI_INPT2/AI_INPT/runs/detect/"+name+"/"+sourceName).scaled(315,300))
        interface3.photo2.setPixmap(QPixmap(source).scaled(315,300))

        ui2.label_13.setPixmap(QPixmap("C:/Users/pc/Desktop/inpt/pfa/AI_INPT2/AI_INPT/runs/detect/"+name+"/"+sourceName).scaled(131, 101))
        widget.setCurrentIndex(widget.currentIndex()+1)
         


def show_new_window():
    name= interface3.line.text()+""+ str(interface3.line1.date().month())+"-"+str(interface3.line1.date().day())+"-"+str(interface3.line1.date().year())
    source=interface2.imagePath
    sourceName=os.path.basename(source)

    ui2.label_11.setPixmap(QPixmap("C:/Users/pc/Desktop/inpt/pfa/AI_INPT2/AI_INPT/runs/detect/"+name+"/"+sourceName).scaled(315,300))
    ui2.show()    
    
    

def Valider(self):
    interface3.titre1.show()    
        

def detection() :
    name= interface3.line.text()+""+ str(interface3.line1.date().month())+"-"+str(interface3.line1.date().day())+"-"+str(interface3.line1.date().year())
    source=interface2.imagePath
    sourceName=os.path.basename(source)
    get_ipython().system('python C:/Users/pc/Desktop/inpt/pfa/AI_INPT2/AI_INPT/detect.py --weights C:/Users/pc/Desktop/inpt/pfa/AI_INPT2/AI_INPT/best.pt --source $source  --name $name --save-txt  --save-conf --conf 0.40')
    widget.setCurrentIndex(widget.currentIndex()+1)
    print("C:/Users/pc/Desktop/inpt/pfa/AI_INPT2/AI_INPT/runs/detect/"+name+"/"+sourceName)
    interface3.photo1.setPixmap(QPixmap("C:/Users/pc/Desktop/inpt/pfa/AI_INPT2/AI_INPT/runs/detect/"+name+"/"+sourceName).scaled(315,300))
    interface3.photo2.setPixmap(QPixmap(source).scaled(315,300))

    ui2.label_13.setPixmap(QPixmap("C:/Users/pc/Desktop/inpt/pfa/AI_INPT2/AI_INPT/runs/detect/"+name+"/"+sourceName).scaled(131, 101))



def enregistrer():
    
        name= interface3.line.text()+""+ str(interface3.line1.date().month())+"-"+str(interface3.line1.date().day())+"-"+str(interface3.line1.date().year())
        msg=QtWidgets.QMessageBox(None)
        msg.setWindowTitle("alerte")

        msg.setWindowIcon(QIcon("C:/Users/pc/Desktop/inpt/pfa/PFA1/PFA/PFA3.png"))
        try:
            
            
            fichier = open("C:/Users/pc/Desktop/inpt/pfa/AI_INPT2/AI_INPT/runs/detect/"+name+"/Synthèse.txt", "a+")
            fichier.write("nom: "+ interface3.line.text()+"\n"+"date: "+ interface3.line1.text() + "\n"+ "commentaire: " +interface3.line4.text())
            fichier.close()
            msg.setText(" les informations sont enregistrés")
            msg.show()
            
            msg.raise_()
            msg.exec_() 
        except:
            
            msg.setText("veuillez ressayer")
            msg.show()
            msg.raise_()
            msg.exec_() 


    
def Navigate1():
    widget.setCurrentIndex(widget.currentIndex()-1)
    interface1.line.setText(interface2.line.text())
    interface1.line1.setDate(interface2.line1.date())
    interface1.line2.setText(interface2.line2.text())
    interface2.line.setText(interface3.line.text())
    interface2.line1.setDate(interface3.line1.date())
    interface2.line2.setText(interface3.line4.text())
    
    


app=QApplication(sys.argv)
Window=QtWidgets.QMainWindow()
widget=QtWidgets.QStackedWidget()
widget.setWindowIcon(QtGui.QIcon("PFA2.png"))
widget.setWindowTitle("PFA")
widget.setStyleSheet("background-color: #FFFFFF")

interface1=Ui_MainWindow()
interface1.setupUi(Window)
interface1.valider.clicked.connect(navigate_1ere_interface)


interface2=Ui()
Window1=QtWidgets.QMainWindow()
interface2.setupUi(Window1)
interface2.photo7.clicked.connect(Navigate1)
interface2.Detection.clicked.connect(navigate_2eme_interface)



interface3=Ui_MainWindow2()
Window2=QtWidgets.QMainWindow()
interface3.setupUi(Window2)
interface3.label.clicked.connect(show_new_window)
interface3.titre1.clicked.connect(enregistrer)
interface3.photo7.clicked.connect(Navigate1)



interface3.btn5.clicked.connect(Valider)


ui2=AnotherWindow()
##sc2=aa
##sc3=aaa
widget.setWindowIcon(QIcon("C:/Users/pc/Desktop/inpt/pfa/PFA1/PFA/PFA3.png"))
widget.addWidget(Window)
widget.addWidget(Window1)
widget.addWidget(Window2)
##widget.addWidget(sc2)
##widget.addWidget(sc3)
widget.resize(1920,1080)
widget.show()
sys.exit(app.exec_())


# 

# In[ ]:




