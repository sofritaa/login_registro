from flask import Flask
import re

app = Flask(__name__)
app.secret_key = 'esto es secreto'
BASE_DATOS = "bd_login_registro"
EMAIL_REGEX = re.compile(r'^[\w\.-]+@[\w\.-]+\.\w+$')
NOMBRE_REGEX = re.compile(r'^[A-Za-záéíóúÁÉÍÓÚñÑ\s]+$')
