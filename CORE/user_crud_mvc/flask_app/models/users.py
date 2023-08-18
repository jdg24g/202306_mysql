from flask_app.config.mysqlconnection  import connectToMySQL

class User:
    def __init__(self,data) -> None:
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"

        results = connectToMySQL('users_cr').query_db(query)

        users = []

        for user in results:
            users.append(cls(user))
        return users
    
    @classmethod
    def save(cls,data):
        query = "INSERT INTO users (first_name, last_name, email, created_at, updated_at) VALUES (%(fname)s, %(lname)s, %(email)s, NOW(), NOW())"
        print(query)
        return connectToMySQL('users_cr').query_db(query,data)
    
    @classmethod
    def get_one(cls,data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        print(query)
        results = connectToMySQL('users_cr').query_db(query,data)
        return cls(results[0])
        
    @classmethod
    def update(cls,data):
        query = "UPDATE users SET first_name = %(fname)s, last_name = %(lname)s, email = %(email)s, updated_at = NOW() WHERE id = %(id)s;"
        return connectToMySQL('users_cr').query_db(query,data)
    @classmethod
    def delete(cls,data):
        query = "DELETE FROM users WHERE id = %(id)s;"
        return connectToMySQL('users_cr').query_db(query,data)