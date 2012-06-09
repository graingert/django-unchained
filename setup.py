import sys
import webbrowser
from distutils.core import setup

trailer_url = 'http://youtube.com/v/rC8VJ9aeB_g?hd=1&autoplay=1'

if 'install' in sys.argv:
    webbrowser.open_new(trailer_url)


setup(
    name='django-unchained',
    version='1.0',
    maintainer='Jannis Leidel',
    maintainer_email='jannis@leidel.info',
    url=trailer_url)
