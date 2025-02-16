"""User controller for handling HTTP requests."""
from typing import Tuple, Dict, Any
from flask import jsonify, request
from marshmallow import ValidationError
from app.services.user_service import UserService
from app.schemas.user_schema import UserSchema

class UserController:
    """Controller class for user-related endpoints."""
    
    @staticmethod
    def create_user() -> Tuple[Dict[str, Any], int]:
        """Handle user creation request.
        
        Returns:
            tuple: Response data and status code
        """
        try:
            data = request.get_json()
            schema = UserSchema()
            validated_data = schema.load(data)
            user = UserService.create_user(validated_data)
            return {'message': 'User created successfully', 'user': user}, 201
        except ValidationError as e:
            return {'message': 'Validation error', 'errors': e.messages}, 400
        except ValueError as e:
            return {'message': str(e)}, 409
        except Exception as e:
            return {'message': 'Internal server error', 'error': str(e)}, 500
    
    @staticmethod
    def get_user(user_id: int) -> Tuple[Dict[str, Any], int]:
        """Handle get user request.
        
        Args:
            user_id (int): User ID
            
        Returns:
            tuple: Response data and status code
        """
        try:
            user = UserService.get_user_by_id(user_id)
            if user:
                return {'user': user}, 200
            return {'message': 'User not found'}, 404
        except Exception as e:
            return {'message': 'Internal server error', 'error': str(e)}, 500
    
    @staticmethod
    def get_all_users() -> Tuple[Dict[str, Any], int]:
        """Handle get all users request.
        
        Returns:
            tuple: Response data and status code
        """
        try:
            users = UserService.get_all_users()
            return {'users': users}, 200
        except Exception as e:
            return {'message': 'Internal server error', 'error': str(e)}, 500
    
    @staticmethod
    def update_user(user_id: int) -> Tuple[Dict[str, Any], int]:
        """Handle user update request.
        
        Args:
            user_id (int): User ID
            
        Returns:
            tuple: Response data and status code
        """
        try:
            data = request.get_json()
            schema = UserSchema(partial=True)
            validated_data = schema.load(data)
            user = UserService.update_user(user_id, validated_data)
            
            if user:
                return {'message': 'User updated successfully', 'user': user}, 200
            return {'message': 'User not found'}, 404
        except ValidationError as e:
            return {'message': 'Validation error', 'errors': e.messages}, 400
        except ValueError as e:
            return {'message': str(e)}, 409
        except Exception as e:
            return {'message': 'Internal server error', 'error': str(e)}, 500
    
    @staticmethod
    def delete_user(user_id: int) -> Tuple[Dict[str, Any], int]:
        """Handle user deletion request.
        
        Args:
            user_id (int): User ID
            
        Returns:
            tuple: Response data and status code
        """
        try:
            if UserService.delete_user(user_id):
                return {'message': 'User deleted successfully'}, 200
            return {'message': 'User not found'}, 404
        except Exception as e:
            return {'message': 'Internal server error', 'error': str(e)}, 500
    
    @staticmethod
    def login() -> Tuple[Dict[str, Any], int]:
        """Handle user login request.
        
        Returns:
            tuple: Response data and status code
        """
        try:
            data = request.get_json()
            username = data.get('username')
            password = data.get('password')
            
            if not username or not password:
                return {'message': 'Username and password are required'}, 400
                
            user = UserService.authenticate_user(username, password)
            if user:
                return {'message': 'Login successful', 'user': user}, 200
            return {'message': 'Invalid credentials'}, 401
        except Exception as e:
            return {'message': 'Internal server error', 'error': str(e)}, 500 