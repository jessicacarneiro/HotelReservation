import sys


class HotelChain:

    def __init__(self):
        self.hotels = []

    def add_hotel(self, hotel):
        self.hotels.append(hotel)

    def calculate_cheapest_hotel(self, dates, customer_category):
        hotels = []

        for hotel in self.hotels:
            price = hotel.calculate_total_fee(dates, customer_category)
            hotels.append({'name': hotel.name, 'price': price, 'stars': hotel.stars})

        cheapest_hotel = None
        cheapest_hotel_price = sys.maxsize

        for hotel in hotels:
            if hotel['price'] < cheapest_hotel_price:
                cheapest_hotel = hotel
                cheapest_hotel_price = hotel['price']
            elif hotel['price'] == cheapest_hotel_price:
                if hotel['stars'] > cheapest_hotel['stars']:
                    cheapest_hotel = hotel

        return cheapest_hotel['name']
