import pygame
import time

pygame.init()


alphanumeric_list = [
    "A1", "B2", "E3", "C4", "O5", "D6", "I7", "F8", "U9", "G10",   # 4 vowels: A, E, O, I, U
    "H11", "J12", "A13", "K14", "E15", "L16", "I17", "M18", "O19", "N20",  # 4 vowels: A, E, I, O
    "P21", "Q22", "U23", "R24", "A25", "S26", "E27", "T28", "I29", "V30",  # 4 vowels: U, A, E, I
    "W31", "X32", "O33", "Y34", "A35", "Z36", "E37", "B38", "U39", "C40",  # 4 vowels: O, A, E, U
    "D41", "F42", "I43", "G44", "O45", "H46", "U47", "J48", "A49", "K50",  # 4 vowels: I, O, U, A
    "L51", "M52", "E53", "N54", "I55", "P56", "O57", "Q58", "A59", "R60",  # 4 vowels: E, I, O, A
    "S61", "T62", "U63", "V64", "E65", "W66", "I67", "X68", "O69", "Y70",  # 4 vowels: U, E, I, O
    "Z71", "B72", "A73", "C74", "E75", "D76", "I77", "F78", "U79", "G80",  # 4 vowels: A, E, I, U
    "H81", "J82", "O83", "K84", "A85", "L86", "E87", "M88", "I89", "N90",  # 4 vowels: O, A, E, I
    "P91", "Q92", "U93", "R94", "E95", "S96", "I97", "T98", "O99", "V100"  # 4 vowels: U, E, I, O
]



# Screen settings
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Escape Room")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (200, 0, 0)

# Fonts
font = pygame.font.Font(None, 36)

def typewriter_effect(text, x, y, delay=0.1):
    displayed_text = ""
    for char in text:
        displayed_text += char
        render_text(displayed_text, x, y)
        pygame.display.update()
        time.sleep(delay)

def render_text(text, x, y, color=WHITE):
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))

def main():
    running = True
    show_intro = True
    start_game = False

    while running:
        screen.fill(BLACK)
        
        if show_intro:
            typewriter_effect("You have been captured...", 200, 200)
            time.sleep(1)
            typewriter_effect("Find a way to escape...", 200, 250)
            pygame.display.update()
            time.sleep(1)
            
            # Display "Press Enter"
            typewriter_effect("Press ENTER to continue...", 250, 400, RED)
            pygame.display.update()
            
            while show_intro:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        return
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                        show_intro = False
                        start_game = True
                
        if start_game:
            screen.fill(BLACK)
            render_text("Welcome to the Escape Room", 200, 200)
            render_text("Click START to begin", 250, 300)
            
            start_button = pygame.Rect(300, 350, 200, 50)
            pygame.draw.rect(screen, RED, start_button)
            render_text("START", 365, 365, BLACK)
            
            pygame.display.update()
            
            waiting_for_start = True
            while waiting_for_start:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        return
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if start_button.collidepoint(event.pos):
                            print("Game Starts!")  # Replace this with actual game logic
                            running = False  # Exiting for now
                            break
        

    pygame.quit()

if __name__ == "__main__":
    main()
