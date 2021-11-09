from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.booking import Booking
import repositories.booking_repository as booking_repository
import repositories.member_repository as member_repository
import repositories.session_repository as session_repository

bookings_blueprint = Blueprint("bookings", __name__)


# this is to hold the new bookigns form
@bookings_blueprint.route("/bookings/new")
def new_booking_form():
    return render_template("bookings/new.html", bookings = bookings)


# To see list of all bookings
@bookings_blueprint.route("/bookings", methods=['GET'])
def bookings():
    bookings = booking_repository.select_all() # NEW
    return render_template("bookings/index.html", bookings = bookings)




# NEW
# GET '/visits/new'
@bookings_blueprint.route("/bookings/new", methods=['GET'])
def new_task():
    members = member_repository.select_all()
    sessions = session_repository.select_all()
    return render_template("bookings/new.html", members = members, sessions = sessions)

# CREATE 
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


# DELETE A SESSION
# DELETE '/bookings/<id>'
@bookings_blueprint.route("/bookings/<id>/delete", methods=['POST'])
def delete_task(id):
    booking_repository.delete(id)
    return redirect('/bookings')

