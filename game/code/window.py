import pygame

class Fenetre:
    def __init__(self, largeur, hauteur, titre):
        pygame.init()
        self.fenetre = pygame.display.set_mode((largeur, hauteur))
        pygame.display.set_caption(titre)

    def obtenir_fenetre(self):
        return self.fenetre

    def quitter(self):
        pygame.quit()
        
    def fill(self,couleur):
        self.fenetre.fill(couleur)
        

if __name__ == "__main__":
    # Exemple d'utilisation en tant que script principal
    fenetre = Fenetre(800, 600, "Dialogue avec Pygame")

    # Boucle principale
    while True:
        for evenement in pygame.event.get():
            if evenement.type == pygame.QUIT:
                fenetre.quitter()
                exit()
