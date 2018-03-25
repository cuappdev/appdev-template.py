import datetime as dt
from flask import json
from tests.test_case import *

class DemoTest(TestCase):
  def basic_test(self):
    self.assertEquals(1, 1)
