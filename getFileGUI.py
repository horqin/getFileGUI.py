# @file getFileGUI.py
# @author Tokhta Horqin <tokhta@outlook.com>
# @date 12/27/2019
# @license GNU

import sys
from os import path
from pathlib import Path

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMessageBox, QFileDialog, QWidget, QPushButton, QLineEdit, QApplication

import settings


# @brief main function
# @param func a function that return True if success, and False if failure
def getFileGUI(func):
    app = QApplication(sys.argv)
    ex = MainWindow(func)
    ex.show()
    sys.exit(app.exec_())


# @brief set main window
class MainWindow(QWidget):
    def __init__(self, func):
        super(QWidget, self).__init__()
        self.fileLineEdit = None
        self.getFileButton = None
        self.runButton = None
        self.file = None
        self.fileDirectory = str(Path.home())
        self.func = func
        self.initUI()

    def initUI(self):
        self.setWindowTitle(settings.windowTitle)
        self.setWindowIcon(QIcon(settings.windowIcon))
        self.setGeometry(270, 110, 500, 309)
        self.setFixedSize(500, 309)
        self.setWindowFlags(Qt.WindowMinimizeButtonHint | Qt.WindowCloseButtonHint)
        self.setFileLineEdit()
        self.setGetFileButton()
        self.setRunButton()

    def setFileLineEdit(self):
        self.fileLineEdit = QLineEdit(self.file, self)
        self.fileLineEdit.setDisabled(True)
        self.fileLineEdit.move(50, 82)
        self.fileLineEdit.resize(250, 31)

    def setGetFileButton(self):
        self.getFileButton = QPushButton(settings.getFileButtonText, self)
        self.getFileButton.move(350, 82)
        self.getFileButton.resize(100, 31)
        self.getFileButton.clicked.connect(self.on_get_file_click)

    def on_get_file_click(self):
        self.setGetFileDialog()
        self.updateGetFileLineEditAction()

    def setGetFileDialog(self):
        file, _ = QFileDialog(self).getOpenFileName(
            self, settings.getFileDialogText, self.fileDirectory,
            options=(QFileDialog.Options() | QFileDialog.DontUseNativeDialog))
        if file and Path(file).is_file():
            self.file = file
            self.fileDirectory = path.dirname(file)
        elif not (self.file and Path(self.file).is_file()):
            self.file = None
            self.fileDirectory = str(Path.home())
        # else:
        #     # do nothing

    def updateGetFileLineEditAction(self):
        self.fileLineEdit.setText(self.file)

    def setRunButton(self):
        self.runButton = QPushButton(settings.runButtonText, self)
        self.runButton.move(175, 195)
        self.runButton.resize(100, 31)
        self.runButton.clicked.connect(self.on_run_click)

    def on_run_click(self):
        status = self.runAction()
        if status:
            self.setComputeSuccessMessageBox()
        else:
            self.setComputeFailureMessageBox()

    def runAction(self):
        return self.func(self.file)

    def setComputeSuccessMessageBox(self):
        QMessageBox(self).information(self, settings.runInformationMessageBoxText,
                                      settings.runInformationMessageBoxSuccessText, QMessageBox.Ok, QMessageBox.Ok)

    def setComputeFailureMessageBox(self):
        QMessageBox(self).information(self, settings.runInformationMessageBoxText,
                                      settings.runInformationMessageBoxFailureText, QMessageBox.Ok, QMessageBox.Ok)
