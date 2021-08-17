import pygame

# classe qui va s'ocuper es animation
class animateSprite(pygame.sprite.Sprite):
    def __init__(self, sprite_name) -> None:
        super().__init__()
        self.sprite_name = sprite_name
        self.image = pygame.image.load(f'assets/{sprite_name}.png')
        self.current_image = 0 # commence l'annimation
        self.images =  animation.get(sprite_name)
        self.animation = False

    # methode pour démarer une animation
    def start_animation(self):
        self.animation= True


    # methode pour animer le sprite
    def animate(self, loop=False):

        if self.animation :
            self.current_image += 1
            if self.current_image > len(self.images) -1 :
                self.current_image = 0
     
                # verifier si l annimation n est pas en mode boucle
                if loop is False :
                    self.animation = False

            # modifier l'image 
            self.image = self.images[self.current_image]

# definir  une fonction pour charger les images d'un srite
def load_animation_images(sprite_name):
    # charger les 24 images de ce sprite dans le dossier correspondant
    images = []
    # recupérer le c
    path=f'assets/{sprite_name}/{sprite_name}'
    # boucler sur chaque imae sur ce dossier
    for i in range(1,24):
        image_path = path + str(i) +'.png' 
        images.append(pygame.image.load(image_path))
    
    return images


#definir un dictionnaire qui va definir les images chargés de chaque spite
# mummy -> [... mummy1.png, ... ]
animation = { 
    'mummy'  : load_animation_images("mummy"),
    'player' : load_animation_images('player')
    }