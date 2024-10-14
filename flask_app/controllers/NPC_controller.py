from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.notes_models import Notes
from flask_app.models.register_login import User
from flask_app.models.campagin import Campaigns
from flask_app.models.NPC_model import NPC
from flask_app.controllers import notes_controller


@app.route('/dashboard/NPC/new')
def new_NPC(): 
    campaign = Campaigns.get_by_id(session.get('campaign_id'))
    print("Accessing NPC/new page")
    return render_template('create_npc.html', campaign=campaign)

@app.route('/new/NPC', methods=['POST'])
def save_npc():
    campaign_id = session.get('campaign_id')
    # Get form data and insert into the database here
    data = { 
        "Name": request.form['Name'],
        "Race": request.form['Race'],
        "Class": request.form['Class'],
        "location": request.form['location'],
        "small_discription": request.form['small_discription'],
        "user_id": session.get('user_id'),
        "campaign_id": campaign_id 
            # Assuming the user is logged in
    }
    NPC.save_npc(data)

    return redirect('/dashboard/NPC')

@app.route('/delete/<int:npc_id>')
def remove_npc(npc_id):
    NPC.delete(npc_id)
    return redirect('/dashboard/NPC')

@app.route('/Edit/<int:npc_id>')
def edit_npc(npc_id):
    npc = NPC.get_by_id(npc_id)
    campaign = Campaigns.get_by_id(session.get('campaign_id'))  # Fetch the NPC data from the database
    return render_template('edit_npc.html', npc=npc, campaign=campaign)

@app.route('/Edit/<int:npc_id>', methods=['POST'])
def update_npc(npc_id):
    campaign_id = session.get('campaign_id')
	# ADD ID TO UPDATE CAUSE IT IS ADDED WHEN CREATED
    data = { 
        "id": npc_id,
        "Name": request.form['Name'],
        "Race": request.form['Race'],
        "Class": request.form['Class'],
        "location": request.form['location'],
        "small_discription": request.form['small_discription'],
        "user_id": session.get('user_id'),
        "campaign_id": campaign_id 
            # Assuming the user is logged in
    }
    print(data)
    NPC.update(data)
    print(data)
    return redirect('/dashboard/NPC')