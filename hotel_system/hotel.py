WEEKEND = [5, 6]  # Saturday = 5, Sunday = 6


class Hotel:
    """
    A class to represent a hotel.

    Attributes:
    -----------
    name: str
        The hotel's name
    stars: int
        Number of stars the hotel was classified from 1 to 5
    workweek_regular_fee: int
        Fee for a workweek day for a regular customer
    workweek_rewards_fee: int
        Fee for a workweek day for a rewards customer
    weekend_regular_fee: int
        Fee for a weekend day for a regular customer
    weekend_rewards_fee:
        Fee for a weekend day for a rewards customer

    Methods:
    --------
    calculate_total_fee(date_list, customer_category)
        Calculates the total fee for a period for a specific customer category (Regular
        or Rewards)

    """

    def __init__(self, name, stars, workweek_regular_fee, workweek_rewards_fee,
                 weekend_regular_fee, weekend_rewards_fee, blackout_days=[]):
        self.name = name
        self.stars = stars
        self.workweek_regular_fee = workweek_regular_fee
        self.workweek_rewards_fee = workweek_rewards_fee
        self.weekend_regular_fee = weekend_regular_fee
        self.weekend_rewards_fee = weekend_rewards_fee
        self.blackout_days = blackout_days

    def calculate_total_fee(self, date_list, customer_category):
        """Calculates the total fee due for a specific customer in a period

        Parameters:
        date_list (list of datetime): Period the customer will stay in the hotel
        customer_category (string): Customer category that will define the fees

        Returns:
        int: Total fee due for customer in the period specified
        """
        
        total_fee = 0

        workweek_fee = self.workweek_regular_fee if customer_category == 'Regular' else self.workweek_rewards_fee
        weekend_fee = self.weekend_regular_fee if customer_category == 'Regular' else self.weekend_rewards_fee

        for date in date_list:
            if date.weekday() in WEEKEND:
                if date in self.blackout_days:
                    total_fee += self.weekend_regular_fee
                else:
                    total_fee += weekend_fee
            else:
                if date in self.blackout_days:
                    total_fee += self.workweek_regular_fee
                else:
                    total_fee += workweek_fee

        return total_fee

    def is_blackout_day(self, date):
        return date in self.blackout_days