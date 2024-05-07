from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):

    def create_superuser(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(username, email, password, **extra_fields)

    def create_user(self, email, username=None, password=None, **extra_fields):
        if not username:
            raise ValueError('The username field must set')

        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self.db)

        return user
