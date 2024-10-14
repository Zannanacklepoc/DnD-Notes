from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.notes_models import Notes
from flask_app.models.register_login import User
from flask_app.models.campagin import Campaigns
from flask_app.models.NPC_model import NPC
from flask_app.controllers import notes_controller
from flask_app.models.quest_model import Quest
from flask_app.models.partytreasure import Treasure

@app.route('/dashboard/Party_treasure')
def Party_Treasure():
    print("Quests route triggered")
    campaign_id = session.get('campaign_id')
    treasure= Treasure.get_all_treasure()
    # Assuming you're fetching the campaign data from the database
    campaign_data = Campaigns.get_by_id(session.get('campaign_id'))
    treasure = Treasure.get_treasure_by_campaign_id(campaign_id)  # Fetch the campaign data
    return render_template('party_treasure.html', treasure=treasure, campaign=campaign_data)

@app.route('/treasure', methods=['POST'])
def save_treasure():
    campaign_id = session.get('campaign_id')
    # Get form data and insert into the database here
    data = { 
        "Name": request.form['Name'],
        "description": request.form['description'],
        "user_id": session.get('user_id'),
        "campaign_id": campaign_id 
            # Assuming the user is logged in
    }
    Treasure.save_treasure(data)

    return redirect('/dashboard/Party_treasure')

if __name__=="__main__":
    app.run(debug=True)  