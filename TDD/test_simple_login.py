# flake8: noqa
import unittest
from simple_login_logic import LoginInterface


class TestLoginInteface(unittest.TestCase):
    def test_create_user_raises_user_name_cant_be_a_none_value(self):
        with self.assertRaises(Exception) as ex:
            LoginInterface.create_user(None, 'pass', 'pass')
        self.assertEqual(ex.exception.args[0], 'User Data Error: Username cant be a None value.')

    def test_if_passwd_and_passwd_confirm_are_equals_raises_an_password_error(self):
        with self.assertRaises(Exception) as ex:
            LoginInterface.create_user('Well', 'pass1', 'pass2')
        self.assertEqual(ex.exception.args[0], 'Password error: Passwords dont confirm.')

    def test_password_length_raises_an_length_error(self):
        with self.assertRaises(Exception) as ex:
            LoginInterface.create_user('Foo', 'p1', 'p1')
        self.assertEqual(ex.exception.args[0], 'Password error: too short.')
    
    def test_if_password_is_strong_enough_raises_an_password_error(self):
        with self.assertRaises(Exception) as ex:
            LoginInterface.create_user('Foo', '12345678', '12345678')
        self.assertEqual(ex.exception.args[0], 'Password error: Password too common.')
    
    def test_username_existence_raises_an_username_already_exists(self):
        with self.assertRaises(Exception) as ex:
            LoginInterface.create_user('Foo', 'strRong%p4$$wD', 'strRong%p4$$wD')
            LoginInterface.create_user('Foo', 'strRong%p4$$wD', 'strRong%p4$$wD')
        self.assertEqual(ex.exception.args[0], 'User error: Username already exists.')

    # TODO: digits in password
    # TODO: upercase characters in password
    # TODO: change password test

if __name__ == '__main__':
    unittest.main(verbosity=2)
