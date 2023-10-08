# flake8: noqa
import unittest
from simple_login_logic import LoginInterface


class TestLoginInteface(unittest.TestCase):
    def test_create_user_raises_user_name_cant_be_a_none_value(self):
        with self.assertRaises(Exception) as ex:
            LoginInterface.create_user(None, 'pass', 'pass')
        self.assertEqual(ex.exception.args[0], 'User Data Error: username cant be a None value.')

    def test_if_passwd_and_passwdconfirm_are_equals_raises_an_password_error(self):
        with self.assertRaises(Exception) as ex:
            LoginInterface.create_user('Foo', 'pass1', 'pass2')
        self.assertEqual(ex.exception.args[0], 'Password error: passwords dont confirm.')

    def test_password_length_raises_an_password_error(self):
        with self.assertRaises(Exception) as ex:
            LoginInterface.create_user('Foo', 'p1', 'p1')
        self.assertEqual(ex.exception.args[0], 'Password error: too short.')
    
    def test_if_password_is_strong_enough_raises_an_password_error(self):
        with self.assertRaises(Exception) as ex:
            LoginInterface.create_user('Foo', '12345678', '12345678')
        self.assertEqual(ex.exception.args[0], 'Password error: password too common.')
    
    def test_username_existence_raises_an_username_already_exists(self):
        with self.assertRaises(Exception) as ex:
            LoginInterface.create_user('Foo', 'strRong%p4$$wD', 'strRong%p4$$wD')
            LoginInterface.create_user('Foo', 'strRong%p4$$wD', 'strRong%p4$$wD')
        self.assertEqual(ex.exception.args[0], 'User error: username already exists.')
    
    def test_if_passwd_has_any_digit_raises_an_password_error(self):
        with self.assertRaises(Exception) as ex:
            LoginInterface.create_user('Foo', 'testPassword*#', 'testPassword*#')
        self.assertEqual(ex.exception.args[0], 'Password error: missing any numerical character.')
    
    def test_if_passwd_has_any_uppercase_character_raises_an_password_error(self):
        with self.assertRaises(Exception) as ex:
            LoginInterface.create_user('Foo', '1testpassword*#', '1testpassword*#')
        self.assertEqual(ex.exception.args[0], 'Password error: missing any uppercase character.')

    def test_if_user_exists_raises_an_user_error_not_found(self):
        with self.assertRaises(Exception) as ex:
            LoginInterface.change_password('iDontExist', 'Str0ng#P4s$w0rd!', 'n3wStr0ng#P4s$w0rd!')
        self.assertEqual(ex.exception.args[0], 'User error: not found.')
    
    def test_changing_the_password_getting_a_true_value(self):
        LoginInterface.create_user('FooW', 'StrongPassword#3', 'StrongPassword#3')
        self.assertEqual(LoginInterface.change_password('FooW', 'StrongPassword#3', 'n###33WStrongPassword#3'), True)
    
    def test_if_password_match_with_the_user_getting_an_password_error(self):
        with self.assertRaises(Exception) as ex:
            LoginInterface.create_user('Foo', 'StrongPassword#3', 'StrongPassword#3')
            LoginInterface.change_password('Foo', 'otherStr0n6P4$$', 'nE3WStrongPassword#3')
        self.assertEqual(ex.exception.args[0], 'Password error: user and old password dont match.')
    
    def test_checking_the_strength_of_the_new_password_getting_an_weak_password_error(self):
        with self.assertRaises(Exception) as ex:
            LoginInterface.create_user('foo', 'StrongPassword#3', 'StrongPassword#3')
            LoginInterface.change_password('foo', 'StrongPassword#3', 'weakpasswd')
        self.assertEqual(ex.exception.args[0], 'Password error: password too weak.')


if __name__ == '__main__':
    unittest.main(verbosity=2)
