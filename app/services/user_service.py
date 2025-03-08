"""User service for handling business logic."""

from typing import Optional, List, Dict, Any
from sqlalchemy.exc import IntegrityError
from app.models.report import Report
from config.database import db
from app.models.user import User
from app.schemas.user_schema import user_schema, users_schema


class UserService:
    """Service class for user-related operations."""

    @staticmethod
    def create_user(data: Dict[str, Any]) -> Dict[str, Any]:
        """Create a new user.

        Args:
            data (dict): User data including username, email, password, etc.

        Returns:
            dict: Created user data

        Raises:
            ValueError: If username or email already exists
        """
        try:
            user = User(
                username=data["username"],
                email=data["email"],
                password=data["password"],
                first_name=data.get("first_name"),
                last_name=data.get("last_name"),
                bio=data.get("bio"),
                country=data.get("country"),
            )
            db.session.add(user)
            db.session.commit()
            return user_schema.dump(user)
        except IntegrityError:
            db.session.rollback()
            raise ValueError("Username or email already exists")

    @staticmethod
    def get_user_by_id(user_id: int) -> Optional[Dict[str, Any]]:
        """Get user by ID.

        Args:
            user_id (int): User ID

        Returns:
            dict: User data if found, None otherwise
        """
        user = User.query.get(user_id)
        return user_schema.dump(user) if user else None

    @staticmethod
    def get_user_by_username(username: str) -> Optional[Dict[str, Any]]:
        """Get user by username.

        Args:
            username (str): Username

        Returns:
            dict: User data if found, None otherwise
        """
        user = User.query.filter_by(username=username).first()
        return user_schema.dump(user) if user else None

    @staticmethod
    def get_all_users() -> List[Dict[str, Any]]:
        """Get all users.

        Returns:
            list: List of all users
        """
        users = User.query.all()
        return users_schema.dump(users)

    @staticmethod
    def update_user(user_id: int, data: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """Update user details.

        Args:
            user_id (int): User ID
            data (dict): Updated user data

        Returns:
            dict: Updated user data if successful, None if user not found

        Raises:
            ValueError: If username or email already exists
        """
        user = User.query.get(user_id)
        if not user:
            return None

        try:
            for key, value in data.items():
                if key == "password":
                    user.password = value
                elif hasattr(user, key):
                    setattr(user, key, value)

            db.session.commit()
            return user_schema.dump(user)
        except IntegrityError:
            db.session.rollback()
            raise ValueError("Username or email already exists")

    @staticmethod
    def delete_user(user_id: int) -> bool:
        """Delete a user.

        Args:
            user_id (int): User ID

        Returns:
            bool: True if deleted successfully, False if user not found
        """
        user = User.query.get(user_id)
        if not user:
            return False

        db.session.delete(user)
        db.session.commit()
        return True

    @staticmethod
    def authenticate_user(username: str, password: str) -> Optional[Dict[str, Any]]:
        """Authenticate a user.

        Args:
            username (str): Username
            password (str): Password

        Returns:
            dict: User data if authentication successful, None otherwise
        """
        user = User.query.filter_by(username=username).first()
        if user and user.verify_password(password):
            return user_schema.dump(user)
        return None

    @staticmethod
    def report_user_new(Validated_data):
        target_id = Validated_data.get("target_id")
        reason = Validated_data["reason"]
        reported_user = Report()
        reported_user.user_id = target_id
        reported_user.reason = reason

        db.session.add(reported_user)
        db.session.commit()