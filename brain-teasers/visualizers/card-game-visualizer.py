import pygame
import random
import sys
import time

pygame.init()

WIDTH, HEIGHT = 1000, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Card Game Visualization")

FONT = pygame.font.SysFont(None, 28)
BIGFONT = pygame.font.SysFont(None, 36)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (220, 50, 50)
GRAY = (180, 180, 180)

clock = pygame.time.Clock()

def draw_text(text, x, y, color=BLACK, big=False):
    font = BIGFONT if big else FONT
    img = font.render(text, True, color)
    screen.blit(img, (x, y))

def main():
    deck = ['R'] * 26 + ['B'] * 26
    random.shuffle(deck)

    your_pile = []
    dealer_pile = []
    discarded = []

    index = 0
    running = True
    step_timer = 0

    while running:
        screen.fill(WHITE)
        clock.tick(60)
        step_timer += 1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        draw_text("YOU (Red-Red)", 100, 20, RED, True)
        draw_text("DEALER (Black-Black)", 700, 20, BLACK, True)
        draw_text("DISCARDED (Mixed)", 400, 20, GRAY, True)

        draw_text(f"Your pile: {len(your_pile)}", 100, 60, RED)
        draw_text(f"Dealer pile: {len(dealer_pile)}", 700, 60, BLACK)
        draw_text(f"Discarded: {len(discarded)}", 420, 60, GRAY)

        if index < len(deck) and step_timer > 60:
            c1 = deck[index]
            c2 = deck[index + 1]
            index += 2
            step_timer = 0

            if c1 == 'R' and c2 == 'R':
                your_pile.extend([c1, c2])
            elif c1 == 'B' and c2 == 'B':
                dealer_pile.extend([c1, c2])
            else:
                discarded.extend([c1, c2])

        draw_text(f"Cards left: {len(deck) - index}", 420, 500, BLACK, True)

        if index >= len(deck):
            draw_text("GAME OVER", 420, 300, BLACK, True)

            if len(your_pile) > len(dealer_pile):
                draw_text("YOU WIN", 420, 350, RED, True)
            elif len(your_pile) < len(dealer_pile):
                draw_text("YOU LOSE", 420, 350, BLACK, True)
            else:
                draw_text("TIE", 460, 350, GRAY, True)

        pygame.display.flip()

main()
