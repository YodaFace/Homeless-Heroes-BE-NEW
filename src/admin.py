
import os
from flask_admin import Admin
from models import db, Homeless_User, Shelter, Contributor
from flask_admin.contrib.sqla import ModelView

# set optional bootswatch theme

def setup_admin(app):
    # app.secret_key = os.environ.get('FLASK_APP_KEY', 'sample key')
    app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
    admin = Admin(app, name='Homeless Hero', template_mode='bootstrap3')
    # Add administrative views here
    
    
    admin.add_view(ModelView(Homeless_User, db.session))

    admin.add_view(ModelView(Shelter, db.session))

    admin.add_view(ModelView(Contributor, db.session))