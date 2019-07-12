"""
Copyright (c) 2012-2014 Ben Croston

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
of the Software, and to permit persons to whom the Software is furnished to do
so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

__version__ = '0.5.8.6'

classifiers = """\
Development Status :: 5 - Production/Stable
Operating System :: POSIX :: Linux
License :: OSI Approved :: MIT License
Intended Audience :: Developers
Programming Language :: Python :: 2.7
Programming Language :: Python :: 3
Topic :: Software Development
Topic :: Home Automation
Topic :: System :: Hardware
"""

from setuptools import setup, Extension

setup(name             = 'NPi.GPIO',
      version          = __version__,
      author           = 'Tungsteno',
      author_email     = 'contacts00-npigpio@yahoo.it',
      description      = 'A module to control NanoPi GPIO channels',
      long_description = open('README.md').read(),
      long_description_content_type = 'text/markdown',
      license          = 'MIT',
      keywords         = 'NanoPi GPIO',
      url              = 'https://github.com/Tungsteno74/NPi.GPIO',
      classifiers      = list(filter(None, classifiers.split('\n'))),
      packages         = ['NPi', 'NPi.GPIO'],
      ext_modules      = [Extension('NPi._GPIO', ['source/py_gpio.c', 'source/c_gpio.c', 'source/cpuinfo.c', 
                                                 'source/event_gpio.c', 'source/soft_pwm.c', 'source/py_pwm.c', 
                                                 'source/common.c', 'source/constants.c', 
                                                 'source/boardtype_friendlyelec.c'])],
      data_files       = [('/NPi' , ['LICENSE', 'README.md', 'CHANGELOG.txt'])])
