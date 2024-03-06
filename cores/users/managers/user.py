from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):

    def create_superuser(self, username, email=None, password=None, **extra_field):
        extra_field.setdefault('is_staff', True)
        extra_field.setdefault('is_superuser', True)

        return self.create_user(username, email, password, **extra_field)

    def create_user(self, email, username=None, password=None, **extra_field):
        if not username:
            raise ValueError('The username field must set')

        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_field)
        user.set_password(password)
        user.save(using=self.db)

        return user
