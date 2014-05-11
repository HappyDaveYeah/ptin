from PySide.QtGui import QIcon, QPixmap

__author__ = 'Nikiva'

class App:
    def __init__(self, id, status, appListXML):

        for node in appListXML:
            if node.attributes['id'].value == id:
                self.name = node.getAttribute('name')
                self.icon = QIcon()
                # TODO: Icons amb el color corresponent al seu estat!
                self.icon.addPixmap(QPixmap(node.getAttribute('iconPath')), QIcon.Disabled, QIcon.Off)
                #self.icon.addPixmap(QPixmap('../Resources/Icons/AppPoC/'+ app[0] + '.png'), QIcon.Normal)
                break

        self.id = id
        self.status = status
