
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QDesktopWidget

class WindowUtils():
    

    def show(self):
        #Find the current window where the mouse is just in case we are in a multi
        #monitor setup. And then move to its center.
        frameGm = self.frameGeometry()
        screen = QDesktopWidget().screenNumber(QApplication.desktop().cursor().pos())
        centerPoint = QDesktopWidget().availableGeometry(screen).center()
        frameGm.moveCenter(centerPoint)
        self.move(frameGm.topLeft())
        super().show()
            
        
    