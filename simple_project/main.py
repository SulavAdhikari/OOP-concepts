from customer import Customer
from products import Product, Purchase


c_jared = Customer("Jared", 21, balance=1500)
c_sulav = Customer("Sulav", 18, balance=3000)
c_manraj= Customer("Manraj", 22, balance=7000)


p_laptop = Product("Asus ROG Gl753ve", 1500, 3)
p_GPU = Product("RTX-4070ti", 2000, 1)


purchase_1 = Purchase(p_laptop, c_jared, 1)
print("The transaction for the purchase has been completed, success: ", purchase_1.confirm)


purchase_2 = Purchase(p_laptop, c_manraj, 3)

purchase_2.confirm()
