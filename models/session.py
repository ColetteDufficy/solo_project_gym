class Session:

    def __init__(self, session_name, time, max_capacity, id = None):
        self.session_name = session_name
        self.time = time
        self.max_capacity = max_capacity
        self.id = id