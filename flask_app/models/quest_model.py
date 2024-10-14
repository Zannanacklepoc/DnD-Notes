from flask_app.config.MySQLconnection import connect_to_mysql
from flask_app.models import register_login

class Quest:
    def __init__(self,data):
        self.id = data['id']
        self.Giver = data['Giver']
        self.Objective = data['Objective']
        self.Reward = data['Reward']

    @classmethod
    def get_all_quests(cls):
        query = "SELECT * FROM quest;"
        print(query)
        results = connect_to_mysql('DnDnotes').query_db(query)
        
        quest = []
        for row in results:
            quest.append(cls(row))  # Append each campaign object
        
        return quest
    
    @classmethod
    def save_quest (cls, data ):
        query = "INSERT INTO quest (Giver, Objective, Reward, campaign_id) VALUES (%(Giver)s, %(Objective)s,%(Reward)s,%(campaign_id)s);"
        results = connect_to_mysql('DnDnotes').query_db( query, data)
        return results
    
    @classmethod
    def get_by_id(cls, npc_id):
        query = "SELECT * FROM quest WHERE id = %(id)s;"
        data = { 'id': npc_id }
        results = connect_to_mysql('DnDnotes').query_db(query, data)
        if results:
            return results[0]
        
    @classmethod
    def get_by_campaign_id(cls, campaign_id):
        query = "SELECT * FROM quest WHERE Campaign_id = %s"
        results = connect_to_mysql('DnDnotes').query_db(query, (campaign_id,))
        return results  # Adjust this based on your database library