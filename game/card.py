import random


class Cards:
    """
    Cards represented as a number from 1 - 13
    The resposibility of the cards is to keep track of the card that is drawn and calculate the points for it.
    
    Attributes:
    value(int): the card value [from 1 to 13]
    points(int): correct guess = +100, incorrect guess = -75
    """

    # 2) Create the class constructor. Use the following method comment.
    def __init__(self):
        """Constructs a new instance of Cards with a value and points attribute.

        Args:
            self (Cards): An instance of Cards.
        """
        self.value = 0
        

    def draw(self):
        """Generates a new random value from 1 to 13
        
        Args:
            self (Cards): An instance of cards.
        """
        self.value = random.randint(1, 13)
        