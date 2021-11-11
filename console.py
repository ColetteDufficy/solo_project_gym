import pdb
from models.session import Session
from models.member import Member
from models.booking import Booking

import repositories.session_repository as session_repository
import repositories.member_repository as member_repository
import repositories.booking_repository as booking_repository

booking_repository.delete_all()
session_repository.delete_all()
member_repository.delete_all()

member1 = Member('Ollie', 'Hodges', 'o.hodges@email.com', True)
member_repository.save(member1)

member2 = Member('Mary', 'OBrien', 'm.obrien@email.com', False)
member_repository.save(member2)

member3 = Member('Dora', 'Allman', 'd.allman@email.com', True)
member_repository.save(member3)

member4 = Member('Jack', 'Jackman', 'j.jackman@email.com', True)
member_repository.save(member4)

session1 = Session('Spinning', '45mins', 5)
session_repository.save(session1)

session2 = Session('Boxercise', '30mins', 8)
session_repository.save(session2)

session3 = Session('Zumba', '60mins', 15)
session_repository.save(session3)

booking1 = Booking(member1, session2)
booking_repository.save(booking1)

booking2 = Booking(member1, session1)
booking_repository.save(booking2)

booking3 = Booking(member3, session2)
booking_repository.save(booking3)


