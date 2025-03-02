"""User model for the application."""
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from config.database import db

class User(db.Model):
    """User model for storing user related details."""
    
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False, index=True)
    email = db.Column(db.String(120), unique=True, nullable=False, index=True)
    password_hash = db.Column(db.String(256), nullable=False)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    is_active = db.Column(db.Boolean, default=True)
    bio = db.Column(db.String(256), nullable=True)
    
    
    def __init__(self, username, email, password, first_name=None, last_name=None):
        """Initialize a new user.

        
        Args:
            username (str): The username
            email (str): The email address
            password (str): The unhashed password
            first_name (str, optional): The user's first name
            last_name (str, optional): The user's last name
        """
        self.username = username
        self.email = email
        self.password = password  # This will call the password.setter
        self.first_name = first_name
        self.last_name = last_name
    
    @property
    def password(self):
        """Prevent password from being accessed."""
        raise AttributeError('password is not a readable attribute')
    
    @password.setter
    def password(self, password):
        """Set password to a hashed password.
        
        Args:
            password (str): The password to hash
        """
        self.password_hash = generate_password_hash(password)
    
    def verify_password(self, password):
        """Check if password matches the hashed password.
        
        Args:
            password (str): The password to verify
            
        Returns:
            bool: True if password matches, False otherwise
        """
        return check_password_hash(self.password_hash, password)
    
    def to_dict(self):
        """Convert user object to dictionary.
        
        Returns:
            dict: User details
        """
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None,
            'is_active': self.is_active
        }
    
    def __repr__(self):
        """Return string representation of the user.
        
        Returns:
            str: String representation
        """
        return f'<User {self.username}>' 