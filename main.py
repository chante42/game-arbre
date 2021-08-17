import pygame
import math
from pygame.constants import K_LEFT
from game import Game

pygame.init()

#defnir une clock
clock =pygame.time.Clock()
FPS = 60
        
# généré la fenetre de notre jeux 
pygame.display.set_caption("game-Arbre")
screen = pygame.display.set_mode((1080, 720))

# importer l'arriere plan
background = pygame.image.load("assets/bg.jpg")

# charger la banniere
banner = pygame.image.load("assets/banner.png")
banner = pygame.transform.scale(banner, (500,500))
banner_rect = banner.get_rect()
banner_rect.x = math.ceil(screen.get_width() / 4)

# chargement du bouton pour lancer la partie
play_button = pygame.image.load("assets/button.png")
play_button  = pygame.transform.scale(play_button, (400,150))
play_button_rect = play_button.get_rect()
play_button_rect.x = math.ceil(screen.get_width() / 3.33)
play_button_rect.y = math.ceil(screen.get_height() / 2)

 

game = Game()

running = True

while running:

    screen.blit(background, (0,-200))
    
    # si le jeux a commencer
    if game.is_playing :
        game.update(screen)
    else:
        screen.blit(play_button, play_button_rect)
        screen.blit(banner, banner_rect)

    # met a jour l'écran
    pygame.display.flip()

    #si le joueur ferme la fenetre
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

        # detecte si un joueur appuit sur une touche du clavier
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True

            # detection si la touche espace est déja appuyer
            if event.key == pygame.K_SPACE :
                game.player.launch_projectile()

        elif event.type == pygame.KEYUP :
            game.pressed[event.key] = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if play_button_rect.collidepoint(event.pos):
                game.start()

    # fixer le nombre de FPS sur la clock
    clock.tick(FPS)        