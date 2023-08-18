from flask_app.config.mysqlconnection import connectToMySQL

class Dojo:
    def __init__(self,data) -> None:
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL('schema_dojo_and_ninjas').query_db(query)

        dojos = []
        for dojo in results:
            dojos.append(cls(dojo))
        return dojos


    @classmethod
    def get_one(cls,data):
        query = "SELECT * FROM dojos WHERE id = %(id)s;"
        results = connectToMySQL('schema_dojo_and_ninjas').query_db(query,data)
        return cls(results[0])

    @classmethod
    def save(cls,data):
        query = "INSERT INTO dojos (name) VALUES (%(name)s);"
        print(f'Se corrio la query {query}¡ de la funcion save(cls,data)')
        return connectToMySQL('schema_dojo_and_ninjas').query_db(query,data)
