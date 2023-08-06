
from my_app.config.mysqlconnection import connectToMySQL


class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    # all queries are classmethods
    # so that they have access to the class
    # we want to call these methods regardless if we have any instance of the class
    #*********** CRUD ************
    # ------------ READ ALL ---------------
    @classmethod
    def get_all(cls):

        query = "SELECT * FROM users;"
        results = connectToMySQL("users_db").query_db(query)

        # print(results) # return []
        user_instances = []
        for row in results:
            this_user = cls(row)
            user_instances.append(this_user)

        return user_instances
    
    # --------- CREATE -----------------
    @classmethod
    def create(cls, data):
        print("***", data)

        q = """
                INSERT INTO users (first_name, last_name, email)
                VALUES (%(first_name)s,%(last_name)s,%(email)s);
            """
        
        return connectToMySQL("users_db").query_db(q, data)
    

    # ---------- READ ONE -------------
    @classmethod
    def show_one(cls, data):

        query = """
                    SELECT * FROM users
                    WHERE id = %(id)s;
                """
        results = connectToMySQL("users_db").query_db(query, data)
        # print(results)
        this_user = cls(results[0])

        return this_user
    

        # ----------- UPDATE ------------

    @classmethod
    def update_user(cls, data):

        query = """
                UPDATE users 
                SET first_name = %(first_name)s,
                last_name = %(last_name)s,
                email = %(email)s
                WHERE id = %(id)s;
                """
        
        return   connectToMySQL("users_db").query_db(query, data)
    

    @classmethod
    def delete(cls, data):
        #TODO complete this method
        pass