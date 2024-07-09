import unittest
from students import Student
from datetime import timedelta


class TestStudent(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("setup class")

    @classmethod
    def tearDownClass(cls):
        print("teardown class")

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

    def test_apply_extension(self):
        print("test apply_extension")
        old_end_date = self.student.end_date
        self.student.apply_extension(5)
        self.assertEqual(self.student.end_date, old_end_date + timedelta(days=5))  # noqa


if __name__ == '__main__':
    unittest.main()
