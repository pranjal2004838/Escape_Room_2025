import pygame
import time

import random


# Initialize pygame
pygame.init()  # This initializes all Pygame modules, including fonts and mixer

# Initialize pygame mixer and load sound effects
pygame.mixer.init()
typewriter_sound = pygame.mixer.Sound(r"Escape_Room_2025\typewriter-typing-68696.mp3")  # Replace with your sound file path
hacking_sound = pygame.mixer.Sound(r"Escape_Room_2025\tv-static-noise-291374.mp3")  # Use only this sound file
clock_sound = pygame.mixer.Sound(r"Escape_Room_2025\one-minute-mechanical-clock-ticking-sound-effect-253099.mp3")  # Replace with your sound file path



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
        
pygame.init()

# Colors
BLACK = (0, 0, 0)

def typewriter(text, x, y, color=BLACK, delay=10):
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
GREEN = (0, 200, 0)

# Fonts
font = pygame.font.Font(None, 36)

def render_text(text, x, y, color=WHITE):
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))

def intro_screen():
    """Display the intro screen with the 'You are captured...' message once."""
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

def puzzle_game(start_time, total_time):
    """Run the alphanumeric puzzle game with a timer."""
    start_index = 0
    running = True
    user_input = ""
    incorrect_attempts = 0  # Count incorrect answers

    while running:
        screen.fill(BLACK)

        # Calculate remaining time
        elapsed_time = int(time.time() - start_time)
        remaining_time = max(0, total_time - elapsed_time)  # Ensure it doesn't go below 0
        minutes = remaining_time // 60
        seconds = remaining_time % 60

        # Display the timer
        render_text(f"Time Left: {minutes:02}:{seconds:02}", WIDTH - 200, 20, RED)

        # Display the current 10 alphanumeric strings
        current_chunk = alphanumeric_list[start_index:start_index + 10]
        y_offset = 50
        for item in current_chunk:
            render_text(item, 50, y_offset)
            y_offset += 30

        # Display instructions
        render_text("Enter the numbers from vowels in reverse order:", 50, 400)
        render_text(f"Your Input: {user_input}", 50, 450, GREEN)
        render_text(f"Incorrect Attempts: {incorrect_attempts}/3", 50, 500, RED)

        pygame.display.update()

        # Check if time is up
        if remaining_time <= 0:
            screen.fill(BLACK)
            typewriter("Time's Up! Game Over.", 150, HEIGHT // 2, RED)
            pygame.display.update()
            time.sleep(3)
            running = False  # Exit the game loop
            return

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    # Check the answer
                    number_list = [item[1:] for item in current_chunk[::-1] if item[0] in 'AEIOU']
                    answer = ''.join(number_list)
                    if user_input == answer:
                        

                        while remaining_time > 0:  # Keep the screen static while the timer runs
                            screen.fill(BLACK)  # Clear the screen for the next chunk
                            elapsed_time = int(time.time() - start_time)
                            remaining_time = max(0, total_time - elapsed_time)  # Ensure it doesn't go below 0
                            minutes = remaining_time // 60
                            seconds = remaining_time % 60

                            render_text(f"Time Left: {minutes:02}:{seconds:02}", WIDTH - 200, 20, RED)
                            render_text("Level 1 Complete!", 150, HEIGHT // 2, GREEN)
                            render_text("Go To Next Puzzle On Your Right", 150, HEIGHT // 2 + 30, GREEN)
                            render_text("Your Clues Are:", 150, HEIGHT // 2 + 50, GREEN)
                            render_text("For next puzzle: 3520", 150, HEIGHT // 2 + 100, GREEN)
                            render_text("To Fetch RFID Tag: 5", 150, HEIGHT // 2 + 150, GREEN)
                            pygame.display.update()
                            pygame.time.delay(1000)  # Delay to reduce CPU usage


                            if remaining_time <= 870:
                                clock_sound.play(-1)

                                
                        
                        # Once the timer runs out, exit the loop
                        screen.fill(BLACK)
                        typewriter("Time's Up! Game Over.", 150, HEIGHT // 2, RED)
                        pygame.display.update()
                        time.sleep(3)
                        running = False  # Exit the game loop
                       



                        
                    else:
                        incorrect_attempts += 1
                        render_text("Incorrect!", 50, 550, RED)
                        pygame.display.update()
                        time.sleep(2)
                        user_input = ""  # Reset user input

                        if incorrect_attempts >= 3:
                            screen.fill(BLACK)
                            typewriter("Too many incorrect attempts. Game Over.", 100, 250, RED)
                            pygame.display.update()
                            time.sleep(3)
                            running = False  # Exit game
                elif event.key == pygame.K_BACKSPACE:
                    user_input = user_input[:-1]
                else:
                    user_input += event.unicode

def main():
    """Main function to run the game."""
    running = True
    total_time = 15 * 60  # 15 minutes in seconds
    start_time = time.time()  # Record the start time

    # Show the intro screen first
    if not intro_screen():
        return

    # Show the glitch effect
    glitch_effect(duration=4)

    # Start the puzzle game
    puzzle_game(start_time, total_time)  # Pass the required arguments

    pygame.quit()

if __name__ == "__main__":
    main()