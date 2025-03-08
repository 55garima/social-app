"""Report model for the application."""
from config.database import db 

class Report(db.Model):
    """Report Model for banned user"""
    
    __tablename__ = 'reports'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    reason = db.Column(db.String(256), nullable=False)

    def __init__(self, user_id = None, reason = None):   #contructor 
        self.user_id = user_id
        self.reason = reason
   