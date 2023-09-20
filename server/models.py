from flask_sqlalchemy import SQLAlchemy
from flask_sqlalchemy import db

class Owner(db.Model):
    __tablename__ = 'owners'

    id = db.Column(db.Integer, primary_key = True)
    name = db.column(db.string, unique = True)

    pets = db.relationship('pet', backref = 'owner')

    def __repr__(self):
        return f'<Pet owner {self.name}>'
    
class Pet(db.Model):
    __tablename__ = 'pets'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.string)
    species = db.Column(db.string)

    owner_id = db.Column(db.Integer, db.ForeignKey('owners.id'))

    def __repr__(self):
        return f'<Pet {self.name}, {self.species}>'
    
db.create_all() 
app.run()

    

            

