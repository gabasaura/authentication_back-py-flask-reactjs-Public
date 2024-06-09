from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()



class User(db.Model):
    """
    Tabla correspondiente a los usuarios
    """
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    password = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    active = db.Column(db.Boolean, default=True)
    admin = db.Column(db.Boolean, default=False)

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "admin": self.admin
        }

    def save(self):
        db.session.add(self)
        db.session.commit()

    
