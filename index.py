from PyQt5.QtWidgets import  QWidget, QFileDialog,QMessageBox,QMainWindow, QApplication, QAction, QTableWidget,QTableWidgetItem,QVBoxLayout, QPushButton,QHBoxLayout,QDialog
from PyQt5 import uic
import sys
import metodo as mt
from numpy import *
import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')


def tableToVector(tabla):
    vect=[]
    for j in range(tabla.columnCount()):
        vect.append(float(tabla.item(0,j).text()))
    return vect

def tableToMatrix(tabla):
    matrix=[]
    for i in range(tabla.rowCount()):
        arr=[]
        for j in range(tabla.columnCount()):
            arr.append(float(tabla.item(i,j).text()))
        matrix.append(arr)
    return matrix
def vectorToTable(vect,tabla):
    for j in range(tabla.columnCount()):
        tabla.setItem(0,j,QTableWidgetItem(str(vect[j])))
    


class inicio(QMainWindow):            
    def __init__(self):
        QMainWindow.__init__(self)
        uic.loadUi("gui.ui", self)
        self.pushButtonCalc.clicked.connect(self.calc)
        self.pushButtonGraph.clicked.connect(self.graficar)

    def calc(self):
        mv=tableToMatrix(self.tableWidgetV)
        mw=tableToMatrix(self.tableWidgetW)
        punto=tableToVector(self.tableWidgetPunto)
        resp=mt.transformacion(mv,mw,punto)
        vectorToTable(resp,self.tableWidgetRpta)

    def graficar(self):
        x = [0, 1, 1]
        y = [0, 1, 0]

        plt.plot(x, y)
        plt.show()

        
app = QApplication(sys.argv)

_ventana = inicio()
_ventana.show()
app.exec_()

