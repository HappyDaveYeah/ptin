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

        # Top QFrame
        topFrame = QFrame()
        #topFrame.setFrameShape(QFrame.Box)
        topFrame.setStyleSheet("QFrame { background-color:qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(250, 250, 250, 90), stop:0.9 rgba(255, 255, 255, 255)) }")

        # Layouts
        menuLayout = QHBoxLayout()
        menuLayout.setContentsMargins(QMargins(10, 0, 10, 0))
        centerLayout = QStackedLayout()
        mainLayout = QVBoxLayout()
        mainLayout.setContentsMargins(QMargins(0, 0, 0, 0))

        # Top move buttons
        self.backBut = QToolButton()
        self.backBut.setIcon(QIcon('../Resources/Icons/back.png'))
        self.forwardBut = QToolButton()
        self.forwardBut.setIcon(QIcon('../Resources/Icons/forward.png'))
        moveLayout = QHBoxLayout()
        moveLayout.addWidget(self.backBut)
        moveLayout.addWidget(self.forwardBut)
        moveLayout.setSpacing(0)

        # Top menu buttons
        self.repBut = QToolButton()
        #self.repBut.setStyleSheet("background-color:transparent; border:none")
        self.repBut.setText("Repository")
        self.repBut.setIcon(QIcon('../Resources/Icons/rep.png'))
        self.repBut.setIconSize(QSize(20, 20))
        self.repBut.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.repBut.setCheckable(True)
        self.repBut.setAutoExclusive(True)
        self.repBut.clicked.connect(lambda: centerLayout.setCurrentIndex(0))
        self.configBut = QToolButton()
        #self.configBut.setStyleSheet("background-color:transparent; border:none")
        self.configBut.setText("System")
        self.configBut.setIcon(QIcon('../Resources/Icons/sys.png'))
        self.configBut.setIconSize(QSize(20, 20))
        self.configBut.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.configBut.setCheckable(True)
        self.configBut.setAutoExclusive(True)
        self.configBut.clicked.connect(lambda: centerLayout.setCurrentIndex(1))
        self.logBut = QToolButton()
        #self.logBut.setStyleSheet("background-color:transparent; border:none")
        self.logBut.setText("Logging")
        self.logBut.setIcon(QIcon('../Resources/Icons/log.png'))
        self.logBut.setIconSize(QSize(20, 20))
        self.logBut.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.logBut.setCheckable(True)
        self.logBut.setAutoExclusive(True)
        self.logBut.clicked.connect(lambda: centerLayout.setCurrentIndex(2))
        menuButLayout = QHBoxLayout()
        menuButLayout.addWidget(self.repBut)
        menuButLayout.addWidget(self.configBut)
        menuButLayout.addWidget(self.logBut)
        menuButLayout.setSpacing(0)


        # Top search button
        self.search = QLineEdit()
        self.search.setPlaceholderText("search")


        menuLayout.addLayout(moveLayout)
        menuLayout.addStretch(2.5)
        menuLayout.addLayout(menuButLayout)
        menuLayout.addStretch(2)
        menuLayout.addWidget(self.search)



        self.repLabel = QLabel()
        #self.repLabel.setFrameShape(QFrame.Box)
        self.repLabel.setText("Rep")

        self.sysLabel = QLabel()
        #self.sysLabel.setFrameShape(QFrame.Box)
        self.sysLabel.setText("Sys")


        centerLayout.insertWidget(0, self.repLabel)
        centerLayout.insertWidget(1, self.sysLabel)


        topFrame.setLayout(menuLayout)
        mainLayout.addWidget(topFrame)
        mainLayout.addLayout(centerLayout)


        centralWidget.setLayout(mainLayout)




    def createActions(self):
        """ Function to create actions for menus
        """




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
