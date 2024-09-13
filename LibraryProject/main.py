
from models import UserModel, BookModel, user_table, book_table


user_jared = UserModel(username="jared", age=19, phonenumber="9812312345")

user_sharon = UserModel(username="sharon", age=21, phonenumber="9832132154")

user_jared.save()
user_sharon.save()

book_sherlock = BookModel("Sherlock Holmes", 'Aurthur', rating=7)

book_sherlock.save()

print("Printing user jared")
print(user_jared)

print("\nPrinting user Sharon")
print(user_sharon)

print("\nPrinting book sherlock")
print(book_sherlock)

print("\nPrinting book with id 1")
print(BookModel.get(1))

print("\nPrinting User with id 2")
print(UserModel.get(2))

print("\n\nPrinting all users from the user table")
print(user_table)
