from db.run_sql import run_sql
from models.session import Session
from models.member import Member


# To see list of all members
def select_all():
    members = []

    sql = "SELECT * FROM members"
    results = run_sql(sql)
    for row in results:
        member = Member(row['first_name'], row['last_name'], row['email'], row['active_member'], row['id'])
        members.append(member)
    return members



def select_all_alphabetical():
    members = []

    sql = "SELECT * FROM members ORDER BY first_name"
    results = run_sql(sql)
    for row in results:
        member = Member(row['first_name'], row['last_name'], row['email'], row['active_member'], row['id'])
        members.append(member)
    return members



def select_all_active():
    members = []

    sql = "SELECT * FROM members WHERE active_member IN ('True')"
    results = run_sql(sql)
    for row in results:
        member = Member(row['first_name'], row['last_name'], row['email'], row['active_member'], row['id'])
        members.append(member)
    return members





# To save a new member, eg adding anew member to the over all members list.
def save(member):
    sql = "INSERT INTO members( first_name, last_name, email, active_member ) VALUES ( %s, %s, %s, %s ) RETURNING id"
    values = [member.first_name, member.last_name, member.email, member.active_member]
    results = run_sql( sql, values )
    member.id = results[0]['id']
    return member




# to edit a specific member details, where ID number is X
def update(member):
    sql = "UPDATE members SET ( first_name, last_name, email, active_member ) = (%s, %s, %s, %s) WHERE id = %s"
    values = [member.first_name, member.last_name, member.email, member.active_member, member.id]
    run_sql(sql, values)
    



# delete all members - dont use this here!
def delete_all():
    sql = "DELETE FROM members"
    run_sql(sql)
    
    
    
# select a specific member
def select(id):
    member = None
    sql = "SELECT * FROM members WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        member = Member(result['first_name'], result['last_name'], result['email'], result['active_member'], result['id'] )
    return member

    





