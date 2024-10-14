from flask_app.config.MySQLconnection import connect_to_mysql
from flask_app.models import register_login

class NPC:
    def __init__(self,data):
        self.id = data['id']
        self.Name = data['Name']
        self.Race = data['Race']
        self.Class = data['Class']
        self.location = data['location']
        self.small_discription = data['small_discription']

    @classmethod
    def get_all_NPCs(cls):
        query = "SELECT * FROM npc;"
        print(query)
        results = connect_to_mysql('DnDnotes').query_db(query)
        
        npc = []
        for row in results:
            npc.append(cls(row))  # Append each campaign object
        
        return npc
    
    @classmethod
    def save_npc (cls, data ):
        query = "INSERT INTO npc (Name, Race, Class, location, small_discription, campaign_id) VALUES (%(Name)s, %(Race)s,%(Class)s,%(location)s, %(small_discription)s,%(campaign_id)s);"
        results = connect_to_mysql('DnDnotes').query_db( query, data)
        return results
    
    @classmethod
    def delete(cls, id):
        query  = "DELETE FROM npc WHERE id = %(id)s;"
        data = {"id": id}
        return connect_to_mysql('DnDnotes').query_db(query, data)
    
    @classmethod
    def update(cls,data):
        query = """UPDATE npc 
                SET Name = %(Name)s, 
                    Race = %(Race)s, 
                    Class = %(Class)s, 
                    location = %(location)s, 
                    small_discription = %(small_discription)s, 
                    campaign_id = %(campaign_id)s 
                WHERE id = %(id)s;"""
        print(query)
        return connect_to_mysql('DnDnotes').query_db(query,data)
    
    @classmethod
    def get_by_id(cls, npc_id):
        query = "SELECT * FROM npc WHERE id = %(id)s;"
        data = { 'id': npc_id }
        results = connect_to_mysql('DnDnotes').query_db(query, data)
        if results:
            return results[0]
        
    @classmethod
    def get_NPCs_by_campaign_id(cls, campaign_id):
        query = "SELECT * FROM npc WHERE Campaign_id = %s"
        results = connect_to_mysql('DnDnotes').query_db(query, (campaign_id,))
        return results  # Adjust this based on your database library