from setuptools import setup

setup(name='typeform',
      version='0.1',
      description='API wrapper for CapsuleCRM written in Python',
      url='https://github.com/GearPlug/capsulecrm-python',
      author='Luisa Torres',
      author_email='hanna860@gmail.com',
      license='GPL',
      packages=['capsulecrm'],
      install_requires=[
          'requests',
      ],
      zip_safe=False)
