from django.db import models
from django.contrib.auth.models import AbstractUser
from models_manager.models import Account

# Create your models here.

class SystemUser(AbstractUser):
    account = models.OneToOneField(Account, null=True, on_delete=models.CASCADE, verbose_name="Аккаунт")

    def __str__(self):
        if self.account:
            return " ".join([self.account.firstname, self.account.lastname, self.account.patronymic])
        return " ".join([self.first_name, self.last_name])

    class Meta:
        verbose_name = 'Пользователь системы'
        verbose_name_plural = 'Пользователи системы'    