import unittest

import sys
import os

from pathlib import Path

class MyTestCase(unittest.TestCase):
  def test_sys_checker(self):
    print(sys.path)
    print(len(sys.path)) #9
    # automatically already in... webstorm option to append to $PYTHONPATH for both source and current folder
    # py3-folder-path/test
    # py3-folder-path/venv/lib/python3.9/site-packages


    # namespace folder in pycharm?
    self.assertEqual(True, True)  # add assertion here
  def test_sys_path_import(self):
    # https: // stackoverflow.com / questions / 918154 / relative - paths - in -python
    mod_path = Path(__file__).parent
    # relative_path_1='../a/b'
    relative_path_1='../a'
    src_path_1 = (mod_path / relative_path_1).resolve()
    # print(src_path_1.absolute())
    print(src_path_1)
    self.assertEqual(os.path.isdir(src_path_1), True)  # add assertion here
    self.assertEqual(len(sys.path), 9)  # add assertion here
    sys.path.append(str(src_path_1))
    self.assertEqual(len(sys.path), 10)  # add assertion here
    print(sys.path)
    # works but ide doesnt know...
    from b.b1 import hello_world
    hello_world()
    self.assertEqual(True, True)  # add assertion here

  def test_sites(self):
    # https: // stackoverflow.com / questions / 918154 / relative - paths - in -python
    # https: // stackoverflow.com / questions / 9554087 / setting - an - environment - variable - in -virtualenv
    # cat $VIRTUAL_ENV/bin/postactivate
    # cat $VIRTUAL_ENV/bin/predeactivate
    import site
    print(site.ENABLE_USER_SITE) # false, venv/pyvenv.cfg...
    print(site.USER_BASE)
    print(site.USER_SITE)
    print('hi')
    # mod_path = Path(__file__).parent
    # # relative_path_1='../a/b'
    # relative_path_1 = '../a'
    # src_path_1 = (mod_path / relative_path_1).resolve()
    # # print(src_path_1.absolute())
    # print(src_path_1)
    # self.assertEqual(os.path.isdir(src_path_1), True)  # add assertion here
    # self.assertEqual(len(sys.path), 9)  # add assertion here
    # sys.path.append(str(src_path_1))
    # self.assertEqual(len(sys.path), 10)  # add assertion here
    # print(sys.path)
    # # works but ide doesnt know...
    # from b.b1 import hello_world
    # hello_world()
    # self.assertEqual(True, True)  # add assertion here

  # https://docs.python.org/3/tutorial/venv.html#tut-venv
  # seems easier
  # pyvenv.cfg?

  # pip install --editable



if __name__ == '__main__':
  unittest.main()
