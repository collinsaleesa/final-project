import pygame
import sys
import random

# I used mostly yt turtorials and the ebook plus some rubberduck.ai and chatgpt throughout the project.
correct_code = "5683"


pygame.init()
clock = pygame.time.Clock()
fps = 60
font = pygame.font.Font("freesansbold.ttf", 36)
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Escape Room Game")


locked_img = pygame.image.load("closed_door.png").convert_alpha()
unlocked_img = pygame.image.load("room_image.jpg").convert_alpha()
BG = locked_img

puzzle = [
    "puzzle1_piece1.jpg",
    "puzzle1_piece2.jpg",
    "puzzle1_piece3.jpg",
    "puzzle1_piece4.jpg",
    "puzzle2_piece1.jpg",
    "puzzle2_piece2.jpg",
    "puzzle2_piece3.jpg",
    "puzzle2_piece4.jpg",
]

puzzle_pieces = []
for f in puzzle:
    image = pygame.image.load(f).convert_alpha()
    rect = image.get_rect()
    puzzle_pieces.append({"image": image, "rect": rect})


active_puzzle = None
run = True
while run:
    clock.tick(fps)
    SCREEN.blit(BG, (0, 0))

    my_text = font.render("Welcome", True, "black")
    SCREEN.blit(my_text, (100, 150))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                for num, piece in enumerate(puzzle_pieces):
                    if piece["rect"].collidepoint(event.pos):
                        active_puzzle = num
                        break
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                active_puzzle = None
        elif event.type == pygame.MOUSEMOTION:
            if active_puzzle != None:
                puzzle_pieces[active_puzzle]["rect"].move_ip(event.rel)

    for piece in puzzle_pieces:
        SCREEN.blit(piece["image"], piece["rect"])

    pygame.display.flip()


class Button:
    def __init__(self, image, pos, text_input, font, base_color, hovering_color):
        self.image = image
        self.x_pos = pos[0]
        self.y_pos = pos[1]
        self.font = font
        self.base_color = base_color
        self.hovering_color = hovering_color
        self.text_input = text_input
        self.text = self.font.render(self.text_input, True, self.base_color)

        if self.image is None:
            self.image = self.text

        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
        self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

    def update(self, screen):
        if self.image is not None:
            screen.blit(self.image, self.rect)
        screen.blit(self.text, self.text_rect)

    def checkForInput(self, position):
        return self.rect.collidepoint(position)

    def changeColor(self, position):
        if self.rect.collidepoint(position):
            self.text = self.font.render(self.text_input, True, self.hovering_color)
        else:
            self.text = self.font.render(self.text_input, True, self.base_color)


def main_menu():
    pygame.display.set_caption("Main Menu")

    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = font.render("MAIN MENU", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        PLAY_BUTTON = Button(
            image=pygame.image.load("file name"),
            pos=(640, 250),
            text_input="START",
            font=get_font(75),
            base_color="#d7fcd4",
            hovering_color="White",
        )


pygame.quit()
