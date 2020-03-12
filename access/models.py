from django.db import models
from django.utils.translation import ugettext as _
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)


# class Role(models.Model):
#     '''
#        Table des rôles
#     '''
#     name = models.CharField(max_length=125)
#     description = models.CharField(max_length=125,null=True,blank=True)

#     created = models.DateTimeField(verbose_name=_('Created'),auto_now_add=True)
#     updated = models.DateTimeField(verbose_name=_('Updated'),auto_now=True)


#     class Meta:
#         verbose_name = _('Role')
#         verbose_name_plural = _('Roles')
#         ordering = ['name','created']


#     def __str__(self):
#         return self.name


class UserManager(BaseUserManager):
    def create_user(self, email, role, password=None):
        """
        Creates and saves a User with the given email, Role
         and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            role=role,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, role, password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            password=password,
            role=role,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    ROLE_CHOICES = (
        ('DG', 'DG'),
        ('COO', 'COO'),
        ('COE', 'COE'),
        ('DRH', 'DRH'),
        ('Manager', 'Manager'),
        ('Developper', 'Developper'),
        ('Commercial(e)', 'Commercial(e)'),
        ('Autres', 'Autres'),
    )
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    bio = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['role']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin