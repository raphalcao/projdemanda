from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)


class GerenciamentoUsuario(BaseUserManager):
    def create(self, email, password, validaAdmin=False, validaAnunciante=False):
        if not email:
            raise ValueError("É necessário possuir um email.")

        if not password:
            raise ValueError("É necessário possuir uma senha.")

        user = self.model(email=self.normalize_email(email))

        user.admin = validaAdmin
        user.anunciante = validaAnunciante
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        user = self.create(email, password, validaAdmin=True, validaAnunciante=True)

        return user

# Create your models here.


class User(AbstractBaseUser):
    email = models.CharField(max_length=255, unique=True)
    nomeCompleto = models.CharField(max_length=100)
    telefone = models.CharField(max_length=50, null=True, unique=True, default=None)
    admin = models.BooleanField(default=False)
    anunciante = models.BooleanField(default=False)

    objects = GerenciamentoUsuario()

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def anunciante(self):
        return self.anunciante

    @property
    def admin(self):
        return self.admin

    USERNAME_FIELD = 'email'


class Endereco(models.Model):
    cep = models.CharField(max_length=11)
    endereco = models.CharField(max_length=255)
    numero = models.IntegerField()
    complemento = models.CharField(max_length=255, null=True)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=2)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return "{} nº{}, {} - {} - {} - {}".format(self.endereco, self.numero, self.complemento, self.cep, self.cidade,
                                                   self.estado)


class Demanda(models.Model):
    descricao = models.TextField()
    endereco = models.ForeignKey(Endereco, on_delete=models.CASCADE, null=False, blank=False)
    anunciante = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)
    finalizado = models.BooleanField(default=False)

    def __str__(self):
        self.format = "{} ".format(self.descricao)

