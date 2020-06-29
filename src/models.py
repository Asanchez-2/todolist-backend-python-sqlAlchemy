from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Todos(db.Model):
    __tablename__= 'todos'
    id = db.Column(db.Integer, primary_key=True)
    done = db.Column(db.Boolean, nullable=False)
    label = db.Column(db.String(255), unique=True, nullable=False)
    

    def serialize(self):
        return {
            "id":self.id,
            "done": self.done,
            "label": self.label
        }