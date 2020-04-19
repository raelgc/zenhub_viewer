import glob, os, setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

def _data_files():
  yield os.path.join('share', 'doc', 'zenhub_viewer'), \
    ['LICENSE', 'README.md']
  yield os.path.join('share', 'applications'), \
    glob.glob(os.path.join('share', '*.desktop'))
  yield os.path.join('share', 'pixmaps'), \
    glob.glob(os.path.join('zenhub_viewer', 'resources', 'zenhub_viewer.png'))

setuptools.setup(
  name="zenhub_viewer",
  version="0.9",
  author="Rael Gugelmin Cunha",
  author_email="rael.gc@gmail.com",
  data_files=list(_data_files()),
  description="ZenHub Viewer is a non official desktop viewer for ZenHub",
  long_description=long_description,
  long_description_content_type="text/markdown",
  keywords = "zenhub desktop project collaboration",
  entry_points = {
    'gui_scripts': ['zenhub_viewer = zenhub_viewer.__main__:main'],
  },
  url="https://github.com/raelgc/zenhub_viewer",
  packages=setuptools.find_packages(),
  classifiers=[
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
    "Development Status :: 4 - Beta",
    "Environment :: X11 Applications :: Qt",
    "Intended Audience :: Information Technology",
  ],
  python_requires='>=3.6',
)
