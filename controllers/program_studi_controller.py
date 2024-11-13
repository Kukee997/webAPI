from flask import Blueprint, request, jsonify, render_template  # Import render_template
from models.program_studi import ProgramStudi  # Pastikan ini tetap
from models import db

program_studi_bp = Blueprint('program_studi', __name__)

@program_studi_bp.route('/program_studi', methods=['GET', 'POST'])
def handle_program_studi():
    if request.method == 'GET':
        program_studi_list = ProgramStudi.query.all()
        result = [{'id': ps.id, 'program_studi': ps.program_studi} for ps in program_studi_list]
        return jsonify(result)
    
    if request.method == 'POST':
        data = request.json
        if 'program_studi' not in data:
            return jsonify({'message': 'Field "program_studi" diperlukan'}), 400
        
        # Cek apakah program studi sudah ada
        existing_program_studi = ProgramStudi.query.filter_by(program_studi=data['program_studi']).first()
        if existing_program_studi:
            return jsonify({'message': 'Program studi ini sudah ada.'}), 400
        
        new_program_studi = ProgramStudi(program_studi=data['program_studi'])
        
        try:
            db.session.add(new_program_studi)
            db.session.commit()
            return jsonify({
                'message': 'Program studi berhasil ditambahkan',
                'data': {
                    'id': new_program_studi.id,
                    'program_studi': new_program_studi.program_studi
                }
            }), 201
        except Exception as e:
            db.session.rollback()  # Mengembalikan sesi jika terjadi kesalahan
            return jsonify({'message': 'Terjadi kesalahan saat menambahkan program studi.', 'error': str(e)}), 500

@program_studi_bp.route('/program_studi/view', methods=['GET'])
def view_program_studi():
    program_studi_list = ProgramStudi.query.all()
    return render_template('program_studi.html', program_studi=program_studi_list)

@program_studi_bp.route('/program_studi/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def handle_program_studi_by_id(id):
    program_studi = ProgramStudi.query.get_or_404(id)
    
    if request.method == 'GET':
        return jsonify({'id': program_studi.id, 'program_studi': program_studi.program_studi})
    
    if request.method == 'PUT':
        data = request.json
        if 'program_studi' not in data:
            return jsonify({'message': 'Field "program_studi" diperlukan'}), 400
        
        program_studi.program_studi = data['program_studi']
        
        try:
            db.session.commit()
            return jsonify({'message': 'Data program studi berhasil diperbarui'})
        except Exception as e:
            db.session.rollback()  # Mengembalikan sesi jika terjadi kesalahan
            return jsonify({'message': 'Terjadi kesalahan saat memperbarui program studi.', 'error': str(e)}), 500
    
    if request.method == 'DELETE':
        try:
            db.session.delete(program_studi)
            db.session.commit()
            return jsonify({'message': 'Data program studi berhasil dihapus'})
        except Exception as e:
            db.session.rollback()  # Mengembalikan sesi jika terjadi kesalahan
            return jsonify({'message': 'Terjadi kesalahan saat menghapus program studi.', 'error': str(e)}), 500