import pygame
import math


class RotationController:

   def __init__(self):
       self.rot_x = 0
       self.rot_y = 0
       self.sensitivity = 0.3
       self.dragging = False
       self.last_pos = None

   def handle_event(self, event):

       if event.type == pygame.MOUSEBUTTONDOWN:
           if event.button == 1:
               self.dragging = True
               self.last_pos = pygame.mouse.get_pos()

       elif event.type == pygame.MOUSEBUTTONUP:
           if event.button == 1:
               self.dragging = False

       elif event.type == pygame.MOUSEMOTION and self.dragging:
           x, y = pygame.mouse.get_pos()
           lx, ly = self.last_pos

           dx = x - lx
           dy = y - ly

           self.rot_y += dx * self.sensitivity
           self.rot_x += dy * self.sensitivity

           self.last_pos = (x, y)
