from PySide.QtCore import Qt
from PySide.QtGui import QVBoxLayout, QPushButton, QCheckBox, QLabel, QLineEdit, QHBoxLayout, QDialog

__author__ = 'Nikiva'


class DialogApp(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.findLabel = QLabel("Find &What:")
        self.lineEdit = QLineEdit()
        self.findLabel.setBuddy(self.lineEdit)
        self.caseCheckBox = QCheckBox("Match &Case")
        self.backwardCheckBox = QCheckBox("Search &Backward")
        self.findButton = QPushButton("&Find")
        self.findButton.setDefault(True)
        self.closeButton = QPushButton("Close")
        self.topLeftLayout = QHBoxLayout()
        self.topLeftLayout.addWidget(self.findLabel)
        self.topLeftLayout.addWidget(self.lineEdit)
        self.leftLayout = QVBoxLayout()
        self.leftLayout.addLayout(self.topLeftLayout)
        self.leftLayout.addWidget(self.caseCheckBox)
        self.leftLayout.addWidget(self.backwardCheckBox)
        self.rightLayout = QVBoxLayout()
        self.rightLayout.addWidget(self.findButton)
        self.rightLayout.addWidget(self.closeButton)
        self.rightLayout.addStretch()
        self.mainLayout = QHBoxLayout()
        self.mainLayout.addLayout(self.leftLayout)
        self.mainLayout.addLayout(self.rightLayout)
        self.findButton.clicked.connect(self.findText)
        self.setWindowTitle("Find")
        self.setLayout(self.mainLayout)
        self.show()

    def findText(self):
        mySearchText = self.lineEdit.text()
        if self.caseCheckBox.isChecked():
            caseSensitivity = Qt.CaseSensitive
        else:
            caseSensitivity = Qt.CaseInsensitive
        if self.backwardCheckBox.isChecked():
            #search functionality goes here...
            print("Backward Find ")
        else:
            #search functionality goes here...
            print("Forward Find")
