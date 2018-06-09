import sys
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication,QDialog
from PyQt5.uic import loadUi

class PyUiTest(QDialog):
    def __init__(self):
        super(PyUiTest,self).__init__()
        loadUi('dialog1.ui',self)
        self.pushButton.clicked.connect(self.on_pushButton_clicked)
    @pyqtSlot()
    def on_pushButton_clicked(self):
        self.label.setText(self.lineEdit.text())

app=QApplication(sys.argv)
widget=PyUiTest()
widget.show()
sys.exit(app.exec_())
