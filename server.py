from login_regristro_app import app
from login_regristro_app.controladores import controlador_usuarios

if __name__ == '__main__':
    app.run(debug= True, port= 5001)
    