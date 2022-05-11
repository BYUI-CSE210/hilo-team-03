
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
        self.cards = []
        self.second_cards =[]
        self.is_playing = True
        self.score = 0
        self.total_score = 300

        card = cards()
        second_card = cards()
        self.cards.append(card)
        self.second_cards.append(second_card)

    def start_game(self):
        """Starts the game by running the main game loop.

        Args:
            self (Director): an instance of Director.
        """
        while self.is_playing:
            self.get_inputs()
            self.do_updates()
            self.do_outputs()

    def get_inputs(self):
        """Ask the user if they want to draw a card.

        Args:
            self (Director): An instance of Director.
        """
        starting_card = print(f"The card is: {cards.draw}.")
        draw_card = input("Higher or lower? [h/l] ")
        self.is_playing = (draw_card == "y")


    def do_updates(self):
        """Updates the player's score.

        Args:
            self (Director): An instance of Director.
        """
        if not self.is_playing:
            return

        card = cards.draw()
        if card > starting_card

        self.score += cards.points
        self.total_score += self.score

    def do_outputs(self):
        """Displays the dice and the score. Also asks the player if they want to roll again. 

        Args:
            self (Director): An instance of Director.
        """
        if not self.is_playing:
            return

        values = ""
        for i in range(len(self.cards)):
            card = self.cards[i]
            values += f"{card.value}"

        print(f"The card is: {values}")
        print(f"Your score is: {self.total_score}")
        self.is_playing == (self.score > 0)