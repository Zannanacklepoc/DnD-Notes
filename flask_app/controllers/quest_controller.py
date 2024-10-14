from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.notes_models import Notes
from flask_app.models.register_login import User
from flask_app.models.campagin import Campaigns
from flask_app.models.NPC_model import NPC
from flask_app.controllers import notes_controller
from flask_app.models.quest_model import Quest

@app.route('/dashboard/Quests')
def Quests():
    print("Quests route triggered")
    campaign_id = session.get('campaign_id')
    quest= Quest.get_all_quests()
    # Assuming you're fetching the campaign data from the database
    campaign_data = Campaigns.get_by_id(session.get('campaign_id'))
    quest = Quest.get_by_campaign_id(campaign_id)  # Fetch the campaign data
    return render_template('quests.html', quest=quest, campaign=campaign_data)

@app.route('/quests', methods=['POST'])
def save_quest():
    campaign_id = session.get('campaign_id')
    # Get form data and insert into the database here
    data = { 
        "Giver": request.form['Giver'],
        "Objective": request.form['Objective'],
        "Reward": request.form['Reward'],
        "user_id": session.get('user_id'),
        "campaign_id": campaign_id 
            # Assuming the user is logged in
    }
    Quest.save_quest(data)

    return redirect('/dashboard/Quests')

@app.route('/delete/<int:quest_id>')
def remove_quest(quest_id):
    Quest.delete(quest_id)
    return redirect('/dashboard/Quests')

if __name__=="__main__":
    app.run(debug=True)  