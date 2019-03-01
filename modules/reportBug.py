# -*- coding: utf-8 -*-
#  reportBug.py: -*- Python -*-  DESCRIPTIVE TEXT.

from .reportBugBA import Ui_reportBugBA
from .util import *
#from PyQt5.QtGui import *
#from PyQt5.QtCore import *
#from PyQt5 import *
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QWidget
import sys
import string
import smtplib
from .version import VERSION

AUTHOR_ADDR = "phil_schwartz@users.sourceforge.net"

class reportBug(QWidget, Ui_reportBugBA):
    def __init__(self, parent=None, name=None):
        #reportBugBA.__init__(self, parent)
        
        super(reportBug,self).__init__()
        self.setupUi(self)
        
        self.parent = parent
        self.kodos_main = parent.kodos_main
        self.populate()


    def populate(self):
        self.OSEdit.setText(sys.platform)
        pyvers = sys.version.replace("\n", " - ")
        self.pythonVersionEdit.setText(pyvers)
        self.PyQtVersionEdit.setText(QT_VERSION_STR)
        self.regexMultiLineEdit.setPlainText(self.kodos_main.regexMultiLineEdit.toPlainText())
        self.stringMultiLineEdit.setPlainText(self.kodos_main.stringMultiLineEdit.toPlainText())


    def cancel_slot(self):
        self.parent.close()

    def submit_slot(self):
        addr = str(self.emailAddressEdit.text())
        if not addr:
            msg = self.tr(
                "An email address is necessary so that the author "
                "can contact you.  Your email address will not "
                "be used for any other purposes.")

            QMessageBox.information(None,
                                    self.tr("You must supply a valid email address"),
                                    msg)
            return

        msg = "Subject: Kodos bug report\n\n"
        msg += "Kodos Version: %s\n" % VERSION
        msg += "Operating System: %s\n" % str(self.OSEdit.text())
        msg += "Python Version: %s\n" % str(self.pythonVersionEdit.text())
        msg += "PyQt Version: %s\n" % str(self.PyQtVersionEdit.text())
        msg += "\n" + "=" * 70 + "\n"
        msg += "Regex:\n%s\n" % str(self.regexMultiLineEdit.text())
        msg += "=" * 70 + "\n"
        msg += "String:\n%s\n" % str(self.stringMultiLineEdit.text())
        msg += "=" * 70 + "\n"
        msg += "Comments:\n%s\n" % str(self.commentsMultiLineEdit.text())
        email_server = str(self.kodos_main.prefs.emailServerEdit.text()) or "localhost"
        try:
            server = smtplib.SMTP(email_server)
            server.sendmail(addr, AUTHOR_ADDR, msg)
            server.quit()
            QMessageBox.information(None,
                                    self.tr("Bug report sent"),
                                    self.tr("Your bug report has been sent."))
            self.parent.close()
        except Exception as e:
            QMessageBox.information(None,
                                    self.tr("An exception occurred sending bug report"),
                                    str(e))


class reportBugWindow(QMainWindow):
    def __init__(self, kodos_main):
        self.kodos_main = kodos_main
        QMainWindow.__init__(self, kodos_main)#, Qt.Window | Qt.WA_DeleteOnClose)

        self.setGeometry(100, 50, 800, 600)
        self.setWindowTitle(self.tr("Report a Bug"))
        self.setWindowIcon(QIcon(QPixmap(":images/kodos_icon.png")))

        self.bug_report = reportBug(self)
        self.setCentralWidget(self.bug_report)


        self.createMenu()
        self.createToolBar()

        self.show()


    def createMenu(self):
        self.menubar = self.menuBar()
        self.filemenu = self.menubar.addMenu(self.tr("&File"))
        
        closeAction = QAction(self.tr("close"),self)
        self.filemenu.addAction(closeAction)


    def createToolBar(self):
        toolbar = QToolBar()
        self.addToolBar(toolbar)
        self.logolabel = kodos_toolbar_logo(toolbar)
        

