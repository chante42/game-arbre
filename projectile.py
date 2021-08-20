import pygame
import animation
# definir la classe de gestion du projectif de notre joueur

class Projectile (animation.animateSprite):

    def __init__(self, player) -> None:
        super().__init__('projectile', (50,50))

        self.velocity  = 1
        self.player = player
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + 120
        self.rect.y = player.rect.y + 80 
        self.origin_image = self.image
        self.angle = 0
        self.start_animation()

    def update_animation(self) :
        self.animate(loop=True)

    def remove(self) :
        self.player.all_projectiles.remove(self)

    def move(self):
        self.rect.x += self.velocity
        #self.rotate()

        # si le projectile rentre en collision avec un monstre
        for monster in  self.player.game.check_collision(self, self.player.game.all_monsters):
            self.remove()
            monster.damage(self.player.attack)

        # si le projectile sort de l'écran
        if self.rect.x > 1080 :
            self.remove()
        

