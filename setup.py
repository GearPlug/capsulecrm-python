import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(name='capsulecrm-python',
      version='0.1.2',
      description='API wrapper for CapsuleCRM written in Python',
      long_description=read('README.md'),
      url='https://github.com/GearPlug/capsulecrm-python',
      author='Luisa Torres',
      author_email='hanna860@gmail.com',
      license='GPL',
      packages=['capsulecrm'],
      install_requires=[
          'requests',
      ],
      zip_safe=False)
