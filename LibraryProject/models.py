from abc import ABC, abstractmethod

user_table = []
book_table = []
lend_table = []

class ModelManager(ABC):

    def __assign_id(self):
        if self.model_table == []:
            self.id = 1
        else: 
            self.id = max([model['id'] for model in self.model_table]) + 1

    def __init__(self):
        self.__assign_id()

    @abstractmethod
    def save(self, dict_data):
        if self.id in [model['id'] for model in self.model_table]:
            self.__assign_id()
        dict_data['id'] = self.id
        

    @classmethod
    def get(cls, id):
        for model in cls.model_table:
            if model['id'] == id:
                return model


class UserModel(ModelManager):
    model_table = user_table

    username = None
    age = None
    phonenumber = None

    def __init__(self, username=None, age=None, phonenumber=None):
        self.dict_data = {
            'username':self.username,
            'age': self.age,
            'phonenumber': self.phonenumber
        }
        super().__init__()

    def save(self):    
        super().save(self.dict_data)
        if self.dict_data not in user_table:
            user_table.append(self.dict_data)
        else:
            for user in user_table:
                if user['id'] == self.id:
                    user = model_data
                    break
    
    def __repr__(self):
        return str(self.dict_data)


class BookModel(ModelManager):
    model_table = book_table

    book_name = None
    author = None
    rating = None

    def __init__(self, book_name=None, author=None, rating=None):
        super().__init__()
        self.dict_data = {
            'book_name':self.book_name,
            'author': self.author,
            'rating': self.rating
        }    
    def save(self):
        
        super().save(self.dict_data)
        if self.dict_data not in user_table:
            book_table.append(self.dict_data)
        else:
            for book in book_table:
                if book['id'] == self.id:
                    book = model_data
                    break

    def __repr__(self):
        return str(self.dict_data)



class LendModel(ModelManager):
    
    def __init__(self):
        pass

