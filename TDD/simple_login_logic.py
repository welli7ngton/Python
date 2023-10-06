# flake8: noqa

class LoginInterface:
    _registered_users = []
    def create_user(username: str, passwd: str, passwdconfirm: str):
        assert not isinstance(username, None | int | float), 'User Data Error: Username cant be a None value.'
        assert passwd == passwdconfirm, 'Password error: Passwords dont confirm.'
        assert len(passwd) >= 8, 'Password error: too short.'
        assert __class__.check_if_password_is_common(passwd) is True, 'Password error: Password too common.'
        assert __class__.check_if_passwd_has_any_special_characters(passwd) is True, 'Password error: Password too weak.'
        assert __class__.check_if_user_name_already_exists(username), 'User error: Username already exists.'
        user = {
            'username': username,
            'password': passwd,
        }
        __class__._registered_users.append(user)

        return user

    @classmethod
    def check_if_password_is_common(cls, passwd: str):
        most_common_passwd = [
            '123456789', '12345678', 'password', 'qwerty12', 'chess123',
            '87654321', 'abcdefgh', 'zxcvbnm,', '11111111', '22222222',
            '33333333', '44444444', '66666666', '77777777', '88888888',
            '99999999', '00000000',
        ]
        return True if passwd not in most_common_passwd else False

    @classmethod
    def check_if_passwd_has_any_special_characters(cls, passwd: str):
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
    def check_if_user_name_already_exists(cls, username: str):
        return True if username not in [user['username'] for user in cls._registered_users] else False
