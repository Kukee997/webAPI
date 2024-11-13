from flask import Blueprint, request, jsonify, render_template
from models.mahasiswa import Mahasiswa
from models import db

mahasiswa_bp = Blueprint('mahasiswa', __name__)

@mahasiswa_bp.route('/mahasiswa', methods=['GET', 'POST'])
def handle_mahasiswa():
    if request.method == 'GET':
        mahasiswa_list = Mahasiswa.query.all()
        result = [
            {
                'id': m.id,
                'nama': m.nama,
                'nim': m.nim,
                'angkatan': m.angkatan.tahun if m.angkatan else None,
                'program_studi': m.program_studi.program_studi if m.program_studi else None  # Pastikan ini sesuai
            }
            for m in mahasiswa_list
        ]
        return jsonify(result)
    
    if request.method == 'POST':
        data = request.json
        new_mahasiswa = Mahasiswa(
            nama=data['nama'],
            nim=data['nim'],
            angkatan_id=data['angkatan_id'],
            program_studi_id=data['program_studi_id']  # Pastikan ini sesuai
        )
        db.session.add(new_mahasiswa)
        db.session.commit()
        return jsonify({
            'message': 'Mahasiswa berhasil ditambahkan',
            'data': {
                'id': new_mahasiswa.id,
                'nama': new_mahasiswa.nama,
                'nim': new_mahasiswa.nim
            }
        }), 201

@mahasiswa_bp.route('/mahasiswa/view', methods=['GET'])
def view_mahasiswa():
    mahasiswa_list = Mahasiswa.query.all()
    
    # Mengirimkan data mahasiswa ke template
    return render_template('mahasiswa.html', mahasiswa=mahasiswa_list)

@mahasiswa_bp.route('/mahasiswa/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def handle_mahasiswa_by_id(id):
    mahasiswa = Mahasiswa.query.get_or_404(id)
    
    if request.method == 'GET':
        return jsonify({
            'id': mahasiswa.id,
            'nama': mahasiswa.nama,
            'nim': mahasiswa.nim,
            'angkatan': mahasiswa.angkatan.tahun if mahasiswa.angkatan else None,
            'program_studi': mahasiswa.program_studi.program_studi if mahasiswa.program_studi else None  # Pastikan ini sesuai
        })
    
    if request.method == 'PUT':
        data = request.json
        mahasiswa.nama = data.get('nama', mahasiswa.nama)
        mahasiswa.nim = data.get('nim', mahasiswa.nim)
        mahasiswa.angkatan_id = data.get('angkatan_id', mahasiswa.angkatan_id)
        mahasiswa.program_studi_id = data.get('program_studi_id', mahasiswa.program_studi_id)
        db.session.commit()
        return jsonify({'message': 'Data mahasiswa berhasil diperbarui'})
    
    if request.method == 'DELETE':
        db.session.delete(mahasiswa)
        db.session.commit()
        return jsonify({'message': 'Data mahasiswa berhasil dihapus'})