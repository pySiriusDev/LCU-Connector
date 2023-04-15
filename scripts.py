from tests import *
import os


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def run_tests():
    clear_screen()
    print('Starting tests...')
    connection_test.request_test()
    print('No errors found.')


def build_docs():
    clear_screen()
    print('\n\nBuilding docs...')
    os.system('sphinx-build -b html source build')


def build():
    os.system('python setup.py sdist')
