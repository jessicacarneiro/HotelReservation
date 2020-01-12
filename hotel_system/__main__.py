import sys
from .file_handler import read_file
from .hotel import Hotel
from .customer import Customer
from .hotel_chain import HotelChain

if __name__ == "__main__":
    if len(sys.argv) < 2:
        exit('Usage: python -m hotel_system <file>')

    lakewood = Hotel('Lakewood', 3, 110, 80, 90, 80)
    bridgewood = Hotel('Bridgewood', 4, 160, 110, 60, 50)
    ridgewood = Hotel('Ridgewood', 5, 220, 100, 150, 40)

    hotel_chain = HotelChain()
    hotel_chain.add_hotel(lakewood)
    hotel_chain.add_hotel(bridgewood)
    hotel_chain.add_hotel(ridgewood)

    file_data = read_file(sys.argv[1])

    customer = Customer(category=file_data[0])
    dates = file_data[1]

    cheapest_hotel = hotel_chain.calculate_cheapest_hotel(dates, customer.category)
    print(cheapest_hotel)