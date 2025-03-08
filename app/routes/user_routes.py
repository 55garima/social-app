"""User routes for the application."""
from flask import Blueprint
from app.controllers.user_controller import UserController

# Create blueprint
user_bp = Blueprint('user', __name__, url_prefix='/api/users')

# User registration and authentication
user_bp.add_url_rule(
    '',
    view_func=UserController.create_user,
    methods=['POST']
)

user_bp.add_url_rule(
    '/login',
    view_func=UserController.login,
    methods=['POST']
)

# User CRUD operations
user_bp.add_url_rule(
    '',
    view_func=UserController.get_all_users,
    methods=['GET']
)

user_bp.add_url_rule(
    '/<int:user_id>',
    view_func=UserController.get_user,
    methods=['GET']
)

user_bp.add_url_rule(
    '/<int:user_id>',
    view_func=UserController.update_user,
    methods=['PUT']
)

user_bp.add_url_rule(
    '/<int:user_id>',
    view_func=UserController.delete_user,
    methods=['DELETE']
) 

user_bp.add_url_rule(
    '/report',
    view_func=UserController.report_user,
    methods=['POST']
) 