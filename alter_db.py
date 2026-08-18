from app import app
from models import db
from sqlalchemy import text

with app.app_context():
    try:
        db.session.execute(text('ALTER TABLE productos ADD COLUMN imagen VARCHAR(255);'))
        db.session.commit()
        print('Columna "imagen" agregada correctamente a la tabla "productos".')
    except Exception as e:
        print('Error:', e)
