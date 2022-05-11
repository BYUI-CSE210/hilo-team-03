import random

# 1) Add the class declaration. Use the following class comment.


class cards:
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
        self.points = 300

    # 3) Create the draw(self) method. Use the following method comment.
    def draw(self):
        """Generates a new random value from 1 to 13 [I already imported the random library]
        
        Args:
            self (Cards): An instance of cards.
        """
        self.value = random.randint(1, 13)
        self.points = 100 if correct_guess == True else -75 if incorrect_guess == True
