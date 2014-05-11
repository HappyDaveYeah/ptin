from PySide.QtCore import Qt
from PySide.QtGui import QVBoxLayout, QPushButton, QCheckBox, QLabel, QLineEdit, QHBoxLayout, QDialog, QIcon, QFrame
import navyCalls

__author__ = 'Nikiva'


class DialogApp(QDialog):
    def __init__(self, app, parent=None):
        QDialog.__init__(self)
        self.app = app
        self.setWindowTitle(self.app.name)

        self.label = QLabel(self.app.name)
        self.label.setPixmap(self.app.icon.pixmap(50, 50, QIcon.Normal))
        self.label.setFrameStyle(QFrame.StyledPanel | QFrame.Sunken)

        # Config Buttons Install/Enable
        if (self.app.installed == "1"):
            self.installedButt = QPushButton("Uninstall")
            self.installedButt.clicked.connect(self.uninstallApp)
        else:
            self.installedButt = QPushButton("Install")
            self.installedButt.clicked.connect(self.installApp)


        if (self.app.enabled == "1"):
            self.enabledButt = QPushButton("Disable")
            self.enabledButt.clicked.connect(self.disableApp)
        else:
            self.enabledButt = QPushButton("Enable")
            self.enabledButt.clicked.connect(self.enableApp)
            if(self.app.installed == "0"):
                self.enabledButt.setEnabled(False)

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

    def installApp(self):
        navyCalls.add(self.app)
        self.installedButt.setText("Uninstall")
        self.installedButt.clicked.connect(self.uninstallApp)
        self.enabledButt.setEnabled(True)

    def uninstallApp(self):
        navyCalls.delete(self.app)
        self.installedButt.setText("Install")
        self.installedButt.clicked.connect(self.installApp)
        self.enabledButt.setText("Enable")
        self.enabledButt.clicked.connect(self.enableApp)
        self.enabledButt.setEnabled(False)

    def enableApp(self):
        navyCalls.enable(self.app)
        self.enabledButt.setText("Disable")
        self.enabledButt.clicked.connect(self.disableApp)

    def disableApp(self):
        navyCalls.disable(self.app)
        self.enabledButt.setText("Enable")
        self.enabledButt.clicked.connect(self.enableApp)
