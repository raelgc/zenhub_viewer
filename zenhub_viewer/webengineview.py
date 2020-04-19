from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEngineSettings
from .webenginepage import WebEnginePage

class WebEngineView(QWebEngineView):

  def __init__(self, parent = None):
    super().__init__(parent)
    self.setPage(WebEnginePage(self))
    self.setZoomFactor(1.3)
    settings = self.settings()
    settings.setAttribute(QWebEngineSettings.JavascriptEnabled, True)
    settings.setAttribute(QWebEngineSettings.JavascriptCanOpenWindows, True)
