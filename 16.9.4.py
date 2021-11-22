class User:
    def __init__(self, name, city):
        self.name = name
        self.city = city

class Post(User):
    def __init__(self, post, **kwargs):
        self.post = post
        super().__init__(**kwargs)

    def get_post(self):
        return f'{self.name}, {self.city} city - {self.post}'

karl = Post(name='Karl Pivz', city='Omsk', post='Director')
peter = Post(name='Harry Potter', city='London', post='Student')
print(karl.get_post())
print(peter.get_post())
