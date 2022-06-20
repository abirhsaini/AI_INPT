#!/usr/bin/env python
# coding: utf-8

# In[1]:
# In[2]:
# In[3]:


import os
import glob as glob
from tqdm import tqdm


# In[4]:


get_ipython().system('pip install PyYAML>=5.3.1')


# In[1]:


get_ipython().system('python C:/Users/pc/Desktop/inpt/pfa/AI_INPT/AI_INPT/detect.py --weights C:/Users/pc/Desktop/inpt/pfa/AI_INPT/AI_INPT/best.pt --source C:/Users/pc/Desktop/inpt/pfa/AI_INPT/AI_INPT/106.png --save-txt --save-conf --conf 0.40')


# In[6]:



# In[7]:


import utils
display = utils.notebook_init()
display.Image(filename='runs/detect/exp/106.jpg', width=600)


# In[1]:


from cProfile import label
from PyQt5 import QtWidgets, QtCore, QtGui , uic
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
import shutil
from interface1 import Ui
from interface0 import Ui_MainWindow
from interface2 import Ui_MainWindow2
from petitWindow import AnotherWindow
import sys
import os
import utils
from fpdf import FPDF



##from abc1 import Ui_MainWindow2 as aaa


    

def opencal():
        
        
        dateselected = interface1.ui.calendarWidget.selectedDate()
        date_in_string = str(dateselected.toPyDate())
        
        print(date_in_string)
        
        interface1.line1.setText(date_in_string)


def navigate_1ere_interface():
    msg=QtWidgets.QMessageBox(None)
    msg.setWindowIcon(QIcon("C:/Users/pc/Desktop/inpt/pfa/PFA1/PFA/PFA3.png"))
    msg.setWindowTitle("alerte")

    if (interface1.line.text()=="") or (interface1.lineP.text()=="")  :
        msg.setText("veuiller entrer le nom du patient ")
        msg.show()
        msg.raise_()
        msg.exec_()
        
       
    else :
        widget.setCurrentIndex(widget.currentIndex()+1)
        interface2.line.setText(interface1.line.text())
        interface2.lineP.setText(interface1.lineP.text())

        interface2.line1.setText(interface1.line1.text())
        interface2.line2.setText(interface1.line2.text())  

def navigate_2eme_interface():
    msg=QtWidgets.QMessageBox(None)
    msg.setWindowIcon(QIcon("C:/Users/pc/Desktop/inpt/pfa/PFA1/PFA/PFA3.png"))
    msg.setWindowTitle("alerte")
    if (interface1.line.text()=="")or (interface1.lineP.text()=="")   :
        msg.setText("veuiller entrer le nom du patient ")
        msg.show()
        msg.raise_()
        msg.exec_()
        
        
    else:
        QApplication.setOverrideCursor(Qt.WaitCursor)

        interface3.line.setText(interface2.line.text())
        interface3.linep.setText(interface2.lineP.text())

        interface3.line1.setText(interface2.line1.text())
        interface3.line4.setText(interface2.line2.text())
        date=   interface3.line1.text().replace("/","-")
        name= interface3.line.text()+interface3.linep.text()+date
        source=interface2.imagePath
        path="C:/Users/pc/Desktop/inpt/pfa/AI_INPT2/AI_INPT/runs/detect/"+name

        sourceName=os.path.basename(source)
        if (os.path.isdir(path)):
            shutil.rmtree(path)
        get_ipython().system('python C:/Users/pc/Desktop/inpt/pfa/AI_INPT2/AI_INPT/detect.py --weights C:/Users/pc/Desktop/inpt/pfa/AI_INPT2/AI_INPT/best.pt --source $source  --name $name --save-txt  --save-conf --conf 0.40')
        widget.setCurrentIndex(widget.currentIndex()+1)
        print("C:/Users/pc/Desktop/inpt/pfa/AI_INPT2/AI_INPT/runs/detect/"+name+"/"+sourceName)
        interface3.photo1.setPixmap(QPixmap("C:/Users/pc/Desktop/inpt/pfa/AI_INPT2/AI_INPT/runs/detect/"+name+"/"+sourceName).scaled(315,300))
        interface3.photo2.setPixmap(QPixmap(source).scaled(315,300))

        ui2.label_13.setPixmap(QPixmap("C:/Users/pc/Desktop/inpt/pfa/AI_INPT2/AI_INPT/runs/detect/"+name+"/"+sourceName).scaled(131, 101))
        widget.setCurrentIndex(widget.currentIndex()+1)
        QApplication.restoreOverrideCursor()

         

def Navigate1():
    widget.setCurrentIndex(widget.currentIndex()-1)
    interface1.line.setText(interface2.line.text())
    interface1.line1.setText(interface2.line1.text())
    interface1.line2.setText(interface2.line2.text())
    interface2.line.setText(interface3.line.text())
    interface2.line1.setText(interface3.line1.text())
    interface2.line2.setText(interface3.line4.text())

def show_new_window():
    date=   interface3.line1.text().replace("/","-")
    name= interface3.line.text()+interface3.linep.text()+date
    source=interface2.imagePath
    sourceName=os.path.basename(source)

    ui2.label_11.setPixmap(QPixmap("C:/Users/pc/Desktop/inpt/pfa/AI_INPT2/AI_INPT/runs/detect/"+name+"/"+sourceName).scaled(315,300))
    ui2.show()    
    
    

def Valider(self):
    interface3.titre1.show()    
        



def enregistrer():

        date=   interface3.line1.text().replace("/","-")
        name= interface3.line.text()+interface3.linep.text()+date
        
        source=interface2.imagePath
        sourceName=os.path.basename(source) 
        msg=QtWidgets.QMessageBox(None)
        msg.setWindowTitle("alerte")
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size = 15)
        pdf.cell(200, 10, txt ="nom et prenom: " +interface3.line.text() + " "+ interface3.linep.text(),ln = 1, align = 'C')
        pdf.cell(200, 10, txt =" date:"+interface3.line1.text(),ln = 1, align = 'C')

        pdf.cell(200, 10, txt ="commentaire:"+ interface3.line4.text(),ln = 1, align = 'C')
        pdf.image("C:/Users/pc/Desktop/inpt/pfa/AI_INPT2/AI_INPT/runs/detect/"+name+"/"+sourceName,x=None,y=None,h=200,w=200)



        pdf.output("C:/Users/pc/Desktop/inpt/pfa/AI_INPT2/AI_INPT/runs/detect/"+name+"/Synthèser.pdf") 


        msg.setWindowIcon(QIcon("C:/Users/pc/Desktop/inpt/pfa/PFA1/PFA/PFA3.png"))
        try:
            
            
            fichier = open("C:/Users/pc/Desktop/inpt/pfa/AI_INPT2/AI_INPT/runs/detect/"+name+"/Synthèse.txt", "a+")
            fichier.write("nom: "+ interface3.line.text() +" "+interface3.linep.text()+"\n"+"date: "+ interface3.line1.text() + "\n"+ "commentaire: " +interface3.line4.text())
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


    

    


app=QApplication(sys.argv)
Window=QtWidgets.QMainWindow()
widget=QtWidgets.QStackedWidget()
widget.setWindowIcon(QtGui.QIcon("PFA2.png"))
widget.setWindowTitle("PFA")
widget.setStyleSheet("background-color: #FFFFFF")


interface1=Ui_MainWindow()
interface1.setupUi(Window)
interface1.valider.clicked.connect(navigate_1ere_interface)
interface1.cal1.clicked.connect(opencal)


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
widget.resize(1500,750)
widget.show()
sys.exit(app.exec_())


# 

# In[ ]:




