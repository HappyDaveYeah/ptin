import sys
from PySide.QtCore import QSize, Qt, QMargins
from PySide.QtGui import QApplication, QMainWindow, QDesktopWidget, QStatusBar, QTextEdit, QLineEdit, QPushButton, \
    QSizePolicy, QWidget, QFrame, QHBoxLayout, QStyleFactory, QVBoxLayout, QLabel, QToolButton, QIcon, QStyle, QPixmap, \
    QGridLayout, QStackedLayout, QListWidget


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

        repFrame.setFrameStyle(QFrame.StyledPanel | QFrame.Sunken)
        appGridLayout = QGridLayout()
        appGridLayout.setSpacing(0)

        appList = [("bus", "0"), ("lightning", "1"), ("cams", "1"), ("factory", "1"),
                   ("health", "1"), ("roll", "0"), ("store", "1"), ("test", "0")]

        numApp = len(appList)
        cols = 4
        rows = numApp / 4
        for row in range(rows):
            for col in range(cols):
                app = appList.pop(0)
                but = QPushButton(app[0])
                but.setIcon(QIcon('../Resources/Icons/AppPoC/'+ app[0] + '.png'))
                but.setIconSize(QSize(60, 60))
                #but.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
                appGridLayout.addWidget(but, row, col)

        repFrame.setLayout(appGridLayout)


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
