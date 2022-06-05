from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('email is must')

        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(max_length=50, unique=True)  # unique=trueで重複させない
    is_active = models.BooleanField(default=True)  # ログインを許可
    is_staff = models.BooleanField(default=False)

    objects = UserManager()  # ネストしたクラスUserクラスからUserManagerのメソッドを使える。

    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email