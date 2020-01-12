class Customer:
    """
    A class to represent a customer in the hotel chain system.

    Attributes:
    -----------
    name: str
        The customer's name
    category: str
        The customer's category that can be 'Regular' or 'Rewards'
    """
    
    def __init__(self, name=None, category='Regular'):
        self.name = name
        self.category = category