from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.gym import Gym
import repositories.gym_repository as gym_repository
import repositories.member_repository as member_repository
import repositories.session_repository as session_repository

gyms_blueprint = Blueprint("gyms", __name__)



@gyms_blueprint.route("/gyms")
def gyms():
    gyms = gym_repository.select_all() # NEW
    return render_template("gyms/index.html", gyms = gyms)

# NEW
# GET '/visits/new'
@gyms_blueprint.route("/gyms/new", methods=['GET'])
def new_task():
    members = member_repository.select_all()
    sessions = session_repository.select_all()
    return render_template("gyms/new.html", members = members, sessions = sessions)

# CREATE 
# POST '/gyms'
@gyms_blueprint.route("/gyms",  methods=['POST'])
def create_task():
    member_id = request.form['member_id']
    session_id = request.form['session_id']
    member = member_repository.select(member_id)
    session = session_repository.select(session_id)
    gym = Gym(member, session)
    gym_repository.save(gym)
    return redirect('/gyms')


# DELETE A SESSION
# DELETE '/gyms/<id>'
@gyms_blueprint.route("/gyms/<id>/delete", methods=['POST'])
def delete_task(id):
    gym_repository.delete(id)
    return redirect('/gyms')

