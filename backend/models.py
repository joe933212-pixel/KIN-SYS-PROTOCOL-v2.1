class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

class Application:
    def __init__(self, app_name, user):
        self.app_name = app_name
        self.user = user

class PaymentLedger:
    def __init__(self, amount, user, timestamp):
        self.amount = amount
        self.user = user
        self.timestamp = timestamp

class GPUWorkload:
    def __init__(self, workload_id, gpu_type, user):
        self.workload_id = workload_id
        self.gpu_type = gpu_type
        self.user = user

class AuditLog:
    def __init__(self, action, user, timestamp):
        self.action = action
        self.user = user
        self.timestamp = timestamp
