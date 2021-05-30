from setuptools import setup

setup(name='pyomatic',
      version='1.0',
      # list folders, not files
      packages=['pyomatic'],
      scripts=['pyomatic/bin/pom.py'],
      package_dir={'pyomatic':'pyomatic'}, 
      #package_data={'pyomatic': ['data/snippets.txt']},
      package_data = { 
            '': ['data/snippets.txt','*.txt', '*.yaml', '*.json'],
      },
   
      )