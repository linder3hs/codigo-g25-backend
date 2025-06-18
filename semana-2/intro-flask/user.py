class User:
    def __init__(self, name, lastname, email, password):
        self.name = name
        self.lastname = lastname
        self.email = email
        self.password = password

    def parse_fullname(self):
        return f"{self.name} {self.lastname}"
