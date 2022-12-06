class Bookings:
    def __init__(self, user_id, studio_id, date, time, attendees, id=None):
        self.user_id = user_id
        self.studio_id = studio_id
        self.date = date
        self.time = time
        self.attendees = attendees
        self.id = id