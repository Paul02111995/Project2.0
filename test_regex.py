import unittest
from regex import is_passport_valid, is_inn_number_valid, is_car_number_valid


class TestValidationFunctions(unittest.TestCase):
    def test_passport_number(self):
        self.assertTrue(is_passport_valid("КМ884422"))
        self.assertFalse(is_passport_valid("123456"))

    def test_inn_number(self):
        self.assertTrue(is_inn_number_valid("1234567894"))
        self.assertFalse(is_inn_number_valid("12345L"))

    def test_car_number(self):
        self.assertTrue(is_car_number_valid("РР1234АА"))
        self.assertTrue(is_car_number_valid("МI5678KK"))
        self.assertTrue(is_car_number_valid("ХХ9102ББ"))
        self.assertTrue(is_car_number_valid("ЕХ3456ГГ"))
        self.assertFalse(is_car_number_valid("АБ1234CD"))

if __name__ == "__main__":
    unittest.main()
