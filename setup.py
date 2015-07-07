# -*- coding: utf-8 -*-

from setuptools import setup

setup(name='Empire-Agent',
      version='0.0.3',
      description='Empire Agent',
      url='http://github.com/wenxer/empire-agent',
      author='Shown Tien',
      author_email='hightian@gmail.com',
      license='MIT',
      packages=['empire_agent'],
      zip_safe=False,
      entry_points={
          'console_scripts': [
              'empire = empire_agent.empire:main'],
      })
