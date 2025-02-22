from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager
from uploader.models import Image

class Usuario(AbstractUser):
    class TipoUsuario(models.IntegerChoices):
        CLIENTE = 1, "Cliente"
        VENDEDOR = 2, "Vendedor"
        GERENTE = 3, "Gerente"

    username = None
    email = models.EmailField(_("e-mail address"), unique=True)
    cpf = models.CharField(_("CPF"), max_length=11, blank=True, null=True)
    telefone = models.CharField(_("Phone"), max_length=11, blank=True, null=True)
    data_nascimento = models.DateField(
        _("Birth Date"), auto_now=False, auto_now_add=False, blank=True, null=True
    )
    foto = models.ForeignKey(
        Image, 
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        default=None
    )

    tipo_usuario = models.IntegerField(choices=TipoUsuario.choices, default=TipoUsuario.CLIENTE)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    EMAIL_FIELD = "email"

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"
        ordering = ["-date_joined"]
