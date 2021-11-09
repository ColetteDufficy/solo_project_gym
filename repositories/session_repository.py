from db.run_sql import run_sql
from models.session import Session
from models.member import Member


# To see list of all session
def select_all():
    sessions = []

    sql = "SELECT * FROM sessions"
    results = run_sql(sql)

    for row in results:
        session = Session(row['session_name'], row['time'], row['max_capacity'], row['id'])
        sessions.append(session)
    return sessions



# To save a new session, eg adding a new session to the over all sessions list.
def save(session):
    sql = "INSERT INTO sessions(session_name, time, max_capacity) VALUES ( %s, %s, %s) RETURNING id"
    values = [session.session_name, session.time, session.max_capacity]
    results = run_sql( sql, values )
    session.id = results[0]['id']
    return session



# to edit a specific sessions details, where ID number is X
def update(session):
    sql = "UPDATE sessions SET ( session_name, time, max_capacity ) = (%s, %s, %s) WHERE id = %s"
    values = [session.session_name, session.time, session.max_capacity, session.id]
    run_sql(sql, values)
    




# select a specific session
def select(id):
    session = None
    sql = "SELECT * FROM sessions WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        session = Session(result['session_name'], result['time'], result['max_capacity'], result['id'] )
    return session


# delete all sessions - dont use this here!
def delete_all():
    sql = "DELETE FROM sessions"
    run_sql(sql)
    
    
    
def members(session):
    members = []

    sql = "SELECT members.* FROM members INNER JOIN visits ON visits.member_id = members.id WHERE session_id = %s"
    values = [session.id]
    results = run_sql(sql, values)
    
    for row in results:
        member = Member(row['first_name'], row['last_name'], row['email'], row['active_member'], row['id'])
        members.append(member)
    
    return members