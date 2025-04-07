import pygame
import random, time
import math

# Initialize pygame
pygame.init()  # This initializes all Pygame modules, including fonts and mixer

# Initialize pygame mixer and load sound effects
pygame.mixer.init()
typewriter_sound = pygame.mixer.Sound(r"Escape_Room_2025\typewriter-typing-68696.mp3")  # Replace with your sound file path
hacking_sound = pygame.mixer.Sound(r"Escape_Room_2025\typewriter-typing-68696.mp3")  # Use only this sound file

# Screen settings
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Escape Room")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (200, 0, 0)
GREEN = (0, 200, 0)

# Fonts
font = pygame.font.Font(None, 36)  # Ensure pygame.init() is called before this

def render_text(text, x, y, color=WHITE):
    """Render text on the screen."""
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))

def glitch_effect(duration=4):
    """Display a realistic glitch effect resembling an old TV no-signal screen with sound."""
    hacking_sound.play(-1)  # Play the hacking sound in a loop
    start_time = time.time()
    while time.time() - start_time < duration:
        screen.fill(BLACK)  # Clear the screen

        # Add random noise (static pixels)
        for _ in range(5000):  # Increase the number of "ants" (random pixels)
            x = random.randint(0, WIDTH - 1)
            y = random.randint(0, HEIGHT - 1)
            color = random.choice([WHITE, BLACK, (100, 100, 100), (50, 50, 50)])  # Add more gray shades
            screen.set_at((x, y), color)  # Set the pixel color at (x, y)

        # Add flickering horizontal lines
        for _ in range(15):  # Increase the number of lines
            x_start = 0
            y = random.randint(0, HEIGHT - 1)
            x_end = WIDTH
            color = random.choice([WHITE, (150, 150, 150), (200, 200, 200)])
            pygame.draw.line(screen, color, (x_start, y), (x_end, y), random.randint(1, 3))  # Random thickness

        # Add random rectangles (screen distortion)
        for _ in range(8):  # Increase the number of rectangles
            x = random.randint(0, WIDTH - 50)
            y = random.randint(0, HEIGHT - 50)
            width = random.randint(50, 200)
            height = random.randint(10, 50)
            color = random.choice([WHITE, BLACK, (50, 50, 50), (80, 80, 80)])
            pygame.draw.rect(screen, color, (x, y, width, height))

        # Add vertical bars (signal interference)
        for _ in range(5):  # Number of vertical bars
            x = random.randint(0, WIDTH - 1)
            height = random.randint(50, HEIGHT)
            color = random.choice([WHITE, (100, 100, 100), (150, 150, 150)])
            pygame.draw.line(screen, color, (x, 0), (x, height), random.randint(1, 3))

        # Add screen flicker effect
        if random.random() < 0.1:  # Occasionally invert the screen colors
            inverted_surface = pygame.Surface((WIDTH, HEIGHT))
            for x in range(WIDTH):
                for y in range(HEIGHT):
                    color = screen.get_at((x, y))
                    inverted_color = (255 - color.r, 255 - color.g, 255 - color.b)
                    inverted_surface.set_at((x, y), inverted_color)
            screen.blit(inverted_surface, (0, 0))

        pygame.display.update()
        pygame.time.delay(random.randint(30, 70))  # Randomize delay for more realism

    hacking_sound.stop()  # Stop the sound after the glitch effect ends

def typewriter(text, x, y, color=BLACK, delay=150):
    """Render text with a typewriter effect and sound."""
    displayed_text = ""
    for char in text:
        displayed_text += char
        text_surface = font.render(displayed_text, True, color)
        screen.fill(BLACK, (x, y, WIDTH, 50))  # Clear the previous text line
        screen.blit(text_surface, (x, y))
        pygame.display.update()

        # Play the typewriter sound effect while rendering the character
        typewriter_sound.play()
        pygame.time.delay(delay)  # Delay in milliseconds
    typewriter_sound.stop()  # Stop the sound after the entire text is rendered

def intro_screen():
    """Display the intro screen."""
    screen.fill(BLACK)
    typewriter("You are captured in a mysterious room!", 150, 200, WHITE)
    typewriter("Solve the puzzles to escape.", 200, 250, WHITE)
    typewriter("Press ENTER to start the game...", 200, 300, GREEN)
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                return True
        # Ensure the screen remains static after rendering the text
        pygame.display.update()

def main():
    """Main function to run the game."""
    if not intro_screen():
        return

    glitch_effect(duration=2)

    pygame.quit()

if __name__ == "__main__":
    main()