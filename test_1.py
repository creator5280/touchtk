import unittest
import touchtk as etk


class TestRootWidget(unittest.TestCase):

    def test_one_instance_possible(self):
        try:
            root1 = etk.Root()
            self.assertTrue(True, "Can instantiate one Root object")
        except TypeError:
            self.assertTrue(False, "Cannot instantiate one Root object")

    def test_des_allows_one_instance(self):
        root1 = etk.Root()
        del root1

        try:
            root2 = etk.Root()
            self.assertTrue(True, "Can instantiate one Root object")
        except TypeError:
            self.assertTrue(False, "Cannot instantiate one Root object")

    def test_multi_instance_blocked(self):
        try:
            root1 = etk.Root()
            root2 = etk.Root()
            self.assertFalse(True, "Can instantiate multiple Root objects! Only one should be allowed")
        except TypeError:
            self.assertFalse(False, "Cannot instantiate multiple Root Objects.")


if __name__ == '__main__':
    unittest.main()

