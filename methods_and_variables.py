

class Book:

    # this is a class level static variable
    book_type = "Digital"
    store_name = "Falano Digital Store"


    def __init__(self, name, author, pre_tax_price, pages):
        # all these below are instance variable 
        self.name = name
        self.author = author
        self.pre_tax_price = pre_tax_price
        self.pages = pages

    @property
    def price(self):
        # local variable. Cannot be accessed outside this method.
        tax_percentage = 0.25
        return self.pre_tax_price + (self.pre_tax_price * tax_percentage)

    # static method
    @staticmethod
    def purchase():
        print("Purchasing this book")
        # declaring a static variable inside a static method
        Book.soldout = True

    @classmethod
    def get_product_info(cls):
        return {
                "Product_type": cls.book_type ,
                "Store_name": cls.store_name
                }



bookobj = Book("bookname", "bookauthor", 100, 25)

print("\n\nPost tax price of the book: ", bookobj.price)

print("Product info: ", Book.get_product_info())


bookobj.purchase()

print(Book.soldout)