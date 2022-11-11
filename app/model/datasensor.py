from app import db
from datetime import datetime

class Datasensor(db.Model):
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    temp = db.Column(db.String(60), nullable=False)
    hum = db.Column(db.String(60), nullable=False)
    telur = db.Column(db.String(60), nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Datasensor {}>'.format(self.name)
