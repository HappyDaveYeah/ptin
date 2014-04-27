import sys
from PySide.QtCore import QSize
from PySide.QtGui import QApplication, QMainWindow, QDesktopWidget, QStatusBar, QTextEdit, QLineEdit, QPushButton, \
    QSizePolicy, QWidget, QFrame, QHBoxLayout, QStyleFactory, QVBoxLayout, QLabel, QToolButton, QIcon, QStyle, QPixmap


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

        # Central Widget
        centralWidget = QWidget()
        self.setCentralWidget(centralWidget)

        # Status Bar
        self.myStatusBar = QStatusBar()
        self.setStatusBar(self.myStatusBar)
        self.myStatusBar.showMessage('Ready', 5000)

        # Actions
        self.createActions()

        # Top QFrame
        topFrame = QFrame()
        topFrame.setFrameShape(QFrame.Box)

        # Move Buttons
        self.backBut = QToolButton()
        self.backBut.setIcon(QIcon('../Resources/Icons/back.png'))
        self.forwardBut = QToolButton()
        self.forwardBut.setIcon(QIcon('../Resources/Icons/forward.png'))
        moveLayout = QHBoxLayout()
        moveLayout.addWidget(self.backBut)
        moveLayout.addWidget(self.forwardBut)
        moveLayout.setSpacing(0)

        #
        self.repBut = QToolButton()
        self.repBut.setText("Repository")
        self.configBut = QToolButton()
        self.configBut.setText("Config Sys")
        self.logBut = QToolButton()
        self.logBut.setText("Logging")

        #
        self.search = QLineEdit()
        self.search.setPlaceholderText("search")


        menuLayout = QHBoxLayout()

        menuLayout.addLayout(moveLayout)
        menuLayout.addStretch(2.5)
        menuLayout.addWidget(self.repBut)
        menuLayout.addWidget(self.configBut)
        menuLayout.addWidget(self.logBut)
        menuLayout.addStretch(2)
        menuLayout.addWidget(self.search)



        self.testLabel = QLabel()
        self.testLabel.setFrameShape(QFrame.Box)
        self.testLabel.setText("Main")

        bottomLayout = QVBoxLayout()
        bottomLayout.addWidget(self.testLabel)

        #topFrame.setLayout(menuLayout)
        mainLayout = QVBoxLayout()
        mainLayout.addLayout(menuLayout)
        mainLayout.addLayout(bottomLayout)


        centralWidget.setLayout(mainLayout)




    def createActions(self):
        """ Function to create actions for menus
        """




if __name__ == '__main__':
    try:
        myApp = QApplication(sys.argv)
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
