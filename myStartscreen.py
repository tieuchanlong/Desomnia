'''
    Title: Desomnia ( Start Screen )
    Author: Long Tieu, Wayne Seto, Ethan
    Date:
'''


import pygame
pygame.init() # load the pygame module commands in the program

# Display variables
TITLE = 'Hello World' # Appear in the window title
FPS = 30 # Frames per second
WIDTH = 900
HEIGHT = 500
SCREENDIM = (WIDTH, HEIGHT)
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Color variables
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (50, 50, 50)

# Create the window
screen = pygame.display.set_mode(SCREENDIM) # Create the main surface where all other assets are placed on top
pygame.display.set_caption(TITLE) # This updates the windows title
screen.fill(BLACK) # Fill the entire surface with the chosen color. Think of fill as erase.

clock = pygame.time.Clock()  # starts a clock object to measure time

### --- Codes starts here --- ###

screenimage = []
imagecounter = -1

for i in range(356):
    imagecounter += 1
    screenimage.append("media/startscreen - image" + str(imagecounter) + ".jpg")

screenimageload = []
for i in range(356):
    screenimageload.append(pygame.image.load(screenimage[i]).convert())

print(imagecounter)
print(screenimage)

print(screenimageload[i])
running = True
count = 0

while running:

    for event in pygame.event.get(): # return all inputs and triggers into an array
        if event.type == pygame.QUIT: # If the red X was clicked
            running = False

        if event.type == pygame.KEYDOWN:
            level = 1

    screen.blit(screenimageload[count], (0, 0))
    count +=1
    if (count > 355):
        count = 0

    clock.tick(FPS) # pause the game until FPS time is reached
    pygame.display.update()


pygame.quit()