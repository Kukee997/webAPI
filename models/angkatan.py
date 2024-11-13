from . import db

class Angkatan(db.Model):
    __tablename__ = 'angkatan'
    id = db.Column(db.Integer, primary_key=True)
    tahun = db.Column(db.String(4), nullable=False)

    # Definisikan relationship
    mahasiswa = db.relationship('Mahasiswa', back_populates='angkatan')