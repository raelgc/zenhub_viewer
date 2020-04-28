import os

class Resources:

  HOST = 'zenhub.com'
  APP_NAME = 'ZenHub Viewer'
  BLACK_LIST = []
  WHITE_LIST = ['headway-widget.net']

  INSTALL_DIR = os.path.dirname(os.path.realpath(__file__))

  def get(filename):
    return os.path.join(Resources.INSTALL_DIR, 'resources', filename)

  def isWorkspace(url):
    return url.startswith(f'https://app.{Resources.HOST}/workspace')

  def isAuth(url):
    return url.startswith('https://github.com/login') or url.startswith('https://github.com/session') or url.startswith('https://github.com/sessions')
    
