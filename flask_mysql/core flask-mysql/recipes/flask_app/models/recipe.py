from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask import flash
from flask_app.models import user
class Recipe:
    def __init__(self,data):
        self.id = data['id']
        self.user_id = data['user_id']
        self.name = data['name']
        self.description = data['description']
        self.instruction = data['instruction']
        self.date = data['date']
        self.under = data['under']
        self.owner = user.User.get_by_id({'id':self.user_id}).first_name
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def create_recip(cls,data):
        query= """INSERT INTO recipes (name,user_id, description, instruction, date,under) 
        VALUES (%(name)s,%(user_id)s,%(description)s,%(instruction)s,%(date)s,%(under)s);
        """
        result=connectToMySQL(DATABASE).query_db(query,data)
        print(result)
        return result
   
   
    
    
        
    
    @classmethod
    def get_all(cls):
        query=""" SELECT * FROM recipes;
        """
        results =  connectToMySQL(DATABASE).query_db(query)
        all_rec=[]
        for row in results:
            all_rec.append(cls(row))
        return all_rec
    @classmethod
    def get_by_id(cls,data):
            query=""" SELECT * FROM recipes WHERE id =%(id)s
            """
            result = connectToMySQL(DATABASE).query_db(query,data)
            if (result):
                return cls(result[0])
    @classmethod
    def edit_recip(cls,data):
        query="""UPDATE recipes
                SET name=%(name)s,description=%(description)s,instruction=%(instruction)s,
                date=%(date)s,under=%(under)s WHERE id = %(id)s;
        """
        return  connectToMySQL(DATABASE).query_db(query,data)
    @classmethod
    def remove(cls,data):
        query="""DELETE FROM recipes WHERE id=%(id)s
        """
        return  connectToMySQL(DATABASE).query_db(query,data)


    # * validation
    @staticmethod
    def validate(data):
        is_valid=True
        if len(data['name'])<3:
            flash("Invalid  name!")
            is_valid=False
        if len(data['description'])<3:
            flash("Invalid description!")
            is_valid=False
        if len(data['instruction'])<3:
            flash("Invalid instructions!")
            is_valid=False

        return is_valid


