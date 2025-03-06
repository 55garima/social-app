"""Application factory module."""
import os
from flask import Flask
from flask_migrate import Migrate
from config.config import config
from config.database import db, init_db
from app.routes.user_routes import user_bp
from app.models.user import User
from app.models.report import Report
from dotenv import load_dotenv

# Create a migrate instance to be initialized with the app
migrate = Migrate()

def create_app(config_name=None):
    """Create and configure the Flask application.
    
    Args:
        config_name (str, optional): Configuration name. Defaults to None.
        
    Returns:
        Flask: Configured Flask application
    """
    # Load environment variables first
    load_dotenv()
    
    # Create Flask app
    app = Flask(__name__)
    
    # Use development config by default if not specified
    if config_name is None:
        config_name = os.getenv('FLASK_ENV', 'development')
    
    # Load the config
    app.config.from_object(config[config_name])
    
    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    
    with app.app_context():
        # Initialize database connection
        init_db(app)
        
        # Register blueprints
        app.register_blueprint(user_bp)
    
    # Health check endpoint
    @app.route('/health')
    def health_check():
        return {'status': 'healthy'}, 200
    
    return app
