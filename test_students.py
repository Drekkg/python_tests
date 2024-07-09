import unittest
from students import Student


class TestStudent(unittest.TestCase):
    def setUp(self):
        print("setUp")
        self.student = Student('Les', 'Claypool')

    def tearDown(self):
        print("tearDown")

    def test_full_name(self):
        print("test full name")
        self.assertEqual(self.student.full_name, 'Les Claypool')

    def test_alert_santa(self):
        print("test naughty list")
        self.student.alert_santa()

        self.assertTrue(self.student.naughty_list)

    def test_email(self):
        print("test email")
        self.assertEqual(self.student.email, 'les.claypool@email.com')


if __name__ == '__main__':
    unittest.main()
