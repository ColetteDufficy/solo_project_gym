from db.run_sql import run_sql
from models.gym import Gym
import repositories.member_repository as member_repository
import repositories.session_repository as session_repository



def save(gym):
    sql = "INSERT INTO gyms ( member_id, session_id) VALUES ( %s, %s ) RETURNING id"
    values = [gym.member.id, gym.session.id]
    results = run_sql( sql, values )
    gym.id = results[0]['id']
    return gym


def select_all():
    gyms = []

    sql = "SELECT * FROM gyms"
    results = run_sql(sql)

    for row in results:
        member = member_repository.select(row['member_id'])
        session = session_repository.select(row['session_id'])
        gym = Gym(member, session, row['id'])
        gyms.append(gym)
    return gyms


def delete_all():
    sql = "DELETE FROM gyms"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM gyms WHERE id = %s"
    values = [id]
    run_sql(sql, values)
