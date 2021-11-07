from db.run_sql import run_sql
from models.session import Session
from models.member import Member



def select_all():
    members = []

    sql = "SELECT * FROM members"
    results = run_sql(sql)
    for row in results:
        member = Member(row['first_name'], row['last_name'], row['email'], row['active_member'], row['id'])
        members.append(member)
    return members



def delete_all():
    sql = "DELETE FROM members"
    run_sql(sql)
    


