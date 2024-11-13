from flask import Blueprint, request, jsonify, render_template
from models.angkatan import Angkatan
from models import db

angkatan_bp = Blueprint('angkatan', __name__)

@angkatan_bp.route('/angkatan', methods=['GET', 'POST'])
def handle_angkatan():
    if request.method == 'GET':
        angkatan_list = Angkatan.query.all()
        result = [{'id': a.id, 'tahun': a.tahun} for a in angkatan_list]
        return jsonify(result)
    
    if request.method == 'POST':
        data = request.json
        if 'tahun' not in data:
            return jsonify({'message': 'Field "tahun" diperlukan'}), 400
        
        new_angkatan = Angkatan(tahun=data['tahun'])
        db.session.add(new_angkatan)
        db.session.commit()
        return jsonify({
            'message': 'Angkatan berhasil ditambahkan',
            'data': {
                'id': new_angkatan.id,
                'tahun': new_angkatan.tahun
            }
        }), 201
    
@angkatan_bp.route('/angkatan/view', methods=['GET'])
def view_angkatan():
    angkatan_list = Angkatan.query.all()
    
    # Mengirimkan data angkatan ke template
    return render_template('angkatan.html', angkatan=angkatan_list)

@angkatan_bp.route('/angkatan/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def handle_angkatan_by_id(id):
    angkatan = Angkatan.query.get_or_404(id)
    
    if request.method == 'GET':
        return jsonify({'id': angkatan.id, 'tahun': angkatan.tahun})
    
    if request.method == 'PUT':
        data = request.json
        if 'tahun' not in data:
            return jsonify({'message': 'Field "tahun" diperlukan'}), 400
        
        angkatan.tahun = data['tahun']
        db.session.commit()
        return jsonify({'message': 'Data angkatan berhasil diperbarui'})
    
    if request.method == 'DELETE':
        db.session.delete(angkatan)
        db.session.commit()
        return jsonify({'message': 'Data angkatan berhasil dihapus'})
