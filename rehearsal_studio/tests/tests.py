import unittest
import datetime
from models.bookings import Bookings


class TestBooking(unittest.TestCase):
    
    def setUp(self):
        self.booking1 = Bookings("Jim Bobb", 2, datetime.date(2022, 12, 12), datetime.time(13,00,00), 4)

    @unittest.skip("Testing something else")
    def test_booking_name(self):
        self.assertEqual("Jim Bobb", self.booking1.booking_name)


