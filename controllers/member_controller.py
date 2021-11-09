from flask import Flask, render_template, request, redirect
from flask import Blueprint
# from controllers.session_controller import sessions
from models.member import Member
import repositories.member_repository as member_repository
import repositories.session_repository as session_repository

members_blueprint = Blueprint("members", __name__)


# To see list of all members
@members_blueprint.route("/members", methods=['GET'])
def members():
    members = member_repository.select_all() 
    return render_template("members/index.html", members = members)



# this is to hold the new member form
@members_blueprint.route("/members/new")
def new_member_form():
    return render_template("members/new.html", members = members)

    
    
# NEW
# POST '/members/new' 
# This is adding a new member to the gyms total list of members.
@members_blueprint.route("/members", methods=['POST'])
def new_member():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    email = request.form['email']
    active_member = request.form['active_member']

    # member = member_repository.select(member_id)
    member = Member(first_name, last_name, email, active_member)
    members = member_repository.save(member)
    # return redirect ("members", all_members = members)
    return redirect ("members")


# EDIT
# GET '/members/<id>/edit'
# this is the first part of the EDIT action. 
# You'll need to post the edited version back.
@members_blueprint.route("/members/<id>/edit", methods=['GET'])
def edit_member(id):
    member = member_repository.select(id)
    sessions = session_repository.select_all()
    return render_template("members/edit.html", member = member, sessions=sessions)

# UPDATE
# POST '/sessions/<id>'
# this is the second part of the edit/update function. see above. 
# if you edit, you HAVE to post it back. 
# Which means sending this back to "members" like its a new entry.
@members_blueprint.route("/members/<id>", methods=['POST'])
def update_member(id):
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    email = request.form['email']
    active_member = request.form['active_member']
    
    # member = member_repository.select(member_id)
    member = Member(first_name, last_name, email, active_member, id)
    member_repository.update(member)
    return redirect("members")




# @members_blueprint.route("/members/<id>")
# def show(id):
#     member = member_repository.select(id)
#     sessions = member_repository.sessions(member)
#     return render_template("members/show.html", member=member, sessions=sessions)