# flake8: noqa
import string


class LoginInterface:
    _registered_users = []

    @classmethod
    def _check_if_password_is_common(cls, passwd: str):
        most_common_passwd = [
            '123456789', '12345678', 'password', 'qwerty12', 'chess123',
            '87654321', 'abcdefgh', 'zxcvbnm,', '11111111', '22222222',
            '33333333', '44444444', '66666666', '77777777', '88888888',
            '99999999', '00000000',
        ]
        return True if passwd not in most_common_passwd else False

    @classmethod
    def _check_if_passwd_has_any_special_characters(cls, passwd: str):
        return True if (
            '!' in passwd
            or '@' in passwd
            or '#' in passwd
            or '$' in passwd
            or '%' in passwd
            or '&' in passwd
            or '*' in passwd
        ) else False

    @classmethod
    def _check_if_user_name_already_exists(cls, username: str):
        return True if username not in [user['username'] for user in cls._registered_users] else False

    @classmethod
    def _check_if_passwd_has_numerical_characters(cls, passwd: str):
        for i in passwd:
            for j in string.digits:
                if j == i:
                    return True
        return False

    @classmethod
    def _check_uppercase_characters_existence(cls, passwd: str):
        for i in passwd:
            for j in string.ascii_uppercase:
                if j == i:
                    return True
        return False

    @classmethod
    def _check_if_username_exists_in__registered_users_of_this_class(cls, username: str):
        for user in cls._registered_users:
            if user['username'] == username:
                return True
        return False

    @classmethod
    def _check_if_user_match_with_the_password(cls, username: str, old_password: str):
        usr = [u for u in cls._registered_users if u['username'] == username]
        
        return True if usr[0]['password'] == old_password else False


    def create_user(username: str, passwd: str, passwdconfirm: str):
        assert not isinstance(username, None | int | float), 'User Data Error: username cant be a None value.'
        assert passwd == passwdconfirm, 'Password error: passwords dont confirm.'
        assert len(passwd) >= 8, 'Password error: too short.'
        assert __class__._check_if_password_is_common(passwd) is True, 'Password error: password too common.'
        assert __class__._check_if_passwd_has_any_special_characters(passwd) is True, 'Password error: password too weak.'
        assert __class__._check_if_user_name_already_exists(username), 'User error: username already exists.'
        assert __class__._check_if_passwd_has_numerical_characters(passwd), 'Password error: missing any numerical character.'
        assert __class__._check_uppercase_characters_existence(passwd), 'Password error: missing any uppercase character.'

        user = {
            'username': username,
            'password': passwd,
        }

        __class__._registered_users.append(user)

        return user
    
    def change_password(user: str, passwd: str, new_passwd: str):
        assert __class__._check_if_username_exists_in__registered_users_of_this_class(user), 'User error: not found.'
        assert __class__._check_if_user_match_with_the_password(user, passwd), 'Password error: user and old password dont match.'
        _user = dict([u for u in __class__._registered_users if u['username'] == user])

        _user['password'] = new_passwd
        return True


if __name__ == '__main__':
    ...
