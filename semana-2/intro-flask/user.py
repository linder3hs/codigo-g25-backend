class User:
    def __init__(self, id, name, lastname, email, password):
        self.id = id
        self.name = name
        self.lastname = lastname
        self.email = email
        self.password = password

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "lastname": self.lastname,
            "email": self.email,
            "password": self.password
        }

    def parse_fullname(self):
        return f"{self.name} {self.lastname}"
