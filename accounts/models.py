from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.
class MyAccountManager(BaseUserManager):

    def create_user(self, first_name, last_name, username, email, password=None):
        if not email:
         raise ValueError('el usuario debe tener email')  # Verifica si el email no está vacío y lanza un ValueError si lo está
        if not username:
            raise ValueError('El usuario debe tener un username')  # Verifica si el username no está vacío y lanza un ValueError si lo está
    
        user = self.model(
            email=self.normalize_email(email),  # Normaliza el email (lo convierte a minúsculas, por ejemplo)
            username=username,  # Asigna el valor del username al atributo correspondiente del modelo de usuario
            first_name=first_name,  # Asigna el valor del primer nombre al atributo correspondiente del modelo de usuario
            last_name=last_name,  # Asigna el valor del apellido al atributo correspondiente del modelo de usuario
        )

        user.set_password(password)  # Establece la contraseña del usuario utilizando el método set_password de Django
        user.save(using=self._db)  # Guarda el usuario en la base de datos utilizando el objeto Manager y la base de datos especificada

        return user  # Devuelve el usuario creado

    def create_superuser(self, first_name, last_name, email, username, password):
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name,
        )

        user.is_admin = True  # Establece el atributo 'is_admin' en True para indicar que el usuario es un administrador
        user.is_active = True  # Establece el atributo 'is_active' en True para activar la cuenta del usuario
        user.is_staff = True  # Establece el atributo 'is_staff' en True para indicar que el usuario es parte del personal
        user.save(using=self._db)  # Guarda el usuario en la base de datos utilizando el objeto Manager y la base de datos especificada

        return user  # Devuelve el usuario creado como superusuario





class Account(AbstractBaseUser):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique=True)
    email = models.CharField(max_length=100, unique=True)
    phone = models.CharField(max_length=50)

    #campos atributos de django
    date_joined = models.DateTimeField(auto_now_add=True)  # Fecha y hora en la que se unió el usuario
    last_login = models.DateTimeField(auto_now_add=True)  # Fecha y hora del último inicio de sesión
    is_admin = models.BooleanField(default=False)  # Indica si el usuario es administrador
    is_staff = models.BooleanField(default=False)  # Indica si el usuario es personal de staff
    is_active = models.BooleanField(default=False)  # Indica si la cuenta del usuario está activa
    is_superadmin = models.BooleanField(default=False)  # Indica si el usuario es un superadministrador

    USERNAME_FIELD = 'email'  # Indica que el campo utilizado para el inicio de sesión es el correo electrónico

    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']  # Indica los campos adicionales requeridos

    objects = MyAccountManager()

    def __str__(self):
        return self.email  # Devuelve la dirección de correo electrónico como representación en forma de cadena del objeto de usuario

    def has_perm(self, perm, obj=None):
        return self.is_admin  # Verifica si el usuario tiene el permiso especificado basándose en el atributo 'is_admin'

    def has_module_perms(self, add_label):
        return True
