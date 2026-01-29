from wtforms import Form
from wtforms import StringField, PasswordField, IntegerField, PasswordField, FloatField
from wtforms import validators
from wtforms import EmailField

class UserForm(Form):
    matricula=IntegerField('Matricula',[
        validators.DataRequired(message="El campo es requerido."),
        validators.NumberRange(min=100, max=1000, message="Ingrese valor valido.")
    ])
    nombre=StringField('Nombre',[
        validators.DataRequired(message="El campo es requerido."),
        validators.length(min=4, max=10, message="Ingrese nombre valido.")
    ])
    apePaterno=StringField('Apellido Paterno',[
        validators.DataRequired(message="El campo es requerido.")
    ])
    apeMaterno=StringField('Apellido Materno',[
        validators.DataRequired(message="El campo es requerido.")
    ])
    correo=EmailField('Correo',[
        validators.Email(message="Ingresa un correo valido")
    ])    