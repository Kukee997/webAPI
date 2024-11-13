from . import db


class ProgramStudi(db.Model):
    __tablename__ = 'program_studi'  # Ganti nama tabel di sini

    id = db.Column(db.Integer, primary_key=True)
    program_studi = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f'<ProgramStudi {self.program_studi}>'