import unittest
from datetime import datetime
from context import hotel_system
from hotel_system.hotel_chain import HotelChain
from hotel_system.hotel import Hotel

class TestHotelChainMethods(unittest.TestCase):
    def test_calculate_cheapest_hotel_equal_stars_reward_customer(self):
        hotel1 = Hotel('hotel1', 3, 70, 60, 90, 50)   # 60+50+50 = 160
        hotel2 = Hotel('hotel2', 3, 85, 35, 110, 90)  # 35+90+90 = 215
        hotel3 = Hotel('hotel3', 3, 68, 65, 50, 45)   # 65+45+45 = 155

        dates = [datetime(2019, 11, 1), datetime(2019, 11, 2), datetime(2019, 11, 3)]

        hotel_chain = HotelChain()
        hotel_chain.add_hotel(hotel1)
        hotel_chain.add_hotel(hotel2)
        hotel_chain.add_hotel(hotel3)

        self.assertEqual(hotel_chain.calculate_cheapest_hotel(dates, 'Reward'), 'hotel3')


    def test_calculate_cheapest_hotel_equal_stars_regular_customer(self):
        hotel1 = Hotel('hotel1', 3, 60, 60, 50, 50)   # 60+50+50   = 160
        hotel2 = Hotel('hotel2', 3, 85, 35, 110, 90)  # 85+110+110 = 305
        hotel3 = Hotel('hotel3', 3, 68, 65, 50, 45)   # 68+50+50   = 168

        dates = [datetime(2019, 11, 1), datetime(2019, 11, 2), datetime(2019, 11, 3)]

        hotel_chain = HotelChain()
        hotel_chain.add_hotel(hotel1)
        hotel_chain.add_hotel(hotel2)
        hotel_chain.add_hotel(hotel3)

        self.assertEqual(hotel_chain.calculate_cheapest_hotel(dates, 'Regular'), 'hotel1')


    def test_calculate_cheapest_hotel_different_stars_reward_customer(self):
        hotel1 = Hotel('hotel1', 4, 70, 60, 90, 50)   # 60+50+50 = 160
        hotel2 = Hotel('hotel2', 3, 85, 35, 110, 90)  # 35+90+90 = 215
        hotel3 = Hotel('hotel3', 5, 68, 65, 50, 45)   # 65+45+45 = 155

        dates = [datetime(2019, 11, 1), datetime(2019, 11, 2), datetime(2019, 11, 3)]

        hotel_chain = HotelChain()
        hotel_chain.add_hotel(hotel1)
        hotel_chain.add_hotel(hotel2)
        hotel_chain.add_hotel(hotel3)

        self.assertEqual(hotel_chain.calculate_cheapest_hotel(dates, 'Reward'), 'hotel3')


    def test_calculate_cheapest_hotel_different_stars_regular_customer(self):
        hotel1 = Hotel('hotel1', 5, 60, 60, 50, 50)   # 60+50+50   = 160
        hotel2 = Hotel('hotel2', 3, 85, 35, 110, 90)  # 85+110+110 = 305
        hotel3 = Hotel('hotel3', 4, 68, 65, 50, 45)   # 68+50+50   = 168

        dates = [datetime(2019, 11, 1), datetime(2019, 11, 2), datetime(2019, 11, 3)]

        hotel_chain = HotelChain()
        hotel_chain.add_hotel(hotel1)
        hotel_chain.add_hotel(hotel2)
        hotel_chain.add_hotel(hotel3)

        self.assertEqual(hotel_chain.calculate_cheapest_hotel(dates, 'Regular'), 'hotel1')
