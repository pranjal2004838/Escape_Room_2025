import pygame
import random, time
import math

# Initialize pygame
pygame.init()  # This initializes all Pygame modules, including fonts and mixer

# Initialize pygame mixer and load sound effects
pygame.mixer.init()
typewriter_sound = pygame.mixer.Sound(r"typewriter-typing-68696.mp3")  # Replace with your sound file path
hacking_sound = pygame.mixer.Sound(r"tv-static-noise-291374.mp3")  # Use only this sound file

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
    """Chaotic and fast hacking animation with erratic code rain and flickering warnings."""
    start_time = time.time()
    code_columns = [random.randint(0, WIDTH) for _ in range(40)]
    column_speeds = [random.uniform(8.0, 16.0) for _ in range(len(code_columns))]
    trails = [[] for _ in code_columns]

    # Play the hacking sound effect in a loop
    hacking_sound.play(-1)  # -1 means loop indefinitely

    try:
        while time.time() - start_time < duration:
            screen.fill(BLACK)

            # Fast and chaotic code rain
            for i, col in enumerate(code_columns):
                speed = column_speeds[i]
                trail = trails[i]

                if not trail or trail[-1][1] > random.randint(10, 30):
                    char = random.choice("アイウエオカキクケコサシスセソABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()")
                    trail.append([char, 0])

                new_trail = []
                for j, (char, y) in enumerate(trail):
                    fade = max(0, 255 - j * 35)
                    color = (0, fade, 0)
                    x_jitter = col + random.randint(-2, 2)  # slight horizontal chaos
                    render_text(char, x_jitter, int(y), color)
                    y += speed + random.uniform(-2, 4)  # speed variation
                    if random.random() < 0.05:
                        y += 50  # glitch jump
                    if y < HEIGHT:
                        new_trail.append([char, y])
                trails[i] = new_trail

            # Aggressive flickering scanlines
            if random.random() < 0.5:
                for _ in range(random.randint(3, 6)):
                    y = random.randint(0, HEIGHT)
                    color = (0, random.randint(100, 255), 0)
                    pygame.draw.line(screen, color, (0, y), (WIDTH, y), 1)

            # Flickering warning
            if random.random() < 0.7:
                render_text("☠", WIDTH // 2 - 20 + random.randint(-5, 5), HEIGHT // 2 - 60 + random.randint(-5, 5), RED)
                render_text("SYSTEM FAILURE!", WIDTH // 2 - 110 + random.randint(-5, 5), HEIGHT // 2 + 30 + random.randint(-5, 5), RED)

            pygame.display.update()
            pygame.time.delay(10)  # faster frame update
    finally:
        # Stop the sound effect after the glitch effect ends
        hacking_sound.stop()

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

def main():
    """Main function to run the game."""
    if not intro_screen():
        return

    glitch_effect(duration=2)

    pygame.quit()

if __name__ == "__main__":
    main()