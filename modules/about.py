# -*- coding: utf-8 -*-
#  about.py: -*- Python -*-  DESCRIPTIVE TEXT.

from . aboutBA import Ui_AboutBA
from . import  version
from PyQt5.QtWidgets import QDialog


class About(QDialog, Ui_AboutBA):
    def __init__(self):
        super(About, self).__init__()
        self.setupUi(self)
        
        self.versionLabel.setText(version.VERSION)
        