from Project.models import Project
from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import (
                                    AbstractBaseUser,
                                    BaseUserManager,
                                    )
from django.db.models.deletion import CASCADE


class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Vous devez entrer un email.')

        user_obj = self.model(
                        email=self.normalize_email(email),
                        )
        user_obj.set_password(password)
        user_obj.save()
        return user_obj

    def create_superuser(self, email, password, **extra_fields):
        user = self.create_user(email=email,
                                password=password,
                                )
        user.is_admin = True
        user.is_staff = True
        user.save()
        return user


class User(AbstractBaseUser, PermissionsMixin):

    first_name = models.CharField(max_length=128, blank=True)
    last_name = models.CharField(max_length=128, blank=True)
    email = models.EmailField(blank=False, unique=True)
    password = models.CharField(max_length=255, blank=False)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def get_full_name(self):
        full_name = f"{self.first_name} {self.last_name}"
        return full_name.strip()

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    def __str__(self):
        return self.email

    def save(self, *args, **kwargs):
        super(User, self).save(*args, **kwargs)
        return self


class Contributor(models.Model):
    user = models.ForeignKey(User,
                             on_delete=CASCADE,
                             related_name='user_contributor')
    project = models.ForeignKey(Project,
                                on_delete=CASCADE,
                                related_name='project_contributor')

    def __str__(self):
        return f'{self.user}'
