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

  # added init in a... didnt do anything
  # https://stackoverflow.com/questions/1260792/import-a-file-from-a-subdirectory
  # workspace file?
  def test_a_init(self):
    from b.b1 import hello_world
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

  # pip install --editable a # need setup.py
  # need name, version, url...
  # difference between Dist and Packages
  # pip install --editable --file-links file://~/PycharmProjects/py3-folder-path/a # doesnt work evn with full path
  # pip install --editable --file-links a
  # pip uninstall a

  # https://virtualenvwrapper.readthedocs.io/en/latest/
  # virtualenvwrapper
  # https://stackoverflow.com/questions/9554087/setting-an-environment-variable-in-virtualenv

  def test_virt_env(self):
    import re
    PYTHONPATH = os.environ.get("PYTHONPATH")

    print('py:', PYTHONPATH) # doesnt search... when added to venv? why
    print('py:', re.search('/py3-folder-path/a', PYTHONPATH))
    # from a.b.b1 import hello_world
    from b.b1 import hello_world # add to sources in python project struct
    hello_world()


if __name__ == '__main__':
  unittest.main()
