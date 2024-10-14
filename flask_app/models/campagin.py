from flask_app.config.MySQLconnection import connect_to_mysql
from flask_app.models import register_login

class Campaigns:
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.time_and_date = data['time_and_date']


    @classmethod
    def get_all(cls):
        query = "SELECT * FROM campaign;"
        print(query)
        results = connect_to_mysql('DnDnotes').query_db(query)
    
        campaigns = []
        for row in results:
            campaigns.append(cls(row))  # Append each campaign object
    
        return campaigns
    
    @classmethod
    def save (cls, data ):
        query = "INSERT INTO campaign (name, time_and_date, user_id) VALUES (%(name)s, %(time_and_date)s, %(user_id)s);"
        results = connect_to_mysql('DnDnotes').query_db( query, data)
        return results
    
    @classmethod
    def get_one_campaign(cls, data):
        query = """
        SELECT campaign.*, 
            user.id AS user_id, 
            user.first_name, 
            user.last_name, 
            user.email
        FROM campaign 
        JOIN user ON campaign.user_id = user.id 
        WHERE campaign.id = %(id)s;
        """
        print(query)
        results = connect_to_mysql('DnDnotes').query_db(query, data)
    
        if results:  # If the query returns any results
            campaign = cls(results[0])  # Create a Campaign object with the first row of the result
        
        user_data = {
            "id": results[0]['user_id'],
            "first_name": results[0]['first_name'],
            "last_name": results[0]['last_name'],
            "email": results[0]['email']
        }
        
        # Create a User object and assign it to the campaign
        campaign.user = register_login.User(user_data)
        
        return campaign
    
    @classmethod
    def get_by_id(cls, campaign_id):
        query = "SELECT * FROM campaign WHERE id = %(id)s;"
        data = {"id": campaign_id}  # Parameterized query to prevent SQL injection
        print(query)
        
        result = connect_to_mysql('DnDnotes').query_db(query, data)
        return result
    
    @staticmethod
    def get_by_user_id(data):
        query = "SELECT * FROM campaign WHERE user_id = %(user_id)s;"
        results = connect_to_mysql('DnDnotes').query_db(query, data)
        return results  # Adjust this based on your database library