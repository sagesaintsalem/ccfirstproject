from models.studio import Studio
from models.user import User
from models.bookings import Bookings
import repos.booking_repo as booking_repo
import repos.studio_repo as studio_repo
import repos.user_repo as user_repo
import datetime



user1 = User("Jim Bobb")
user_repo.create_user(user1)
user2 = User("Envy Adams")
user_repo.create_user(user2)


studio1 = Studio(1)
studio_repo.create_studio(studio1)
studio2 = Studio(2)
studio_repo.create_studio(studio2)
studio3 = Studio(3)
studio_repo.create_studio(studio3)


booking1 = Bookings(user1, studio1.id, datetime.date(2022, 12, 12), "13:00", 4)
booking_repo.create_booking(booking1)
booking2 = Bookings(user2, studio2.id, datetime.date(2022, 12, 13), "11:00", 3)
booking_repo.create_booking(booking2)


