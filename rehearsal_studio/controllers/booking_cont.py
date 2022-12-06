from flask import Flask, render_template, Blueprint, request, redirect
from models.bookings import Bookings
from models.studio import Studio
from models.user import User
import repos.booking_repo as booking_repo
import repos.studio_repo as studio_repo
import repos.user_repo as user_repo

booking_blueprint = Blueprint("bookings", __name__)

# "/bookings/view_all"
@booking_blueprint.route("/view_all")
def view_all():
    all_bookings = booking_repo.show_all()
    return render_template('/bookings/view_all.html', all_bookings=all_bookings)

# "/bookings/create_booking"
@booking_blueprint.route("/create_booking")
def create_booking_form():
    studios = studio_repo.all_studios()
    return render_template('/bookings/create_booking.html', studios=studios)

@booking_blueprint.route('/view_all', methods=['POST'])
def create_booking():
    name = request.form["name"]
    studio = request.form["studio"]
    date = request.form["date"]
    time = request.form["time"]
    attendees = request.form["attendees"]
    user = User(name)
    user = user_repo.create_user(user)
    booking = Bookings(user, studio, date, time, attendees)
    booking = booking_repo.create_booking(booking)
    return redirect('/view_all')

@booking_blueprint.route('/<booking_id>/delete', methods=['POST'])
def delete_booking(booking_id):
    booking_repo.delete_booking(booking_id)
    return redirect('/view_all')


@booking_blueprint.route('/<booking_id>/edit')
def edit_booking(booking_id):
    booking = booking_repo.show_booking(booking_id)
    studios = studio_repo.all_studios()
    return render_template("/bookings/edit.html", booking=booking, studios=studios)

@booking_blueprint.route('/<booking_id>/update', methods=['POST'])
def submit_edit(booking_id):
    user_id = request.form["user_id"]
    studio = request.form["studio"]
    date = request.form["date"]
    time = request.form["time"]
    attendees = request.form["attendees"]
    booking = Bookings(user_id, studio, date, time, attendees, booking_id)
    booking_repo.update_booking(booking)
    return redirect('/view_all')


@booking_blueprint.route('/bookings_by_studio')
def show_studios():
    studios = studio_repo.all_studios()
    return render_template('/studios/studios.html', studios=studios)

@booking_blueprint.route('/bookings_by_studio/<studio_id>')
def filter_by_studio(studio_id):
    studios = studio_repo.all_studios()
    filtered_bookings = booking_repo.bookings_by_studio(studio_id)
    return render_template('/studios/view_bookings.html', studios=studios, filtered_bookings=filtered_bookings)