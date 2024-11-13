from flask import Flask
from models import db
from controllers.mahasiswa_controller import mahasiswa_bp
from controllers.program_studi_controller import program_studi_bp
from controllers.angkatan_controller import angkatan_bp
from config import Config  # Import konfigurasi

app = Flask(__name__)
app.config.from_object(Config)  # Memuat konfigurasi dari kelas Config


db.init_app(app)


with app.app_context():
    db.create_all()


app.register_blueprint(mahasiswa_bp)
app.register_blueprint(program_studi_bp)
app.register_blueprint(angkatan_bp)

if __name__ == '__main__':
    app.run(debug=True)