from PySide.QtCore import Qt
from PySide.QtGui import QVBoxLayout, QPushButton, QCheckBox, QLabel, QLineEdit, QHBoxLayout, QDialog, QIcon, QFrame

__author__ = 'Nikiva'


class DialogApp(QDialog):
    def __init__(self, app, parent=None):
        QDialog.__init__(self)
        self.setWindowTitle(app.name)

        self.label = QLabel(app.name)
        self.label.setPixmap(app.icon.pixmap(50, 50, QIcon.Disabled, QIcon.Off))
        self.label.setFrameStyle(QFrame.StyledPanel | QFrame.Sunken)


        self.installedButt = QPushButton("Install")

        self.enabledButt = QPushButton("Enable")

        self.rightLayout = QVBoxLayout()
        self.ButtLayout = QHBoxLayout()
        self.ButtLayout.addWidget(self.installedButt)
        self.ButtLayout.addWidget(self.enabledButt)
        self.rightLayout.addLayout(self.ButtLayout)
        self.rightLayout.addStretch()

        self.mainLayout = QHBoxLayout()
        self.mainLayout.addWidget(self.label)
        self.mainLayout.addLayout(self.rightLayout)
        self.setLayout(self.mainLayout)
