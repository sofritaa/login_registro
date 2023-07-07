from flask import session, render_template, redirect, request, flash
from flask_bcrypt import Bcrypt
from login_regristro_app import app
from login_regristro_app.modelos.modelo_usuario import Usuario

bcrypt = Bcrypt(app)

@app.route('/', methods=['GET'])
def desplegar_login_registro():
    return render_template('login_registro.html')

@app.route('/crear/usuario', methods=['POST'])
def nuevo_usuario():
    data = dict(request.form)

    if Usuario.validar_registro(data) == False:
        return redirect('/')
    else:
        password = data['password']
        password_encriptado = bcrypt.generate_password_hash(password).decode('utf-8')
        data['password'] = password_encriptado
        id_usuario = Usuario.crear_uno(data)
        session['nombre'] = data['nombre']
        session['apellido'] = data['apellido']
        session['id_usuario'] =  id_usuario
        
        return redirect('/dashboard')

@app.route('/dashboard', methods=['GET'])
def desplegar_dashboard():
    return render_template('dashboard.html')

@app.route('/login', methods=['POST'])
def procesa_login():
    email = request.form.get('email_login')
    
    usuario = Usuario.obtener_uno_con_email(email)

    if usuario == None:
        flash("Email inválido", "error_email_login")
        return redirect('/')
    else:
        if not bcrypt.check_password_hash( usuario.password, request.form['password_login'] ):
            flash("Contraseña incorrecta", 'error_password_login')
            return redirect('/')
        else:
            session['nombre'] = usuario.nombre
            session['apellido'] = usuario.apellido
            session['id_usuario'] = usuario.id
            return redirect('/dashboard')

@app.route('/logout', methods=['GET', 'POST'])
def procesa_logout():
    session.clear()
    return redirect('/')
