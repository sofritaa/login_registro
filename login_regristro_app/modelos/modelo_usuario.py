from login_regristro_app.config.mysqlconnection import connectToMySQL
from login_regristro_app import BASE_DATOS, EMAIL_REGEX, NOMBRE_REGEX
from flask import flash


class Usuario:
    def __init__(self, data):
        self.id = data['id']
        self.nombre = data['nombre']
        self.apellido = data['apellido']
        self.email = data['email']
        self.password = data['password']
        self.fecha_creacion = data['fecha_creacion']
        self.fecha_actualizacion = data['fecha_actualizacion']
        
    @classmethod
    def crear_uno(cls, data):
        query = '''
                INSERT INTO usuario (nombre, apellido, email, password)
                VALUES (%(nombre)s, %(apellido)s, %(email)s, %(password)s);
                '''
        resultado = connectToMySQL(BASE_DATOS).query_db(query, data)        
        return resultado

    @classmethod
    def obtener_uno_con_email(cls, email):
        query = '''
                SELECT *
                FROM usuario
                WHERE email = %(email)s;
                '''
        resultado = connectToMySQL(BASE_DATOS).query_db(query, {'email': email})        
        if len(resultado) == 0:
            return None
        else:
            return Usuario(resultado[0])

    @staticmethod
    def validar_registro(data):
        es_valido = True
        if len(data['nombre']) < 2:
            es_valido = False
            flash('Tu nombre debe contener al menos 2 caracteres.', 'error_nombre')
                
        if not NOMBRE_REGEX.match(data['nombre']):
            es_valido = False
            flash('Por favor, proporciona un nombre válido (solo letras).', 'error_nombre')
            
        if not NOMBRE_REGEX.match(data['apellido']):
            es_valido = False
            flash('Por favor, proporciona un apellido válido (solo letras).', 'error_apellido')
                    
        if not EMAIL_REGEX.match(data['email']):
            es_valido = False
            flash('Por favor, proporciona un correo electrónico válido.', 'error_email')
                
        if len(data['password']) < 8:
            es_valido = False
            flash('La contraseña debe tener al menos 8 caracteres.', 'error_password')
                
        if data['password'] != data['confirmacion_password']:
            es_valido = False
            flash('Las contraseñas no coinciden.', 'error_password')
                    
        return es_valido

@classmethod
def getEmail(cls, data):
        query = """
        SELECT * FROM users WHERE email = %(email)s;
        """
        resultado = connectToMySQL('bd_login_registro').query_db(query, data)
        print(resultado, "/="*5)
        return resultado