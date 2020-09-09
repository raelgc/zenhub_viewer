from PyQt5.QtWidgets import QTabWidget, QTabBar
from PyQt5.QtGui import QIcon
from .webengineview import WebEngineView

class TabWidget(QTabWidget):

  def __init__(self, parent = None):
    super().__init__(parent)
    self.setDocumentMode(True)
    self.setTabsClosable(True)
    self.tabCloseRequested.connect(lambda i: self.removeTab(i))

  def addNewTab(self, qUrl, label='Loading...', icon = QIcon()):
    browser = WebEngineView(self)
    browser.setUrl(qUrl)
    if self.addTab(browser, icon, label) == 0:
      tabBar = self.tabBar()
      tabBar.tabButton(0, QTabBar.RightSide).deleteLater()
      tabBar.setTabButton(0, QTabBar.RightSide, None)
