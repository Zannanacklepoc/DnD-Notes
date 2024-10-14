from flask_app.config.MySQLconnection import connect_to_mysql
from flask_app.models import register_login

class Notes:
    def __init__(self,data):
        self.id = data['id']
        self.notes = data['notes']


    @classmethod
    def get_all_notes(cls):
        query = "SELECT * FROM notes;"
        print(query)
        results = connect_to_mysql('DnDnotes').query_db(query)
        
        notes = []
        for row in results:
            notes.append(cls(row))  # Append each campaign object
        
        return notes

    @classmethod
    def save_notes (cls, data ):
        query = "INSERT INTO notes (notes, date_time, campaign_id) VALUES (%(notes)s, NOW(), %(campaign_id)s);"
        results = connect_to_mysql('DnDnotes').query_db( query, data)
        return results
    
    @classmethod
    def get_notes_by_campaign_id(cls, data):
        query = "SELECT * FROM notes WHERE campaign_id = %(campaign_id)s;"
        results = connect_to_mysql('DnDnotes').query_db(query, data)
        return results