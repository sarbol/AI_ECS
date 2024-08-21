from flask import Blueprint, request, jsonify
from .models import User, EnvironmentData, db
from .services.ai_service import get_optimal_settings

main_bp = Blueprint('main', __name__)

@main_bp.route('/api/environment', methods=['POST'])
def update_environment():
    data = request.json
    new_data = EnvironmentData(**data)
    db.session.add(new_data)
    db.session.commit()
    
    optimal_settings = get_optimal_settings(new_data)
    
    return jsonify({"optimal_settings": optimal_settings})

@main_bp.route('/api/user', methods=['POST'])
def create_user():
    data = request.json
    new_user = User(**data)
    db.session.add(new_user)
    db.session.commit()
    
    return jsonify({"message": "User created successfully"}), 201
