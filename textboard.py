from turtle import Turtle
from vars import PLAYER_1, PLAYER_2, COMPUTER, PLAYER_SCORE_POSITION, COMPUTER_SCORE_POSITION, SCORE_FONT, TEXT_FONT, FIRST_TO_X, MAX_SCORE

class TextBoard(Turtle):
  """The scoreboard blueprint."""
  def __init__(self, player_type=None, not_score_text=None, initial_message=None) -> None:
    super().__init__()
    self.score = 0
    self.max_score = MAX_SCORE
    self.hideturtle()
    self.penup()
    self.color("white")
    self.text_message = not_score_text

    if initial_message:
      self.first_to_x_goals()

    if player_type != None:
      self.set_score_positions(player_type)

    if not_score_text:
      self.text_helper_refresh()

  def set_score_positions(self, player_type):
    """Positions the score on the screen."""
    if player_type == PLAYER_1:
      self.goto(PLAYER_SCORE_POSITION)
    elif player_type == PLAYER_2 or player_type == COMPUTER:
      self.goto(COMPUTER_SCORE_POSITION)
    self.refresh(self.score, "left", SCORE_FONT)

  def refresh(self, text, align, font):
    """Refreshes the text."""
    if self.text_message == None:
      self.clear_text()
    self.write(arg=text, align=align, font=font)
  
  def text_helper_refresh(self):
    """Helps to create the text pipes | accross the screen."""
    y_range = [y for y in range(-300, 300, 30)]
    for y in y_range[0:-1:2]:
      self.goto(0, y)
      self.refresh("|", "center", TEXT_FONT)
  
  def increase_score(self):
    """Increases the score."""
    self.score += 1
    self.refresh(self.score, "left", SCORE_FONT)
  
  def first_to_x_goals(self):
    """Displays first to {max_score}!"""
    self.refresh(f"First to score {self.max_score} wins the game, Good luck!", "center", FIRST_TO_X)
  
  def clear_text(self):
    self.clear()
  
  def return_the_winner(self, message) -> str:
    """Returns and congratulates the winner!"""
    self.refresh(message, "center", FIRST_TO_X)