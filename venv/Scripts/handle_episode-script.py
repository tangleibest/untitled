#!C:\Users\tl\PycharmProjects\untitled\venv\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'series==2.34.0','console_scripts','handle_episode'
__requires__ = 'series==2.34.0'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('series==2.34.0', 'console_scripts', 'handle_episode')()
    )
