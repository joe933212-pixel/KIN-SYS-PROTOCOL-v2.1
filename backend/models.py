from backend.app import db
from datetime import datetime

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    role = db.Column(db.String(20), default='youth')
    wallet_address = db.Column(db.String(42), unique=True, nullable=True)
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class Application(db.Model):
    __tablename__ = 'applications'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=False)
    status = db.Column(db.String(20), default='pending')
    blockchain_tx_hash = db.Column(db.String(66), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class PaymentLedger(db.Model):
    __tablename__ = 'payment_ledger'
    id = db.Column(db.Integer, primary_key=True)
    application_id = db.Column(db.Integer, db.ForeignKey('applications.id'), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    youth_amount = db.Column(db.Float)
    platform_amount = db.Column(db.Float)
    reserve_amount = db.Column(db.Float)
    blockchain_tx_hash = db.Column(db.String(66), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class GPUWorkload(db.Model):
    __tablename__ = 'gpu_workload'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    workload_type = db.Column(db.String(100), nullable=False)
    compute_hours = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(20), default='active')
    blockchain_tx_hash = db.Column(db.String(66), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class AuditLog(db.Model):
    __tablename__ = 'audit_logs'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=True)
    action = db.Column(db.String(255), nullable=False)
    resource_type = db.Column(db.String(50), nullable=False)
    details = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)