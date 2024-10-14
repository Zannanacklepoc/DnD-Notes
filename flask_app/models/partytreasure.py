from flask_app.config.MySQLconnection import connect_to_mysql
from flask_app.models import register_login

class Treasure:
    def __init__(self,data):
        self.id = data['id']
        self.Name = data['Name']
        self.description = data['description']

    @classmethod
    def get_all_treasure(cls):
        query = "SELECT * FROM party_treasure;"
        print(query)
        results = connect_to_mysql('DnDnotes').query_db(query)
        
        treasure = []
        for row in results:
            treasure.append(cls(row))  # Append each campaign object
        
        return treasure
    
    @classmethod
    def save_treasure (cls, data ):
        query = "INSERT INTO party_treasure (Name, description, campaign_id) VALUES (%(Name)s, %(description)s, %(campaign_id)s);"
        results = connect_to_mysql('DnDnotes').query_db( query, data)
        return results
    
    @classmethod
    def delete(cls, id):
        query  = "DELETE FROM party_treasure WHERE id = %(id)s;"
        data = {"id": id}
        return connect_to_mysql('DnDnotes').query_db(query, data)
    
    @classmethod
    def get_treasure_by_campaign_id(cls, campaign_id):
        query = "SELECT * FROM party_treasure WHERE Campaign_id = %s"
        results = connect_to_mysql('DnDnotes').query_db(query, (campaign_id,))
        return results  # Adjust this based on your database library