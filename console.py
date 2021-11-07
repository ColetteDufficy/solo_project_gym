import pdb
from models.session import Session
from models.member import Member
from models.gym import Gym

import repositories.session_repository as session_repository
import repositories.member_repository as member_repository
import repositories.gym_repository as gym_repository

gym_repository.delete_all()
session_repository.delete_all()
member_repository.delete_all()

member1 = Member('Ollie', 'Hodges', 'o.hodges@email.com', True)
member_repository.save(member1)

member2 = Member('Mary', 'OBrien', 'm.obrien@email.com', False)
member_repository.save(member2)

member3 = Member('Dora', 'Allman', 'd.allman@email.com', True)
member_repository.save(member3)

session1 = Session('Spinning', '45mins', 5)
session_repository.save(session1)

session2 = Session('Boxercise', '30mins', 8)
session_repository.save(session2)

gym1 = Gym(member1, session2)
gym_repository.save(gym1)

gym2 = Gym(member3, session1)
gym_repository.save(gym2)

gym3 = Gym(member2, session2)
gym_repository.save(gym3)


pdb.set_trace()
