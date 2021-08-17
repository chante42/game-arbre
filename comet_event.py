import pygame
from comet import Comet

class CometFallEvent:

    def __init__(self, game) -> None:
        self.percent = 0
        self.percent_speed = 6
        # groupe de sprite pour stocker les commetes
        self.all_comets = pygame.sprite.Group()
        self.game = game
        self.fall_mode = False


    def add_percent(self):
        self.percent += self.percent_speed / 100

    def is_full_loaded(self):
        return self.percent >= 100

    def reset_percent(self) :
        self.percent = 0

    def meteor_fall(self):
        for i in range(1,10) :
            # apparaitre une nouvelle boule de fau
            self.all_comets.add(Comet(self))

        
    def attempt_fall(self):
        if self.is_full_loaded() and len(self.game.all_monsters) == 0:
            
            print("pluis de commete !!!")
            self.meteor_fall()
            
            self.fall_mode = True # activé l'evènement

    def update_bar(self, surface):

        self.add_percent()

        pygame.draw.rect(surface, (0,0,0), [
            0, # x
            surface.get_height() - 20, #y
            surface.get_width(), # longueur
            10 # epaisseur de la barre
             ])
        
        pygame.draw.rect(surface, (187,11,11), [
            0, # x
            surface.get_height() - 20, #y
            (surface.get_width()/100) * self.percent, # longueur
            10 # epaisseur de la barre
             ])