
"""
    Update the code and the comments as you change the code for your game.  You will be graded on following the
    Rules listed and your program meets all of the Requirements found on 
    https://byui-cse.github.io/cse210-course-competency/abstraction/materials/hilo-specification.html
"""
from game.card import cards
class Director:
    """A person who directs the game. 

    The responsibility of a Director is to control the sequence of play.

    Attributes:
        cards (List[cards]): a list of cards instances.
        is_playing (boolean): Whether or not the game is being played.
        score (int): The score for one round of play.
        total_score (int): The score for the entire game.
    """

    def __init__(self):
        """Constructs a new Director.

        Args:
            self (Director): an instance of Director.
        """
        self.is_playing = True
        self.is_higher = True
        self.total_score = 300
        cards = Cards()
        cards.draw()
        self.card = cards.value
        cards.draw()
        self.second_card = cards.value
        

    def start_game(self):
        """Starts the game by running the main game loop.

        Args:
            self (Director): an instance of Director.
        """
        while self.is_playing:
            print(f"The card is: {self.card}")
            self.get_inputs()
            self.do_updates()
            self.do_outputs()
            again = input("Play again? [y/n] ")
            self.is_playing = (again == "y")

    def get_inputs(self):
        """Ask the user if they want to draw a card.

        Args:
            self (Director): An instance of Director.
        """
        
        draw_card = input("Higher or lower? [h/l] ")
        self.is_higher = (draw_card == "h")


    def do_updates(self):
        """Updates the player's score.

        Args:
            self (Director): An instance of Director.
        """
        if not self.is_playing:
            return

        print(f"Next card was: {self.second_card}")
        if self.is_higher:
            if self.second_card > self.card:
                self.total_score += 100
            else: self.total_score -= 75
        else :
            if self.second_card < self.card:
                self.total_score += 100
            else: self.total_score -= 75 

        
                

    def do_outputs(self):
        """Displays the dice and the score. Also asks the player if they want to roll again. 

        Args:
            self (Director): An instance of Director.
        """
        if not self.is_playing:
            return
        print(f"Your score is: {self.total_score}")

        