class Reservation:
    """
    A class to represent a reservation made by a customer in a hotel.

    Attributes:
    -----------
    dates: list<datetime>
        A list with the dates the customer will be staying in the hotel
    customer: Customer
        The customer that made the reservation
    hotel: Hotel
        The hotel chosen by the customer
    price: int
        The total fee the customer should pay

    Methods:
    --------
    make_reservation(dates, customer, hotel)
        Creates an instance of Reservation with the total fee calculated

    """

    def __init__(self, dates=None, customer=None, hotel=None, price=0):
        self.dates = dates
        self.customer = customer
        self.hotel = hotel
        self.price = price

    @classmethod
    def make_reservation(dates, customer, hotel):
        """Create an instance of Reservation

        Parameters:
        dates (list of datetime): Dates to reserve the hotel
        customer (Customer): The customer tha will stay in the hotel
        hotel (hotel): The hotel chosen

        Returns:
        Reservation: An instance of Reservation
        """
        
        total_fee = hotel.calculate_total_fee(dates, customer.category)
        return Reservation(dates, customer, hotel, total_fee)