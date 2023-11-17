from django.apps import AppConfig


class UserConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'user'


# https://github.com/veryacademy/YT-Django-User-Auth/blob/master/login/apps.py :
# class LoginConfig(AppConfig): 
#     name = 'login'
