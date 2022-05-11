
"""
    Update the code and the comments as you change the code for your game.  You will be graded on following the
    Rules listed and your program meets all of the Requirements found on 
    https://byui-cse.github.io/cse210-course-competency/abstraction/materials/hilo-specification.html
"""
from game.card import Cards

class Director:
    """A person who directs the game. 

    The responsibility of a Director is to control the sequence of play.

    Attributes:
        is_playing (boolean): Whether or not the game is being played.
        score (int): The score for the game.
        is_higher (boolean): whether drawn card is higher or not.
        card_1 (int): The first drawn card.
        card_2 (int): The second drawn card.
        again (string): users input to play again [y/n].   
    """

    def __init__(self):
        """Constructs a new Director.

        Args:
            self (Director): an instance of Director.
        """
        self.is_playing = True
        self.is_higher = True
        self.card_1 = 0
        self.card_2 = 2
        self.score = 300
        self.again = "n"
        

    def start_game(self):
        """Starts the game by running the main game loop.

        Args:
            self (Director): an instance of Director.
        """
        while self.is_playing:
            self.get_inputs()
            self.do_updates()
            self.do_outputs()
            self.is_playing = (self.again == "y")
            
    def get_inputs(self):
        """Ask the user if they want to draw a card.

        Args:
            self (Director): An instance of Director.
        """
        # An instance of card called c_init
        c_init = Cards()
        c_init.draw()
        self.card_1 = c_init.value

        
        print("")
        print(f"The card is: {self.card_1}")
        higher = input("Higher or lower? [h/l] ")
        self.is_higher = (higher == "h")

   
    def do_updates(self):
        """Updates the player's score.

        Args:
            self (Director): An instance of Director.
        """
        if not self.is_playing:
            return
        # An instance of card called c_final
        c_final = Cards()
        c_final.draw()
        self.card_2 = c_final.value

        #Main Game logic
        if self.is_higher:
            if self.card_2 > self.card_1: 
                self.score += 100
            else: self.score -= 75
        else:
            if self.card_2 < self.card_1: 
                self.score += 100
            else: self.score -= 75
        


    def do_outputs(self):
        """Displays the dice and the score. Also asks the player if they want to roll again. 

        Args:
            self (Director): An instance of Director.
        """
        if not self.is_playing:
            return
       
        print(f"Next card was: {self.card_2}")
        print(f"Your score is: {self.score}")
        self.again = input("Play again? [y/n] ")