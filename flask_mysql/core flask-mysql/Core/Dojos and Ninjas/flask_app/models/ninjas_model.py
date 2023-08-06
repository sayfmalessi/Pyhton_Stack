from flask_app import DB
from flask_app.config.mysqlconnection import  connectToMySQL 

class Ninja():
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    @classmethod
    def get_all(cls):

        query = "SELECT * FROM ninja;"
        results = connectToMySQL(DB).query_db(query)

        # print(results) # return []
        hero_instances = []
        for row in results:
            this_hero = cls(row)
            hero_instances.append(this_hero)

        return hero_instances
    
    # --------- CREATE -----------------
    @classmethod
    def create(cls, data):
        print("***", data)

        q = """
                INSERT INTO ninja (name, health_level, power)
                VALUES (%(hero_name)s,%(health)s,%(power)s);
            """
        
        return connectToMySQL(DB).query_DB(q, data)
    

    # ---------- READ ONE -------------
    @classmethod
    def show_one(cls, data):

        query = """
                    SELECT * FROM ninja
                    WHERE id = %(id)s;
                """
        results = connectToMySQL(DB).query_DB(query, data)
        # print(results)
        this_hero = cls(results[0])

        return this_hero
    

        # ----------- UPDATE ------------

    @classmethod
    def update_hero(cls, data):

        query = """
                UPDATE ninja 
                SET name = %(name)s,
                power = %(power)s,
                health_level = %(health_level)s
                WHERE id = %(id)s;
                """
        
        return   connectToMySQL(DB).query_DB(query, data)
    

    @classmethod
    def delete(cls, data):
        
        query = """
                DELETE FROM ninja
                WHERE id = %(id)s;
                """
            
        return   connectToMySQL(DB).query_DB(query, data)