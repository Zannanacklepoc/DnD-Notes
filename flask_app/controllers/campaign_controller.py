from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.campagin import Campaigns
from flask_app.models.register_login import User
from flask_app.models.notes_models import Notes


@app.route('/dashboard')
def logged_in():
    if "users_id" not in session:
        return redirect('/')
    
    user_id = session['users_id']
    user=User.login_id({'id':user_id})
    campaigns = Campaigns.get_by_user_id({'user_id': user_id}) #Don't forget to call ur methods or else things wont work
    print("Campaigns data:", campaigns) 
    return render_template('dashboard.html', user=user, campaigns=campaigns) #The varitable recipies is what we are going to be looping through. Not the column

@app.route('/dashboard/new', methods=['POST'])
def new_campaign():
    print("Session contents:", session)
    # Get form data and insert into the database here
    data = { 
        "name": request.form['name'],
        "time_and_date": request.form['time_and_date'],
        "user_id": session['users_id']  # Assuming the user is logged in
    }
    Campaigns.save(data)
    
    flash("Campaign created successfully!")
    return redirect('/dashboard')

@app.route('/dashboard/<int:id>')
def view_campaign(id):
    session['campaign_id'] = id
    campaign = Campaigns.get_one_campaign({'id': id})
    
    # Fetch notes associated with this campaign
    notes = Notes.get_notes_by_campaign_id({'campaign_id': id})
    
    return render_template('notes.html', campaign=campaign, notes=notes)


@app.route('/dashboard/notes')
def view_notes():
    campaign_id = session.get('campaign_id')
    if not campaign_id:
        return redirect('/dashboard')  # Redirect if no campaign ID is set

    campaign = Campaigns.get_one_campaign({'id': campaign_id})
    notes = Notes.get_notes_by_campaign_id({'campaign_id': campaign_id})

    return render_template('notes.html', campaign=campaign, notes=notes)

if __name__=="__main__":
    app.run(debug=True)  