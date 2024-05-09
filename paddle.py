from turtle import Turtle
from vars import PLAYER_1_STARTING_POSITION, PLAYER_2_STARTING_POSITION, DIRECTION, SOUTH, NORTH, PLAYER_SPEED, COMPUTER_SPEED, HEIGHT, PADDLE_WIDTH, PADDLE_HEIGHT
# 

class Paddle:
  """Paddle Blueprint"""
  def __init__(self, player_type="player 1", difficulty="hard", human=False) -> None:
    STARTING_POSITIONS = PLAYER_1_STARTING_POSITION
    if player_type == "player 2" or player_type == "computer":
      STARTING_POSITIONS = PLAYER_2_STARTING_POSITION
    self.paddle = [self.add_segment(segment, DIRECTION) for segment in STARTING_POSITIONS]
    self.player_type = player_type
    self.human = human
  
  def add_segment(self, position, direction) -> Turtle:
    """Creats segments for the paddle. Then in the end the method returns a segment."""
    paddle = Turtle(shape="square")
    paddle.penup()
    paddle.color("white")
    paddle.shapesize(stretch_wid=PADDLE_WIDTH, stretch_len=PADDLE_HEIGHT)
    paddle.goto(position)
    paddle.setheading(direction)
    return paddle
  
  def up(self) -> None:
    """Positions/faces the paddle upwards, then moves it."""
    if self.paddle[0].ycor() < HEIGHT / 2 - 20:
      for segment in self.paddle:
        segment.setheading(NORTH)
        if self.human:
          self.segment_move(segment, PLAYER_SPEED)
  
  def down(self) -> None:
    """Positions/faces the paddle downwards, then moves it."""
    if self.paddle[-1].ycor() > -HEIGHT / 2 + 20:
      for segment in self.paddle:
        segment.setheading(SOUTH)
        if self.human:
          self.segment_move(segment, PLAYER_SPEED)

  def segment_move(self, segment, given_speed) -> None:
    """Moves the paddle."""
    segment.fd(given_speed)

  def move(self) -> None:
    """Moves the paddle."""
    for segment in self.paddle:
      self.segment_move(segment, COMPUTER_SPEED)