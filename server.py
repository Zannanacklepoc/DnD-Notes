from flask_app import app
from flask_app.controllers import login
from flask_app.models import register_login
from flask_app.models import notes_models
from flask_app.controllers import notes_controller
from flask_app.controllers import NPC_controller
from flask_app.models import NPC_model
from flask_app.models import quest_model
from flask_app.controllers import quest_controller
from flask_app.controllers import partytreasure_controller
from flask_app.models import partytreasure

# from flask_app.controllers import
if __name__=="__main__":
    app.run(debug=True)  