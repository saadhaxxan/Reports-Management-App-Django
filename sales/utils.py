import uuid
from profiles.models import Profile
from customers.models import Customer
def generate_code():
    code = str(uuid.uuid4()).replace('-',"")[:12]
    return code

def get_saleman_from_id(val):
    obj = Profile.objects.get(id=val)
    return obj.user.username

def get_customer_from_id(val):
    obj = Customer.objects.get(id=val)
    return obj