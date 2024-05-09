import time
import random
from turtle import Screen
from paddle import Paddle
from ball import Ball
from textboard import TextBoard
from vars import WIDTH, HEIGHT, EASY_MODE_INTELIGENCE, MEDIUM_MODE_INTELIGENCE, HARD_MODE_INTELIGENCE, PLAYER_1, PLAYER_2, COMPUTER, NE, NW, SW, SE, MAX_SCORE, MEDIUM_BALL_SPEED, FAST_BALL_SPEED

screen = Screen()

screen.setup(width=WIDTH, height=HEIGHT)
screen.bgcolor("black")
screen.title("My Pong Game")
screen.tracer(0)

multiplayer_game_mode = screen.textinput("Game Mode", "Want to play as 2 players? (yes/no): ").lower()
game_difficulty = screen.textinput("Game Difficulty Level.", "How difficult would you like the game to be? (easy/medium/hard): ").lower()
dif_idx = 0
if game_difficulty == "easy":
  dif_idx = EASY_MODE_INTELIGENCE
elif game_difficulty == "medium":
  dif_idx = MEDIUM_MODE_INTELIGENCE
else:
  dif_idx = HARD_MODE_INTELIGENCE
difficulty_level = ["seek" for _ in range(0, dif_idx)]
difficulty_level.append("miss")
random.shuffle(difficulty_level)

human = False
multiplayer = COMPUTER
if multiplayer_game_mode == "yes":
  multiplayer = PLAYER_2
  human = True

player = Paddle(human=True)
computer = Paddle(player_type=multiplayer, human=human)
ball = Ball(ball_speed=FAST_BALL_SPEED if game_difficulty == "hard" else MEDIUM_BALL_SPEED)
player_score = TextBoard(player_type=PLAYER_1)
computer_score = TextBoard(player_type=COMPUTER)
text = TextBoard(not_score_text=True)
text_2 = TextBoard(initial_message=True)

player_1 = PLAYER_1[0].upper() + PLAYER_1[1:].lower()
player_2_type = COMPUTER[0].upper() + COMPUTER[1:].lower()

paddle_length = len(player.paddle)

screen.listen()

if multiplayer_game_mode == "yes":
  player_2_type = PLAYER_2[0].upper() + PLAYER_2[1:].lower()
  screen.onkey(computer.up, "Up")
  screen.onkey(computer.down, "Down")
  screen.onkey(player.up, "w")
  screen.onkey(player.down, "s")
else:
  screen.onkey(player.up, "Up")
  screen.onkey(player.down, "Down")

game_on = True

while game_on:
  screen.tracer(0)
  screen.update()
  time.sleep(0.08)
  ball.move()
  difficulty_random_idx = random.randint(0, dif_idx)
  direction_random = random.randint(0, 1)
  # After the first goal clear the clear the instruction text from the screen.
  if player_score.score > 0 or computer_score.score > 0:
    text_2.clear_text()

  # if multiplayer is off 
  if multiplayer_game_mode == "no":
    # Computer seeks the ball position in order to hit it. Computer inteligence is incread based on the difficulty level.
    if difficulty_level[difficulty_random_idx] == "seek" and ball.xcor() > 0:
      if ball.ycor() > computer.paddle[0].ycor() and ball.ycor() > computer.paddle[-1].ycor():
        computer.up()
      elif ball.ycor() < computer.paddle[0].ycor() and ball.ycor() < computer.paddle[-1].ycor():
        computer.down()

    # If computer hits top or bottom wall move computer to opposite direction.
    if computer.paddle[0].ycor() > HEIGHT / 2 - 20:
      computer.down()
    if computer.paddle[-1].ycor() < -HEIGHT / 2 + 20:
      computer.up()

    computer.move()


  # Collision detection between paddle and ball
  for idx in range(0, paddle_length):
    # Responsible for the top side of the paddle returns ball back towards northwards directly with respective to west/eastwards.
    if idx < int(paddle_length/ 2):
      if player.paddle[idx].distance(ball) < 10:
        if direction_random == 1:
          ball.north_east()
        else:
          ball.south_east()
        if game_difficulty == "medium":
          ball.change_speed(FAST_BALL_SPEED) if idx == 0 else ball.change_speed(MEDIUM_BALL_SPEED)
      if computer.paddle[idx].distance(ball) < 10:
        if direction_random == 1:
          ball.north_west()
        else:
          ball.south_west()
        if game_difficulty == "medium":
          ball.change_speed(FAST_BALL_SPEED) if idx == 0 else ball.change_speed(MEDIUM_BALL_SPEED)

    # Responsible for the middle of the paddle returns ball in a straight line as east or west.
    elif idx == int(paddle_length/2):
      if player.paddle[idx].distance(ball) < 10:
        ball.east()
        if game_difficulty == "medium":
          ball.change_speed(FAST_BALL_SPEED)
      if computer.paddle[idx].distance(ball) < 10:
        ball.west()
        if game_difficulty == "medium":
          ball.change_speed(FAST_BALL_SPEED)

    # Responsible for the bottom side of the paddle returns ball back towards southward directly with respective to west/eastwards.
    else:
      if player.paddle[idx].distance(ball) < 10:
        if direction_random == 1:
          ball.south_east()
        else:
          ball.north_east()
        if game_difficulty == "medium":
          ball.change_speed(FAST_BALL_SPEED) if idx == paddle_length - 1 else ball.change_speed(MEDIUM_BALL_SPEED)
      if computer.paddle[idx].distance(ball) < 10:
        if direction_random == 1:
          ball.south_west()
        else:
          ball.north_west()
        if game_difficulty == "medium":
          ball.change_speed(FAST_BALL_SPEED) if idx == paddle_length - 1 else ball.change_speed(MEDIUM_BALL_SPEED)


  # Collision detection between ball and the upper and lower wall.
  if ball.ycor() > HEIGHT / 2 - 20:
    if ball.traveling == NE:
      ball.south_east()
    elif ball.traveling == NW:
      ball.south_west()

  if ball.ycor() < -HEIGHT / 2 + 20:
    if ball.traveling == SE:
      ball.north_east()
    elif ball.traveling == SW:
      ball.north_west()
  

  # If ball passes left wall and is still inside the y-axis increment computer 1 score.
  if ball.xcor() < -WIDTH / 2 - 50 and (ball.ycor() < HEIGHT / 2 - 20 or ball.ycor() > -HEIGHT / 2 + 20):
    if game_difficulty == "medium":
      ball.change_speed(MEDIUM_BALL_SPEED)
    ball.refresh()
    computer_score.increase_score()
  
  # If ball passes right wall and is still inside the y-axis increment player 1 score.
  if ball.xcor() > WIDTH / 2 + 50 and (ball.ycor() < HEIGHT / 2 - 20 or ball.ycor() > -HEIGHT / 2 + 20):
    if game_difficulty == "medium":
      ball.change_speed(MEDIUM_BALL_SPEED)
    ball.refresh()
    player_score.increase_score()
  
  # End the game if somebody scores the max goals.
  if player_score.score == MAX_SCORE or computer_score.score == MAX_SCORE:
    message = "Congratulation {winner} you have won!".format(winner=player_1 if player_score.score == MAX_SCORE else player_2_type)
    text_2.return_the_winner(message)
    game_on = False

screen.exitonclick()