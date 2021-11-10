from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.booking import Booking
import repositories.booking_repository as booking_repository
import repositories.member_repository as member_repository
import repositories.session_repository as session_repository

bookings_blueprint = Blueprint("bookings", __name__)


# INDEXthis is to view all bookings
@bookings_blueprint.route("/bookings")
def bookings():
    bookings = booking_repository.select_all_alphabetical()
    return render_template("bookings/index.html", bookings = bookings)




# show a selected member
@bookings_blueprint.route("/bookings/<id>")
def show(id):
    member = member_repository.select(id)
    sessions = member_repository.sessions(member)
    return render_template("bookings/show.html", member=member, sessions=sessions)


# NEW booking
# GET '/visits/new'
@bookings_blueprint.route("/bookings/new", methods=['GET'])
def new_session():
    members = member_repository.select_all()
    sessions = session_repository.select_all()
    return render_template("bookings/new.html", members = members, sessions = sessions)

# CREATE a booking
# POST '/bookings'
@bookings_blueprint.route("/bookings",  methods=['POST'])
def create_task():
    member_id = request.form['member_id']
    session_id = request.form['session_id']
    member = member_repository.select(member_id)
    session = session_repository.select(session_id)
    booking = Booking(member, session)
    booking_repository.save(booking)
    return redirect('/bookings')


# select a specific session
# @bookings_blueprint.route("/bookings/<id>/show")
# def show(id):
#     session = session_repository.select(id)
#     members = session_repository.members(session)
#     return render_template("bookings/show.html", session=session, members=members)


# DELETE
@bookings_blueprint.route("/bookings/<id>/delete", methods=["POST"])
def delete_booking(id):
    booking_repository.delete(id)
    return redirect("/bookings")


# DELETE A SESSION
# DELETE '/bookings/<id>'
@bookings_blueprint.route("/bookings/<id>/delete", methods=['POST'])
def delete_session(id):
    booking_repository.delete(id)
    return redirect('/bookings')

