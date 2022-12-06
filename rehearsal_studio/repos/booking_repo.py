from models.bookings import Bookings
import repos.user_repo as user_repo
import repos.studio_repo as studio_repo
from db.run_sql import run_sql
import pdb


def create_booking(booking):
    sql = "INSERT INTO bookings (user_id, studio, booking_date, booking_time, attendees) VALUES (%s, %s, %s, %s, %s) RETURNING *"
    values = [booking.user_id.id, booking.studio_id, booking.date, booking.time, booking.attendees]
    result = run_sql(sql, values)
    id = result[0]['id']
    booking.id = id
    return booking 

def show_all():
    bookingz = []
    sql = "SELECT * FROM bookings"
    results = run_sql(sql)
    for row in results:
        user = user_repo.select_user(row['user_id'])
        studio = studio_repo.select_studio(row['studio'])
        booking = Bookings(user.name, studio.studio_number, row['booking_date'], row['booking_time'], row['attendees'], row['id'])
        bookingz.append(booking)
    return bookingz

def show_booking(id):
    sql = "SELECT * FROM bookings WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    user = user_repo.select_user(result['user_id'])
    studio = studio_repo.select_studio(result['studio'])
    booking = Bookings(user, studio.studio_number, result['booking_date'], result['booking_time'], result['attendees'], result['id'])
    return booking



def delete_booking(id):
    sql = "DELETE FROM bookings WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update_booking(booking):
    sql = "UPDATE bookings SET (user_id, studio, booking_date, booking_time, attendees) = (%s, %s, %s, %s, %s) WHERE id = %s RETURNING * "
    values = [booking.user_id, booking.studio_id, booking.date, booking.time, booking.attendees, booking.id]
    print(values)
    run_sql(sql, values)
    # id = result[0]['id']

def bookings_by_studio(studio_id):
    bookingz = []
    sql = "SELECT * FROM bookings WHERE studio = %s"
    values = [studio_id]
    results = run_sql(sql, values)
    for row in results:
        user = user_repo.select_user(row['user_id'])
        studio = studio_repo.select_studio(row['studio'])
        booking = Bookings(user, studio, row['booking_date'], row['booking_time'], row['attendees'], row['id'])
        bookingz.append(booking)
    return bookingz