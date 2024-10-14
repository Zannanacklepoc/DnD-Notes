from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.notes_models import Notes
from flask_app.models.register_login import User
from flask_app.models.NPC_model import NPC
from flask_app.models.campagin import Campaigns
from flask_app.controllers import NPC_controller

@app.route('/notes', methods=['POST'])
def notes():
    # Get form data and insert into the database here
    data = { 
        "notes": request.form['notes'],
        "user_id": session.get('user_id'),
        "campaign_id": request.form['campaign_id'] 
            # Assuming the user is logged in
    }
    Notes.save_notes(data)

    return redirect(f'/dashboard/{request.form["campaign_id"]}')

@app.route('/dashboard/NPC')
def NPCs():
    campaign_id = session.get('campaign_id')
    # Assuming you're fetching the campaign data from the database
    campaign_data = Campaigns.get_by_id(session.get('campaign_id')) 
    npc= NPC.get_all_NPCs() # Fetch the campaign data
    npc = NPC.get_NPCs_by_campaign_id(campaign_id)
    return render_template('NPC.html', npc=npc, campaign=campaign_data, campaign_id=campaign_id)


if __name__=="__main__":
    app.run(debug=True)  