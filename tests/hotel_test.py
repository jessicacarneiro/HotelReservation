import unittest
from datetime import datetime
from context import hotel_system
from hotel_system.hotel import Hotel
from hotel_system.customer import Customer

class TestHotelChainMethods(unittest.TestCase):
    def test_calculate_fee_for_zero_days_regular_customer(self):
        hotel = Hotel('Hotel 1', 3, 100, 90, 150, 100)
        customer = Customer('Customer 1', 'Regular')
        date_list = []
        self.assertEqual(hotel.calculate_total_fee(date_list, customer.category), 0)


    def test_calculate_fee_for_zero_days_reward_customer(self):
        hotel = Hotel('Hotel 2', 5, 150, 120, 190, 150)
        customer = Customer('Customer 2', 'Rewards')
        date_list = []
        self.assertEqual(hotel.calculate_total_fee(date_list, customer.category), 0)


    def test_calculate_fee_for_one_workweek_day_regular_customer(self):
        hotel = Hotel('Hotel 1', 3, 100, 90, 150, 100)
        customer = Customer('Customer 1', 'Regular')
        date_list = [datetime(2019, 11, 1)]
        self.assertEqual(hotel.calculate_total_fee(date_list, customer.category), 100)


    def test_calculate_fee_for_two_workweek_day_regular_customer(self):
        hotel = Hotel('Hotel 2', 5, 150, 120, 190, 150)
        customer = Customer('Customer 1', 'Regular')
        date_list = [datetime(2019, 10, 31), datetime(2019, 11, 1)]
        self.assertEqual(hotel.calculate_total_fee(date_list, customer.category), 300)


    def test_calculate_fee_for_one_weekend_day_regular_customer(self):
        hotel = Hotel('Hotel 1', 3, 100, 90, 150, 100)
        customer = Customer('Customer 1', 'Regular')
        date_list = [datetime(2019, 11, 2)]
        self.assertEqual(hotel.calculate_total_fee(date_list, customer.category), 150)


    def test_calculate_fee_for_two_weekend_day_regular_customer(self):
        hotel = Hotel('Hotel 2', 5, 150, 120, 190, 150)
        customer = Customer('Customer 1', 'Regular')
        date_list = [datetime(2019, 11, 2), datetime(2019, 11, 3)]
        self.assertEqual(hotel.calculate_total_fee(date_list, customer.category), 380)


    def test_calculate_fee_for_one_workweek_day_reward_customer(self):
        hotel = Hotel('Hotel 1', 3, 100, 90, 150, 100)
        customer = Customer('Customer 2', 'Rewards')
        date_list = [datetime(2019, 11, 1)]
        self.assertEqual(hotel.calculate_total_fee(date_list, customer.category), 90)


    def test_calculate_fee_for_two_workweek_day_reward_customer(self):
        hotel = Hotel('Hotel 2', 5, 150, 120, 190, 150)
        customer = Customer('Customer 2', 'Rewards')
        date_list = [datetime(2019, 10, 31), datetime(2019, 11, 1)]
        self.assertEqual(hotel.calculate_total_fee(date_list, customer.category), 240)


    def test_calculate_fee_for_one_weekend_day_reward_customer(self):
        hotel = Hotel('Hotel 1', 3, 100, 90, 150, 100)
        customer = Customer('Customer 2', 'Rewards')
        date_list = [datetime(2019, 11, 2)]
        self.assertEqual(hotel.calculate_total_fee(date_list, customer.category), 100)


    def test_calculate_fee_for_two_weekend_day_reward_customer(self):
        hotel = Hotel('Hotel 2', 5, 150, 120, 190, 150)
        customer = Customer('Customer 2', 'Rewards')
        date_list = [datetime(2019, 11, 2), datetime(2019, 11, 3)]
        self.assertEqual(hotel.calculate_total_fee(date_list, customer.category), 300)


    def test_calculate_fee_for_mixed_days_day_regular_customer(self):
        hotel = Hotel('Hotel 1', 3, 100, 90, 150, 100)
        customer = Customer('Customer 1', 'Regular')
        date_list = [datetime(2019, 11, 1), datetime(2019, 11, 2)]
        self.assertEqual(hotel.calculate_total_fee(date_list, customer.category), 250)


    def test_calculate_fee_for_mixed_days_day_reward_customer(self):
        hotel = Hotel('Hotel 2', 5, 150, 120, 190, 150)
        customer = Customer('Customer 2', 'Rewards')
        date_list = [datetime(2019, 11, 1), datetime(2019, 11, 2)]
        self.assertEqual(hotel.calculate_total_fee(date_list, customer.category), 270)

    def test_calculate_number_of_reward_days(self):
        hotel = Hotel('Hotel 3', 5, 150, 100, 150, 120, [datetime(2019, 12, 25)])
        number_reward_days = hotel.is_blackout_day(datetime(2019, 12, 25))
        self.assertEqual(number_reward_days, True)

    def test_calculate_fee_with_blackout_days(self):
        hotel = Hotel('Hotel 2', 5, 150, 120, 190, 150, [datetime(2019, 12, 25)])
        customer = Customer('Customer 2', 'Rewards')
        date_list = [datetime(2019, 12, 25), datetime(2019, 12, 26)]
        self.assertEqual(hotel.calculate_total_fee(date_list, customer.category), 270)
    
    def test_calculate_fee_with_blackout_days_longer_list(self):
        hotel = Hotel('Hotel 2', 5, 150, 120, 190, 150, [datetime(2019, 12, 25), datetime(2019, 12, 26), datetime(2019, 12, 27)])
        customer = Customer('Customer 2', 'Rewards')
        date_list = [datetime(2019, 12, 24), datetime(2019, 12, 25), datetime(2019, 12, 26)]
        self.assertEqual(hotel.calculate_total_fee(date_list, customer.category), 420)