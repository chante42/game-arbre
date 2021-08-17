import pygame
from projectile import Projectile
import animation

#classe joueur
class Player(animation.animateSprite) :

    def __init__(self, game) -> None:
        super().__init__('player')
        self.health     = 100
        self.max_health = 100
        self.attack     = 10
        self.velocity   = 1
        self.rect       =  self.image.get_rect()
        self.rect.x     = 400
        self.rect.y     = 500
        self.all_projectiles = pygame.sprite.Group()
        self.game       = game

    def damage(self, amount) :

        if self.health > amount :
            self.health -= amount
        else :
            self.game.game_over()

    def update_animation(self):
        self.animate()

    def update_health_bar(self, surface):
        pygame.draw.rect(surface,(60,63,60), [self.rect.x + 50, self.rect.y + 20, self.max_health, 7])
        pygame.draw.rect(surface, (111,210,46), [self.rect.x + 50, self.rect.y + 20, self.health, 7])
    
    def launch_projectile(self) :
        
        self.all_projectiles.add(Projectile(self))
        self.start_animation()

    def move_right(self):
        
        # si le joeur n 'est pas en collision avec le monstre
        if not(self.game.check_collision(self, self.game.all_monsters)) : 
            self.rect.x +=  self.velocity
    
    def move_left(self):
        self.rect.x -=  self.velocity