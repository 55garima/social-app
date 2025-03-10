"""Database configuration and initialization module.

This module handles database setup, initialization, and provides the SQLAlchemy instance
for the application. It supports database connection and configuration.
"""
from typing import Any
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
import logging

# Configure logger for database operations
logger = logging.getLogger(__name__)

# Create a single SQLAlchemy instance to be used across the app
db = SQLAlchemy()

def init_db(app: Flask) -> None:
    """Initialize the database connection with the Flask app.
    
    Note: This no longer creates tables automatically as we're using migrations.
    """
    try:
        # Ensure the database exists
        _create_database_if_not_exists(app.config['SQLALCHEMY_DATABASE_URI'])
        logger.info("Database connection initialized successfully")
    except Exception as e:
        raise RuntimeError(f"Failed to initialize database: {str(e)}") from e

def _create_database_if_not_exists(database_uri: str) -> None:
    """Create the database if it doesn't exist.
    
    Args:
        database_uri: SQLAlchemy database URI
        
    Raises:
        RuntimeError: If database creation fails
    """
    try:
        engine = create_engine(database_uri)
        if not database_exists(engine.url):
            create_database(engine.url)
            logger.info("Created database: %s", engine.url.database)
    except Exception as e:
        logger.error("Failed to create database: %s", str(e))
        raise RuntimeError(f"Database creation failed: {str(e)}") from e 