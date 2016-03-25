from django.contrib.auth.base_user import BaseUserManager
from gezbackend.utils import get_random_code, get_password

class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, username, email, password, **extra_fields):
        """
        Creates and saves a User with the given username, email and password.
        """
        if not username:
            raise ValueError('The given username must be set')
        email = self.normalize_email(email)
        security = get_random_code(10)
        password = get_password(password, security)
        user = self.model(username=username, email=email, security=security, \
               password=password, **extra_fields)
        user.save(using=self._db)
        return user

    def create_user(self, username, email=None, password=None, **extra_fields):
        return self._create_user(username, email, password, **extra_fields)

    def create_superuser(self, username, email, password, **extra_fields):
        return self._create_user(username, email, password, **extra_fields)