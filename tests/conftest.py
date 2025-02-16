"""Test configuration and fixtures."""
import pytest
from app import create_app
from config.database import db as _db

@pytest.fixture
def app():
    """Create and configure a new app instance for each test.
    
    Returns:
        Flask: Test Flask application
    """
    app = create_app('testing')
    
    # Create tables
    with app.app_context():
        _db.create_all()
    
    yield app
    
    # Clean up
    with app.app_context():
        _db.session.remove()
        _db.drop_all()

@pytest.fixture
def client(app):
    """Create a test client for the app.
    
    Args:
        app: Flask application
        
    Returns:
        FlaskClient: Test client
    """
    return app.test_client()

@pytest.fixture
def db(app):
    """Create a new database session for a test.
    
    Args:
        app: Flask application
        
    Returns:
        SQLAlchemy: Database instance
    """
    with app.app_context():
        yield _db 