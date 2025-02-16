"""User tests."""
import json
import pytest
from app.models.user import User

def test_create_user(client):
    """Test user creation."""
    # Test successful creation
    response = client.post(
        '/api/users',
        json={
            'username': 'testuser',
            'email': 'test@example.com',
            'password': 'Test123!@#',
            'first_name': 'Test',
            'last_name': 'User'
        }
    )
    assert response.status_code == 201
    data = json.loads(response.data)
    assert 'user' in data
    assert data['user']['username'] == 'testuser'
    
    # Test duplicate username
    response = client.post(
        '/api/users',
        json={
            'username': 'testuser',
            'email': 'another@example.com',
            'password': 'Test123!@#'
        }
    )
    assert response.status_code == 409
    
    # Test invalid password
    response = client.post(
        '/api/users',
        json={
            'username': 'newuser',
            'email': 'new@example.com',
            'password': 'weak'
        }
    )
    assert response.status_code == 400

def test_get_user(client, db):
    """Test user retrieval."""
    # Create test user
    user = User(
        username='testuser',
        email='test@example.com',
        password='Test123!@#'
    )
    db.session.add(user)
    db.session.commit()
    
    # Test successful retrieval
    response = client.get(f'/api/users/{user.id}')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['user']['username'] == 'testuser'
    
    # Test non-existent user
    response = client.get('/api/users/999')
    assert response.status_code == 404

def test_update_user(client, db):
    """Test user update."""
    # Create test user
    user = User(
        username='testuser',
        email='test@example.com',
        password='Test123!@#'
    )
    db.session.add(user)
    db.session.commit()
    
    # Test successful update
    response = client.put(
        f'/api/users/{user.id}',
        json={
            'first_name': 'Updated',
            'last_name': 'User'
        }
    )
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['user']['first_name'] == 'Updated'
    
    # Test invalid update
    response = client.put(
        f'/api/users/{user.id}',
        json={
            'email': 'invalid-email'
        }
    )
    assert response.status_code == 400

def test_delete_user(client, db):
    """Test user deletion."""
    # Create test user
    user = User(
        username='testuser',
        email='test@example.com',
        password='Test123!@#'
    )
    db.session.add(user)
    db.session.commit()
    
    # Test successful deletion
    response = client.delete(f'/api/users/{user.id}')
    assert response.status_code == 200
    
    # Test non-existent user
    response = client.delete(f'/api/users/{user.id}')
    assert response.status_code == 404

def test_login(client, db):
    """Test user login."""
    # Create test user
    user = User(
        username='testuser',
        email='test@example.com',
        password='Test123!@#'
    )
    db.session.add(user)
    db.session.commit()
    
    # Test successful login
    response = client.post(
        '/api/users/login',
        json={
            'username': 'testuser',
            'password': 'Test123!@#'
        }
    )
    assert response.status_code == 200
    
    # Test invalid credentials
    response = client.post(
        '/api/users/login',
        json={
            'username': 'testuser',
            'password': 'wrongpassword'
        }
    )
    assert response.status_code == 401
    
    # Test missing credentials
    response = client.post(
        '/api/users/login',
        json={
            'username': 'testuser'
        }
    )
    assert response.status_code == 400 