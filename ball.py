from turtle import Turtle
from vars import *
# NORTH_EAST, NORTH_WEST, SOUTH_EAST, SOUTH_WEST, EAST, WEST, BALL_STARTING_POSITION, BALL_STARTING_ANGLE, BALL_SPEED, BALL_HEIGHT, BALL_WIDTH, INITIAL_BALL_TRAVEL, NE, NW, SW, SE, E, W

class Ball(Turtle):
  """Ball blueprint"""
  def __init__(self, ball_speed=MEDIUM_BALL_SPEED) -> None:
    super().__init__()
    self.shape("square")
    self.color("white")
    self.penup()
    self.ball_speed = ball_speed
    self.speed("fastest")
    self.shapesize(stretch_wid=BALL_WIDTH, stretch_len=BALL_HEIGHT)
    self.refresh()

  def refresh(self):
    """Sets the balls starting coordinates."""
    self.goto(BALL_STARTING_POSITION)
    self.setheading(BALL_STARTING_ANGLE)
    self.traveling = INITIAL_BALL_TRAVEL

  def move(self) -> None:
    """Moves the ball."""
    self.fd(self.ball_speed)
  
  def change_speed(self, speed) -> None:
    """Changes the speed of the ball."""
    if speed == FAST_BALL_SPEED:
      self.ball_speed = FAST_BALL_SPEED
    else:
      self.ball_speed = MEDIUM_BALL_SPEED
    

  def north_east(self) -> None:
    """Positions the ball towards the northeast."""
    self.setheading(NORTH_EAST)
    self.traveling = NE
  
  def north_west(self) -> None:
    """Positions the ball towards the northwest."""
    self.setheading(NORTH_WEST)
    self.traveling = NW

  def south_east(self) -> None:
    """Positions the ball towards the southeast."""
    self.setheading(SOUTH_EAST)
    self.traveling = SE

  def south_west(self) -> None:
    """Positions the ball towards the southwest."""
    self.setheading(SOUTH_WEST)
    self.traveling = SW

  def east(self) -> None:
    """Positions the ball towards the east."""
    self.setheading(EAST)
    self.traveling = E

  def west(self) -> None:
    """Positions the ball towards the west."""
    self.setheading(WEST)
    self.traveling = W