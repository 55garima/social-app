"""User controller for handling HTTP requests."""
from typing import Tuple, Dict, Any
from flask import jsonify, request
from flask_jwt_extended import create_access_token
from marshmallow import ValidationError
from app.schemas.request.report_request_dto import ReportRequestDTO
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

           ##  print(f"REQUEST {request.headers}")
           
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
                
            validated_user_dict = UserService.authenticate_user(username, password)
            if validated_user_dict:
                access_token = create_access_token(identity=validated_user_dict['id'])

                print(f"USER : {validated_user_dict}")

                print(f"access token: {access_token}")

                return {'message': 'Login successful', 'validated_user_dict': validated_user_dict, 'access_token' : access_token}, 200
            return {'message': 'Invalid credentials'}, 401
        except Exception as e:
            return {'message': 'Internal server error', 'error': str(e)}, 500 
        
    @staticmethod
    def report_user() -> Tuple[Dict[str, Any], int]:
        
        try:
            data = request.get_json()

            # print(f"data = {data} ////////////////////     type = {type(data)}")
            
            schema = ReportRequestDTO()
            validated_data = schema.load(data)
            # print(f"validated_data = {validated_data} ////////////////////     type = {type(validated_data)}")
            user = UserService.report_user_new(validated_data)

            return {'message': 'User created successfully', 'user': user}, 201
        except ValidationError as e:
            return {'message': 'Validation error', 'errors': e.messages}, 400
        except ValueError as e:
            return {'message': str(e)}, 409
        except Exception as e:
            return {'message': 'Internal server error', 'error': str(e)}, 500
    