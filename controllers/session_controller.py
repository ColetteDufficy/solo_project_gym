from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.session import Session
import repositories.member_repository as member_repository
import repositories.session_repository as session_repository

sessions_blueprint = Blueprint("sessions", __name__)


# To see list of all sessions
@sessions_blueprint.route("/sessions")
def sessions():
    sessions = session_repository.select_all() 
    return render_template("sessions/index.html", sessions = sessions)


# this is to hold the new sessions form
@sessions_blueprint.route("/sessions/new")
def new_session_form():
    return render_template("sessions/new.html", sessions = sessions)



# NEW
# POST '/sessions/new' 
# This is adding a new session to the bookings total list of sessions.
@sessions_blueprint.route("/sessions", methods=['POST'])
def new_session():
    session_name = request.form['session_name']
    time = request.form['time']
    max_capacity = request.form['max_capacity']

    # member = member_repository.select(member_id)
    session = Session(session_name, time, max_capacity)
    sessions = session_repository.save(session)
    # return redirect ("members", all_members = members)
    return redirect ("sessions")



# EDIT
# GET '/sessions/<id>/edit'
# this is the first part of the EDIT action. 
# You'll need to post the edited version back.
@sessions_blueprint.route("/sessions/<id>/edit", methods=['GET'])
def edit_session(id):
    session = session_repository.select(id)
    members = member_repository.select_all()
    return render_template("sessions/edit.html", session = session, members=members)


# UPDATE
# POST '/sessions/<id>'
# this is the second part of the edit/update function. see above. 
# if you edit, you HAVE to post it back. 
# Which means sending this back to "sessions" like its a new entry.
@sessions_blueprint.route("/sessions/<id>", methods=['POST'])
def update_session(id):
    session_name = request.form['session_name']
    time = request.form['time']
    max_capacity = request.form['max_capacity']
    
    # member = member_repository.select(member_id)
    session = Session(session_name, time, max_capacity, id)
    session_repository.update(session)
    return redirect("/sessions")




# @sessions_blueprint.route("/sessions/<id>")
# def show(id):
#     session = session_repository.select(id)
#     members = session_repository.members(session)
#     return render_template("sessions/show.html", session=session, members=members)
