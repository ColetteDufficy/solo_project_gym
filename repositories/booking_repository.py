from db.run_sql import run_sql
from models.booking import Booking
import repositories.member_repository as member_repository
import repositories.session_repository as session_repository



# Creating A New Booking 
def save(booking):
    sql = "INSERT INTO bookings2 ( member_id, session_id ) VALUES ( %s, %s ) RETURNING id"
    values = [booking.member.id, booking.session.id]
    results = run_sql( sql, values )
    booking.id = results[0]['id']
    return booking



# To see list of all bookings
def select_all():
    bookings = []

    sql = "SELECT * FROM bookings"
    results = run_sql(sql)

    for row in results:
        member = member_repository.select(row['member_id'])
        session = session_repository.select(row['session_id'])
        booking = Booking(member, session, row['id'])
        bookings.append(booking)
    return bookings



# deleting all bookings - dont use here!
def delete_all():
    sql = "DELETE FROM bookings"
    run_sql(sql)


# deleting a specific booking
def delete(id):
    sql = "DELETE FROM bookings WHERE id = %s"
    values = [id]
    run_sql(sql, values)


