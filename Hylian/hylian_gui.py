import sys
from PySide.QtGui import QApplication, QMainWindow, QDesktopWidget, QStatusBar, QTextEdit, QLineEdit


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
        """ Function to setup status bar, central widget, menu bar
        """
        self.myStatusBar = QStatusBar()
        self.setStatusBar(self.myStatusBar)
        self.myStatusBar.showMessage('Ready', 5000)
        # self.textEdit = QTextEdit()
        # self.setCentralWidget(self.textEdit)
        self.createActions()
        self.createToolBar()
        search = QLineEdit()

        self.mainToolBar.addWidget(search)
        # self.mainToolBar.addAction(self.newAction)
        # self.mainToolBar.addSeparator()
        # self.mainToolBar.addAction(self.copyAction)
        # self.mainToolBar.addAction(self.pasteAction)

    def createActions(self):
        """ Function to create actions for menus
        """

    def createToolBar(self):
        """ Function to create and config the tool bar
        """
        self.mainToolBar = self.addToolBar('Main')
        self.mainToolBar.setMovable(False)



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
