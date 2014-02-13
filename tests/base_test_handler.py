import unittest
import webtest

from google.appengine.ext import testbed

import main

class TestHandler(unittest.TestCase):
  '''
  a useful class that other tests can inherit
  '''

  def setUp(self):
    self.testbed = testbed.Testbed()
    self.testbed.activate() 
    self.testapp = webtest.TestApp(main.app)

  def tearDown(self):
    self.testbed.deactivate()
