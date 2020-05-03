#!/usr/bin/env python3
import signal, sys
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon
from .tabwidget import TabWidget
from .resources import Resources

class MainWindow(QMainWindow):

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.setWindowTitle(Resources.APP_NAME)
    self.icon = QIcon(Resources.get('zenhub_viewer.png'))
    self.setWindowIcon(self.icon)
    self.tabs = TabWidget(self)
    self.tabs.addNewTab(QUrl(f'https://app.{Resources.HOST}'), 'Board', self.icon)
    self.setCentralWidget(self.tabs)
    self.showMaximized()

def main():
  signal.signal(signal.SIGINT, signal.SIG_DFL)
  app = QApplication(sys.argv)
  window = MainWindow()
  window.show()
  app.exec_()
