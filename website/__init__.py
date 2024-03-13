from flask import Flask

def creat_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'amz_toolbox_sc_key'
    
    from .views import views
    from .auth import auth
    from .calculator import calculator_bp

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    app.register_blueprint(calculator_bp, url_prefix='/')

    return app