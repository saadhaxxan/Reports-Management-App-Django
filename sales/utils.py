import uuid, base64
from profiles.models import Profile
from customers.models import Customer
from io import BytesIO
import matplotlib.pyplot as plt
def generate_code():
    code = str(uuid.uuid4()).replace('-',"")[:12]
    return code

def get_graph():
    buffer = BytesIO()
    plt.savefig(buffer,format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')
    buffer.close()
    return graph

def get_chart(chart_type,data,**kwargs):
    plt.switch_backend('AGG')
    if chart_type == "#1":
        print("bar chart")
        plt.bar(data['transaction_id'],data['price'])
    elif chart_type == "#2":
        labels = kwargs.get('labels')
        plt.pie(data=data,x='price',labels=labels)
        print("pie chart")
    elif chart_type == "#3":
        plt.line(data['transaction_id'],data['price'])
        print("line chart")
    else:
        print("chart generation failed")
    chart = get_graph()
    return chart

def get_saleman_from_id(val):
    obj = Profile.objects.get(id=val)
    return obj.user.username

def get_customer_from_id(val):
    obj = Customer.objects.get(id=val)
    return obj