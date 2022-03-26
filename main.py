import sys
from PyQt5 import QtWidgets
from MyMainForm import MyMainForm

if __name__ =='__main__':
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = MyMainForm()
    sys.exit(app.exec_())
