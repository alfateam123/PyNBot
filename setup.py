#from distutils.core import setup
from setuptools import setup

setup(
    name='PyNBot',
    version='0.1.0',
    author='nicolapcweek94',
    #packages=['src'],
    url='http://github.com/nicolapcweek94/PyNBot',
    description='Python [N]wa Telegram bot',
    long_description=open('README.md').read(),
    install_requires=[
        "pyTelegramBotAPI",
        "pylast"
    ],
    #extras_require={
    #        "test": ["pep8", "nose", "mockfs", "coverage"]
    #},
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "Topic :: Communications :: Chat",
    ],
    #test_suite="tests",
    scripts=['src/pynbot.py']
)
