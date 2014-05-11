import sys
from dialogApp import *
from PySide.QtCore import QSize, Qt, QMargins
from PySide.QtGui import QApplication, QMainWindow, QDesktopWidget, QStatusBar, QTextEdit, QLineEdit, QPushButton, \
    QSizePolicy, QWidget, QFrame, QHBoxLayout, QStyleFactory, QVBoxLayout, QLabel, QToolButton, QIcon, QStyle, QPixmap, \
    QGridLayout, QStackedLayout, QListWidget, QLayout, QSpacerItem, QCheckBox, QBoxLayout


class MainWindow(QMainWindow):
    """ Main Window Class
    """

    def __init__(self):
        """ Constructor Function
        """
        QMainWindow.__init__(self)
        self.setWindowTitle("Hylian")
        self.setGeometry(0, 0, 900, 600)
        self.center()

    def center(self):
        """ Function to center the application
        """
        qRect = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qRect.moveCenter(centerPoint)
        self.move(qRect.topLeft())

    def setupComponents(self):
        """ Function to setup ...
        """

        # Central widget
        centralWidget = QWidget()
        self.setCentralWidget(centralWidget)

        # Status bar
        self.myStatusBar = QStatusBar()
        self.setStatusBar(self.myStatusBar)
        self.myStatusBar.showMessage('Ready', 5000)

        # Actions
        self.createActions()

        # Top Menu QFrame
        topMenuFrame = QFrame()
        self.createTopMenu(topMenuFrame)

        # Repository
        repFrame = QFrame()
        self.createRepository(repFrame)

        # StackedLayout
        self.centerStackedL = QStackedLayout()
        self.centerStackedL.insertWidget(0, repFrame)
        self.sysLabel = QLabel()
        #self.sysLabel.setFrameShape(QFrame.Box)
        self.sysLabel.setText("Sys")
        self.centerStackedL.insertWidget(1, self.sysLabel)


        # Main Layout
        mainLayout = QVBoxLayout()
        mainLayout.setContentsMargins(QMargins(0, 0, 0, 0))

        mainLayout.addWidget(topMenuFrame)
        mainLayout.addLayout(self.centerStackedL)

        centralWidget.setLayout(mainLayout)



    def createActions(self):
        """ Function to create actions for menus
        """

    def createTopMenu(self, topMenuFrame):
        """ Function to create top menu frame
        """

        topMenuFrame.setFrameStyle(QFrame.StyledPanel | QFrame.Sunken)
        topMenuFrame.setStyleSheet("QFrame { background-color:qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(250, 250, 250, 90), stop:0.9 rgba(255, 255, 255, 255)) }")


        # Navigation buttons
        backBut = QToolButton()
        backBut.setIcon(QIcon('../Resources/Icons/back.png'))
        forwardBut = QToolButton()
        forwardBut.setIcon(QIcon('../Resources/Icons/forward.png'))
        # Navigation layout
        navigationL = QHBoxLayout()
        navigationL.addWidget(backBut)
        navigationL.addWidget(forwardBut)
        navigationL.setSpacing(0)

        # Button menu
        repBut = QToolButton()
        #repBut.setStyleSheet("background-color:transparent; border:none")
        repBut.setText("Repository")
        repBut.setIcon(QIcon('../Resources/Icons/rep.png'))
        repBut.setIconSize(QSize(20, 20))
        repBut.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        repBut.setCheckable(True)
        repBut.setAutoExclusive(True)
        repBut.clicked.connect(lambda: self.centerStackedL.setCurrentIndex(0))
        configBut = QToolButton()
        #configBut.setStyleSheet("background-color:transparent; border:none")
        configBut.setText("System")
        configBut.setIcon(QIcon('../Resources/Icons/sys.png'))
        configBut.setIconSize(QSize(20, 20))
        configBut.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        configBut.setCheckable(True)
        configBut.setAutoExclusive(True)
        configBut.clicked.connect(lambda: self.centerStackedL.setCurrentIndex(1))
        logBut = QToolButton()
        #logBut.setStyleSheet("background-color:transparent; border:none")
        logBut.setText("Logging")
        logBut.setIcon(QIcon('../Resources/Icons/log.png'))
        logBut.setIconSize(QSize(20, 20))
        logBut.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        logBut.setCheckable(True)
        logBut.setAutoExclusive(True)
        logBut.clicked.connect(lambda: self.centerStackedL.setCurrentIndex(2))
        # Button menu layout
        buttonMenuL = QHBoxLayout()
        buttonMenuL.addWidget(repBut)
        buttonMenuL.addWidget(configBut)
        buttonMenuL.addWidget(logBut)
        buttonMenuL.setSpacing(0)

        # Search button
        search = QLineEdit()
        search.setPlaceholderText("search")

        # Main layout for top menu
        mainL = QHBoxLayout()
        mainL.setContentsMargins(QMargins(10, 0, 10, 0))
        mainL.addLayout(navigationL)
        mainL.addStretch(2.5)
        mainL.addLayout(buttonMenuL)
        mainL.addStretch(2)
        mainL.addWidget(search)

        topMenuFrame.setLayout(mainL)


    def createRepository(self, repFrame):
        """ Function to create repository frame
        """

        # Call to Navy
        # TODO: Funcio primitiva per a obtenir llista dapps{id, active} from Navy
        appList = [("bus", "0"), ("lightning", "1"), ("cams", "1"), ("factory", "1"),
                   ("health", "1"), ("roll", "0"), ("store", "1"), ("test", "0")]

        # App grid menu
        appGridLayout = QGridLayout()
        appGridLayout.setContentsMargins(30, 15, 11, 20)
        appGridLayout.setSpacing(0)

        appsTopFrame = QFrame()
        appsTopFrame.setFrameStyle(QFrame.StyledPanel | QFrame.Sunken)
        appsTopLabel = QLabel("Apps")
        appsTopLayout = QVBoxLayout()
        appsTopLayout.setContentsMargins(6, 3, 6, 3)
        appsTopLayout.addWidget(appsTopLabel)
        appsTopFrame.setLayout(appsTopLayout)
        appGridLayout.addWidget(appsTopFrame, 0, 0, 1, 4)

        numApp = len(appList)
        cols = 4
        rows = numApp / cols
        for row in range(1, rows + 1):
            for col in range(cols):
                app = appList.pop(0)

                frame = QFrame()
                if row % 2 != 0:
                    frame.setStyleSheet("QFrame { background-color:rgb(250,250,250) }")
                frame.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Maximum)
                frame.setFrameStyle(QFrame.StyledPanel | QFrame.Sunken)
                vLayout = QVBoxLayout()
                hLayout = QHBoxLayout()

                but = QToolButton()
                q = QIcon()
                # TODO: Icons amb el color corresponent al seu estat!
                q.addPixmap(QPixmap('../Resources/Icons/AppPoC/'+ app[0] + '.png'), QIcon.Disabled, QIcon.Off)
                #q.addPixmap(QPixmap('../Resources/Icons/AppPoC/'+ app[0] + '.png'), QIcon.Normal)

                but.setIcon(q)
                but.setIconSize(QSize(50, 50))
                but.clicked.connect(self.openDialogApp)

                titleLabel = QLabel(app[0])
                #titleLabel.setFrameStyle(QFrame.StyledPanel | QFrame.Sunken)
                catLabel = QLabel("Test")
                #catLabel.setFrameStyle(QFrame.StyledPanel | QFrame.Sunken)
                vLayout.addWidget(titleLabel)
                vLayout.addWidget(catLabel)
                vLayout.addSpacerItem(QSpacerItem(0, 0, QSizePolicy.Preferred, QSizePolicy.Expanding))

                hLayout.addWidget(but)
                hLayout.addLayout(vLayout)
                frame.setLayout(hLayout)
                appGridLayout.addWidget(frame, row, col)


        appGridLayout.addItem(QSpacerItem(0, 0, QSizePolicy.Preferred, QSizePolicy.Expanding), rows + 1, 0, 1, cols)


        # Side menu
        titleFrame = QFrame()
        titleFrame.setFrameStyle(QFrame.StyledPanel | QFrame.Sunken)
        titleLabel = QLabel("Filter")
        titleLayout = QVBoxLayout()
        titleLayout.setContentsMargins(6, 3, 6, 3)
        titleLayout.addWidget(titleLabel)
        titleFrame.setLayout(titleLayout)

        checkBoxFrame = QFrame()
        checkBoxFrame.setFrameStyle(QFrame.StyledPanel | QFrame.Sunken)
        checkBoxLayout = QVBoxLayout()
        checkBoxFrame.setLayout(checkBoxLayout)

        instCBox= QCheckBox("Installed")
        notInstCBox= QCheckBox("Not installed")
        enabledCBox = QCheckBox("Enabled")
        notEnabledCBox = QCheckBox("Not enabled")

        checkBoxLayout.addWidget(instCBox)
        checkBoxLayout.addWidget(notInstCBox)
        checkBoxLayout.addWidget(enabledCBox)
        checkBoxLayout.addWidget(notEnabledCBox)

        sideMenuLayout = QVBoxLayout()
        sideMenuLayout.setSpacing(0)
        sideMenuLayout.setContentsMargins(0, 15, 30, 11)
        sideMenuLayout.addWidget(titleFrame)
        sideMenuLayout.addWidget(checkBoxFrame)
        sideMenuLayout.addSpacerItem(QSpacerItem(0, 0, QSizePolicy.Preferred, QSizePolicy.Expanding))

        # Main layout management
        mainRepLayout = QHBoxLayout()
        mainRepLayout.addStretch(1)
        mainRepLayout.addLayout(appGridLayout, 12)
        mainRepLayout.addLayout(sideMenuLayout, 3)
        mainRepLayout.addStretch(1)

        repFrame.setLayout(mainRepLayout)

    def openDialogApp(self):
        dialogApp = DialogApp()
        dialogApp.exec_()


if __name__ == '__main__':
    try:
        myApp = QApplication(sys.argv)
        myApp.setStyle("Plastique")
        mainWindow = MainWindow()
        mainWindow.setupComponents()
        mainWindow.show()
        myApp.exec_()
        sys.exit(0)
    except NameError:
        print ("Name Error:", sys.exc_info()[1])
    except SystemExit:
        print ("Closing Window...")
    except Exception:
        print (sys.exc_info()[1])
