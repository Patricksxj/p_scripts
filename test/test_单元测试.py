from unittest import TestCase
class new_test(TestCase):
    def setUp(self):
        print("Before every test case!")

    def test_case_01(self):
        print("this is test case 1")

    def test_case_02(self):
        print("this is test case 2")