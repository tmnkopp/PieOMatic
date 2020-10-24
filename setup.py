from setuptools import setup

setup(name='pyomatic',
      version='1.0',
      # list folders, not files
      packages=['pyomatic'],
      scripts=['pyomatic/bin/pom.py'],
      package_data={'pyomatic': ['data/snippets.txt']},
      )