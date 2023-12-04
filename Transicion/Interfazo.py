import os, sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(796, 600)
        Dialog.setLayoutDirection(QtCore.Qt.LeftToRight)
        Dialog.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_Superior = QtWidgets.QFrame(self.frame)
        self.frame_Superior.setMinimumSize(QtCore.QSize(0, 42))
        self.frame_Superior.setMaximumSize(QtCore.QSize(16777215, 40))
        self.frame_Superior.setStyleSheet("\n"
"background-color: rgb(0, 0, 0);")
        self.frame_Superior.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_Superior.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_Superior.setObjectName("frame_Superior")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_Superior)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Manu = QtWidgets.QLabel(self.frame_Superior)
        self.Manu.setStyleSheet("font: 87 12pt \"Arial Black \";\n"
"color: rgb(20, 200, 220);")
        self.Manu.setObjectName("Manu")
        self.horizontalLayout.addWidget(self.Manu)
        spacerItem = QtWidgets.QSpacerItem(198, 17, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.btminimizar = QtWidgets.QPushButton(self.frame_Superior)
        self.btminimizar.setMinimumSize(QtCore.QSize(40, 40))
        self.btminimizar.setMaximumSize(QtCore.QSize(40, 16777215))
        self.btminimizar.setStyleSheet("")
        self.btminimizar.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("minimizar (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btminimizar.setIcon(icon)
        self.btminimizar.setIconSize(QtCore.QSize(38, 38))
        self.btminimizar.setObjectName("btminimizar")
        self.horizontalLayout.addWidget(self.btminimizar)
        self.btmaximizar = QtWidgets.QPushButton(self.frame_Superior)
        self.btmaximizar.setMinimumSize(QtCore.QSize(40, 40))
        self.btmaximizar.setStyleSheet("")
        self.btmaximizar.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("maximizar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btmaximizar.setIcon(icon1)
        self.btmaximizar.setIconSize(QtCore.QSize(38, 38))
        self.btmaximizar.setObjectName("btmaximizar")
        self.horizontalLayout.addWidget(self.btmaximizar)
        self.btcerrar = QtWidgets.QPushButton(self.frame_Superior)
        self.btcerrar.setMinimumSize(QtCore.QSize(40, 40))
        self.btcerrar.setStyleSheet("")
        self.btcerrar.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Cierre.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btcerrar.setIcon(icon2)
        self.btcerrar.setIconSize(QtCore.QSize(38, 38))
        self.btcerrar.setObjectName("btcerrar")
        self.horizontalLayout.addWidget(self.btcerrar)
        self.verticalLayout_2.addWidget(self.frame_Superior)
        self.frame_inferior = QtWidgets.QFrame(self.frame)
        self.frame_inferior.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_inferior.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_inferior.setObjectName("frame_inferior")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_inferior)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_2 = QtWidgets.QFrame(self.frame_inferior)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.frame_3 = QtWidgets.QFrame(self.frame_2)
        self.frame_3.setMaximumSize(QtCore.QSize(300, 16777215))
        self.frame_3.setStyleSheet("QFrame{\n"
"background-color: rgb(53, 53, 79);\n"
"}\n"
"\n"
"\n"
"QPushButton{\n"
"font: 87 12pt \"Arial Black\";\n"
"background-color: #000000ff;\n"
"color: rgb(20, 200, 220);\n"
"border-radius:5px;\n"
"border:1px solid white;\n"
"\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"background-color:black;\n"
"}")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.bt1 = QtWidgets.QPushButton(self.frame_3)
        self.bt1.clicked.connect(self.boton1Clicado)
        self.bt1.setLayoutDirection(QtCore.Qt.RightToLeft)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("archivo-nuevo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bt1.setIcon(icon3)
        self.bt1.setIconSize(QtCore.QSize(32, 32))
        self.bt1.setObjectName("bt1")
        self.verticalLayout_4.addWidget(self.bt1)
        self.bt2 = QtWidgets.QPushButton(self.frame_3)
        self.bt2.setLayoutDirection(QtCore.Qt.RightToLeft)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("reciente.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bt2.setIcon(icon4)
        self.bt2.setIconSize(QtCore.QSize(32, 32))
        self.bt2.setObjectName("bt2")
        self.verticalLayout_4.addWidget(self.bt2)
        self.bt3 = QtWidgets.QPushButton(self.frame_3)
        self.bt3.setLayoutDirection(QtCore.Qt.RightToLeft)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("cambiar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bt3.setIcon(icon5)
        self.bt3.setIconSize(QtCore.QSize(32, 32))
        self.bt3.setObjectName("bt3")
        self.verticalLayout_4.addWidget(self.bt3)
        self.bt4 = QtWidgets.QPushButton(self.frame_3)
        self.bt4.setLayoutDirection(QtCore.Qt.RightToLeft)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("ajuste.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bt4.setIcon(icon6)
        self.bt4.setIconSize(QtCore.QSize(32, 32))
        self.bt4.setObjectName("bt4")
        self.verticalLayout_4.addWidget(self.bt4)
        self.horizontalLayout_3.addWidget(self.frame_3)
        self.frame_5 = QtWidgets.QFrame(self.frame_2)
        self.frame_5.setStyleSheet("QFrame{\n"
"background-color: rgb(53, 53, 79);\n"
"}\n"
"\n"
"\n"
"QPushButton{\n"
"font: 87 12pt \"Arial Black\";\n"
"background-color: #000000ff;\n"
"color: rgb(20, 200, 220);\n"
"border-radius:5px;\n"
"border:1px solid white;\n"
"\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"background-color:black;\n"
"}\n"
"")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, -1)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_6 = QtWidgets.QFrame(self.frame_5)
        self.frame_6.setStyleSheet("QFrame{\n"
"background-color: rgb(53, 53, 79);\n"
"}\n"
"\n"
"\n"
"QPushButton{\n"
"font: 87 12pt \"Arial Black\";\n"
"background-color: #000000ff;\n"
"color: rgb(20, 200, 220);\n"
"border-radius:5px;\n"
"border:1px solid #14C8DC;\n"
"\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"background-color:black;\n"
"}")
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_6)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.btmenu1 = QtWidgets.QPushButton(self.frame_6)
        self.btmenu1.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("flecha-izquierda.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btmenu1.setIcon(icon7)
        self.btmenu1.setIconSize(QtCore.QSize(32, 32))
        self.btmenu1.setObjectName("btmenu1")
        self.horizontalLayout_4.addWidget(self.btmenu1)
        self.brmenu2 = QtWidgets.QPushButton(self.frame_6)
        self.brmenu2.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("flecha-correcta.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.brmenu2.setIcon(icon8)
        self.brmenu2.setIconSize(QtCore.QSize(32, 32))
        self.brmenu2.setObjectName("brmenu2")
        self.horizontalLayout_4.addWidget(self.brmenu2)
        self.lineEdit = QtWidgets.QLineEdit(self.frame_6)
        self.lineEdit.setStyleSheet("QLineEdit{\n"
"\n"
"border:2px solid #14c8dc;\n"
"border-radius:8px;\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);\n"
"font: 75 12pt \"Times New Roman\";\n"
"\n"
"}")
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_4.addWidget(self.lineEdit)
        self.pushButton_10 = QtWidgets.QPushButton(self.frame_6)
        self.pushButton_10.setStyleSheet("QFrame{\n"
"background-color: rgb(53, 53, 79);\n"
"}\n"
"\n"
"\n"
"QPushButton{\n"
"font: 87 12pt \"Arial Black\";\n"
"background-color: #000000ff;\n"
"color: rgb(20, 200, 220);\n"
"border-radius:5px;\n"
"border:0px solid #14C8DC;\n"
"\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"background-color:black;\n"
"}")
        self.pushButton_10.setText("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("lupa.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_10.setIcon(icon9)
        self.pushButton_10.setIconSize(QtCore.QSize(32, 32))
        self.pushButton_10.setObjectName("pushButton_10")
        self.horizontalLayout_4.addWidget(self.pushButton_10)
        self.verticalLayout_3.addWidget(self.frame_6)
        self.frame_7 = QtWidgets.QFrame(self.frame_5)
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_7)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.toolBox = QtWidgets.QToolBox(self.frame_7)
        self.toolBox.setStyleSheet("QToolBox::tab{\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius: 5px;\n"
"    color: rgb(0, 0, 0);\n"
"    font: 75 8pt \"MS Shell Dig 2\";\n"
"}\n"
"\n"
"QToolBox::tab:selected{\n"
"    background-color: rgb(20, 200, 220);\n"
"    font: 75 12pt \"MS Shell Dig 2\";\n"
"    color: rgb(0, 0, 0);\n"
"\n"
"}")
        self.toolBox.setObjectName("toolBox")
        self.page = QtWidgets.QWidget()
        self.page.setGeometry(QtCore.QRect(0, 0, 257, 377))
        self.page.setObjectName("page")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.page)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.pushButton = QtWidgets.QPushButton(self.page)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_7.addWidget(self.pushButton)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("Paginas.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolBox.addItem(self.page, icon10, "")
        self.page_5 = QtWidgets.QWidget()
        self.page_5.setGeometry(QtCore.QRect(0, 0, 257, 377))
        self.page_5.setObjectName("page_5")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.page_5)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.pushButton_2 = QtWidgets.QPushButton(self.page_5)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_8.addWidget(self.pushButton_2)
        self.toolBox.addItem(self.page_5, icon10, "")
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setGeometry(QtCore.QRect(0, 0, 257, 377))
        self.page_2.setObjectName("page_2")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.page_2)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.pushButton_3 = QtWidgets.QPushButton(self.page_2)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout_9.addWidget(self.pushButton_3)
        self.toolBox.addItem(self.page_2, icon10, "")
        self.verticalLayout_6.addWidget(self.toolBox)
        self.verticalLayout_3.addWidget(self.frame_7)
        self.horizontalLayout_3.addWidget(self.frame_5)
        self.frame_Paginas = QtWidgets.QFrame(self.frame_2)
        self.frame_Paginas.setStyleSheet("QFrame{\n"
"background-color: rgb(53, 53, 79);\n"
"}\n"
"\n"
"QLabel{\n"
"font:87 12pt \"Arial Black\";\n"
"background-color: #000000ff;\n"
"color: rgb(20, 200, 220);\n"
"border:0px solid #14C8DC;\n"
"\n"
"}")
        self.frame_Paginas.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_Paginas.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_Paginas.setObjectName("frame_Paginas")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_Paginas)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.stackedWidget = QtWidgets.QStackedWidget(self.frame_Paginas)
        self.stackedWidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_uno = QtWidgets.QWidget()
        self.page_uno.setObjectName("page_uno")
        self.label = QtWidgets.QLabel(self.page_uno)
        self.label.setGeometry(QtCore.QRect(90, 210, 91, 101))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("archivo-nuevo.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.stackedWidget.addWidget(self.page_uno)
        self.page_dos = QtWidgets.QWidget()
        self.page_dos.setObjectName("page_dos")
        self.label_2 = QtWidgets.QLabel(self.page_dos)
        self.label_2.setGeometry(QtCore.QRect(90, 210, 91, 101))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("reciente.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.stackedWidget.addWidget(self.page_dos)
        self.page_tres = QtWidgets.QWidget()
        self.page_tres.setObjectName("page_tres")
        self.label_3 = QtWidgets.QLabel(self.page_tres)
        self.label_3.setGeometry(QtCore.QRect(110, 230, 61, 61))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("cambiar.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.stackedWidget.addWidget(self.page_tres)
        self.page_cuatro = QtWidgets.QWidget()
        self.page_cuatro.setObjectName("page_cuatro")
        self.label_4 = QtWidgets.QLabel(self.page_cuatro)
        self.label_4.setGeometry(QtCore.QRect(90, 210, 91, 91))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("ajuste.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.stackedWidget.addWidget(self.page_cuatro)
        self.verticalLayout_5.addWidget(self.stackedWidget)
        self.horizontalLayout_3.addWidget(self.frame_Paginas)
        self.horizontalLayout_2.addWidget(self.frame_2)
        self.verticalLayout_2.addWidget(self.frame_inferior)
        self.verticalLayout.addWidget(self.frame)

        self.retranslateUi(Dialog)
        self.toolBox.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.Manu.setText(_translate("Dialog", "MENU"))
        self.bt1.setText(_translate("Dialog", "Nuevo Archivo            "))
        self.bt2.setText(_translate("Dialog", "Archivos Recietes        "))
        self.bt3.setText(_translate("Dialog", "Apagar                           "))
        self.bt4.setText(_translate("Dialog", "Configuracion               "))
        self.pushButton.setText(_translate("Dialog", "PushButton"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), _translate("Dialog", "Pagina 1"))
        self.pushButton_2.setText(_translate("Dialog", "PushButton"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_5), _translate("Dialog", "Pagina 2"))
        self.pushButton_3.setText(_translate("Dialog", "PushButton"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), _translate("Dialog", "Pagina 3"))

        self.bt1.clicked.connect(self.boton1Clicado)
        self.bt2.clicked.connect(self.boton2Clicado)
    def boton1Clicado(self):
        os.system(r'"C:\Program Files\Inkscape\bin\inkscape.exe"')
    def boton2Clicado(self):
        os.system(r'"C:\Program Files\Inkscape\bin\inkscape.exe"')


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())