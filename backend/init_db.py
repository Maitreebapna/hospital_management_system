import os
from dotenv import load_dotenv
from flask import Flask
from werkzeug.security import generate_password_hash
from models import db, User, Role

load_dotenv()

# Initialize Flask app for database setup
app = Flask(__name__)
database_url = os.getenv('DATABASE_URL') or 'sqlite:///hms.db'
if database_url.startswith('postgres://'):
    database_url = database_url.replace('postgres://', 'postgresql://', 1)
app.config['SQLALCHEMY_DATABASE_URI'] = database_url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['SECURITY_PASSWORD_SALT'] = os.getenv('SECURITY_PASSWORD_SALT')

db.init_app(app)

def setup_database():
    with app.app_context():
        db.create_all()
        
        roles = ['Admin', 'Doctor', 'Patient']
        for role_name in roles:
            role = Role.query.filter_by(name=role_name).first()
            if not role:
                role = Role(name=role_name, description=f'{role_name} privileges')
                db.session.add(role)
        db.session.commit()

        admin_role = Role.query.filter_by(name='Admin').first()
        admin_user = User.query.filter_by(email='admin@hms.com').first()
        
        if not admin_user:
            admin_password = os.getenv('INITIAL_ADMIN_PASSWORD')
            if not admin_password:
                raise RuntimeError(
                    'Set INITIAL_ADMIN_PASSWORD before creating the initial admin user.'
                )
            print("Creating default Admin user...")
            admin_user = User(
                username='superadmin',
                email='admin@hms.com',
                password_hash=generate_password_hash(admin_password),
                active=True
            )
            admin_user.roles.append(admin_role)
            db.session.add(admin_user)
            db.session.commit()
            print("Success: Admin user 'superadmin' created programmatically!")
        else:
            print("Admin user already exists. Database is ready.")

if __name__ == '__main__':
    setup_database() 
