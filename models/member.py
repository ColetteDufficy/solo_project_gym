class Member:

    def __init__(self, first_name, last_name, email, active_member, id = None):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.active_member = active_member
        self.id = id

    def active_member(self):
        self.active = True