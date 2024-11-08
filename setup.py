import os
from setuptools import find_packages, setup

name = 'chs'

def get_version():
  file_path = os.path.dirname(os.path.abspath(__file__))
  version_file = open(os.path.join(file_path, './chs/VERSION'), 'r')
  return version_file.read().rstrip()

setup(
  name = name,
  version = get_version(),
  keywords = ['chess', 'terminal', 'stockfish'],
  packages = find_packages(),
  install_requires=[
    'python-chess',
    'editdistance',
  ],
  entry_points={
    'console_scripts': ['{} = chs.main:run'.format(name)],
  }
)
