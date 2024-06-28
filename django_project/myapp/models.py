from django.db.models import * 

class Client(Model):
    first_name = CharField(max_length=20)
    last_name = CharField(max_length=30)
    email = EmailField(null=False)
    phone = PositiveIntegerField(unique=True)
    address = CharField(max_length=100)
    joined = DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}\nEmail: {self.email}\nPhone: {self.phone}\nAddress: {self.address}\nJoined on: {self.joined}'

class Product(Model):
    title = CharField(max_length=20)
    description = CharField(max_length=100)
    price = PositiveIntegerField(null=False)
    amount = PositiveIntegerField(default=0)
    added = DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.title}\{self.description}\nPrice: {self.price}\nAmount: {self.amount}\nAdded on: {self.added}'

class Order(Model):
    client = ForeignKey(Client, on_delete=CASCADE)
    products = ManyToManyField(Product)
    total = PositiveIntegerField(null=False)
    ordered = DateField(auto_now_add=True)

    def __str__(self):
        return f'Ordered by User {self.client.pk}\n{self.products.all()}\nTotal: {self.total}\nOrdered on: {self.ordered}'