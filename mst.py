"""nom = input("entrer votre nom : ")
age = input("entrer votre age : ")
try:
    age_prochain = int(age) + 1
except:
    print("ERREUR")
print("vous vous appelez " + nom + " vous avez " + str(age))
print("l'an prochain vous avez " + str(age_prochain))


nom = str(input("entrer votre nom : "))
age = int(input("entrer votre age : "))
age_prochain = age + 1
print("vous vous appelez " + nom + " vous avez " + str(age) + " ans")
print("l'an prochain vous avez " + str(age_prochain) + " ans")"""

import pygame
import random

# Initialisation de Pygame
pygame.init()

# Configuration de la fenêtre de jeu
size = (800, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Jeu de tir spatial")

# Couleurs
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Boucle principale
done = False
clock = pygame.time.Clock()

# Position initiale de l'objet joueur
player_x = 400
player_y = 550

# Position initiale de l'objet ennemi
enemy_x = random.randint(0, 700)
enemy_y = 0

# Vitesse de déplacement des objets
player_speed = 5
enemy_speed = 3

# Score du joueur
score = 0

# Boucle de jeu
while not done:
    # Gestion des événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
    # Gestion des touches du clavier
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < 700:
        player_x += player_speed
    
    # Mise à jour de la position de l'objet ennemi
    enemy_y += enemy_speed
    
    # Si l'objet ennemi touche le sol, réinitialiser sa position
    if enemy_y > 600:
        enemy_x = random.randint(0, 700)
        enemy_y = 0
        score -= 1
    
    # Vérifier si l'objet joueur touche l'objet ennemi
    if abs(player_x - enemy_x) < 50 and abs(player_y - enemy_y) < 50:
        enemy_x = random.randint(0, 700)
        enemy_y = 0
        score += 1
    
    # Effacer l'écran
    screen.fill(BLACK)
    
    # Dessiner les objets
    pygame.draw.rect(screen, WHITE, [player_x, player_y, 50, 50])
    pygame.draw.rect(screen, RED, [enemy_x, enemy_y, 50, 50])
    
    # Afficher le score
    font = pygame.font.Font(None, 36)
    text = font.render("Score: " + str(score), True, WHITE)
    screen.blit(text, [10, 10])
    
    # Rafraîchir l'écran
    pygame.display.flip()
    
    # Limiter la vitesse de rafraîchissement de l'écran
    clock.tick(60)

# Quitter Pygame
pygame.quit()

