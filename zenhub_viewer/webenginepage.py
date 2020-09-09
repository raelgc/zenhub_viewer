from PyQt5.QtGui import QDesktopServices
from PyQt5.QtWebEngineWidgets import QWebEnginePage
from .resources import Resources

class WebEnginePage(QWebEnginePage):

  def acceptNavigationRequest(self, qUrl, requestType, isMainFrame):
    tabs = self.parent().parent().parent()
    host = qUrl.host()
    url = qUrl.toString()
    print(url)
    if host in Resources.BLOCKED_LIST:
      return False
    if requestType == self.NavigationTypeLinkClicked and Resources.isWorkspace(url):
      tabs.addNewTab(qUrl)
      return False
    if host.endswith(Resources.HOST) or Resources.isAuth(url) or host in Resources.ALLOWED_LIST:
      return True
    QDesktopServices.openUrl(qUrl)
    return False

  def createWindow(self, windowType):
    return WebEnginePage(self.parent())
