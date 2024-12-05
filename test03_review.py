import pytest

class Testadd(object):
    def setup_method(self):
        print("--setup---")
    def teardown_method(self):
        print("----teardown----")
    def setup_class(self):
        print("==setup class===")
    def teardown_class(self):
        print("===teardown class===")
    def test_add(self):
        print("test one passed")
    def test_add2(self):
        print("test two passed")
