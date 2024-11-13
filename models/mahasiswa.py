from . import db

class Mahasiswa(db.Model):
    __tablename__ = 'mahasiswa'  # Nama tabel mahasiswa

    id = db.Column(db.Integer, primary_key=True)
    nama = db.Column(db.String(100), nullable=False)
    nim = db.Column(db.String(20), nullable=False)
    angkatan_id = db.Column(db.Integer, db.ForeignKey('angkatan.id'), nullable=False)
    program_studi_id = db.Column(db.Integer, db.ForeignKey('program_studi.id'), nullable=False)

    angkatan = db.relationship('Angkatan', backref='mahasiswa_list', lazy=True)
    program_studi = db.relationship('ProgramStudi', backref='mahasiswa_list', lazy=True)

    def __repr__(self):
        return f'<Mahasiswa {self.nama}>'