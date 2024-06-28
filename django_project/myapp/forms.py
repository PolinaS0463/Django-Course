from django.forms import *
from myapp.models import *

class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = ['first_name', 'last_name', 'email', 'phone', 'address']
        widgets = {
                    'first_name' : TextInput(attrs={'placeholder' : 'Введите имя'}),
                    'last_name' : TextInput(attrs={'placeholder' : 'Введите фамилию'}),
                    'email' : EmailInput(attrs={'placeholder' : 'Введите почту'}),
                    'phone' : NumberInput(attrs={'placeholder' : 'Введите номер телефона'}),
                    'address' : TextInput(attrs={'placeholder' : 'Введите адрес'})
                  }
        
class Product(ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'description', 'price', 'amount']
        widgets = {
                    'title' : TextInput(attrs={'placeholder' : 'Введите название'}),
                    'description' : TextInput(attrs={'placeholder' : 'Введите описание'}),
                    'price' : NumberInput(attrs={'placeholder' : 'Введите цену'}),
                    'amount' : NumberInput(attrs={'placeholder' : 'Введите количество'})
                  }
        
