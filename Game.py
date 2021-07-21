import pygame

from Case import Case
from Players import Player


class Game:

    def __init__(self):
        # create player
        self.player = Player()
        self.case1 = Case()


    def printBoard(self,window):
        pygame.draw.rect(window, (0, 0, 0), (self.x, self.y, 32, 32))

# board_rects = [  ( 200,100,250,250, red ), ( 150,75,350,300, green ), ( 100,50,450,350, red ) ]
# for rect in board_rects:
#     x_pos, y_pos  = rect[0], rect[1]
#     width, height = rect[2], rect[3]
#     colour        = rect[4]
#     pygame.draw.rect( screen, colour, ( x_pos, y_pos, width, height ), 2 )

# int the_round(PLAYER *player,int nb_player,int my_round)
# {
#     int value;
#     if(nb_player==2)
#     {
#         if(my_round%2==0)value = 0;
#         else value = 1;
#     }
#     else if(nb_player==3)
#     {
#         if(my_round%3==0)value = 0;
#         else if(my_round%3==1)value = 1;
#         else if(my_round%3==2)value = 2;
#     }
#     else if(nb_player==4)
#     {
#         if(my_round%4==0)value = 0;
#         else if(my_round%4==1)value = 1;
#         else if(my_round%4==2)value = 2;
#         else if(my_round%4==3)value = 3;
#     }
#
#     return value;
# }