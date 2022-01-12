import unittest
import z2 as employee


class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.employee = employee.Employee("Adam", "Karolczak", 150000)

    def test_give_default_raise(self):  # nazwy muszą zaczynać się od test
        self.employee.give_raise()
        self.assertEqual(self.employee.annual_salary, 152000)

    def test_give_custom_raise(self):
        self.employee.give_raise(500)
        self.assertEqual(self.employee.annual_salary, 150500)
        self.employee.give_raise(-499.5)
        self.assertEqual(self.employee.annual_salary, 150000.5)
        self.assertRaises(TypeError, self.employee.give_raise, "1010")
        with self.assertRaises(TypeError):
            self.employee.give_raise("123")



if __name__ == '__main__':
    unittest.main()
