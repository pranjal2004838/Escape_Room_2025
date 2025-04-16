import pygame
import time
import random
import os
import sys


binary_numbers = [
    "0000",  # 0
    "0001",  # 1
    "0010",  # 2
    "0011",  # 3
    "0100",  # 4
    "0101",  # 5
    "0110",  # 6
    "0111",  # 7
    "1000",  # 8
    "1001"   # 9
]


def render_centered_text(text, color, y=None, delay=100):
    if y is None:
        y = HEIGHT // 2
    surface = font.render(text, True, color)
    x = WIDTH // 2 - surface.get_width() // 2
    screen.blit(surface, (x, y))


def update_run_count():
    count_file = "run_count.txt"
    if os.path.exists(count_file):
        with open(count_file, "r") as file:
            try:
                run_count = int(file.read().strip())
            except ValueError:
                run_count = 0
    else:
        run_count = 0

    run_count += 1
    if run_count > 10:
        run_count = 1

    with open(count_file, "w") as file:
        file.write(str(run_count))

    return run_count


pygame.init()
pygame.mixer.init()

typewriter_sound = pygame.mixer.Sound(r"typewriter-typing-68696.mp3")
hacking_sound = pygame.mixer.Sound(r"tv-static-noise-291374.mp3")
clock_sound = pygame.mixer.Sound(r"typewriter-typing-68696-[AudioTrimmer.com].mp3")
game_over_sound = pygame.mixer.Sound(r"game-over-38511.mp3")
incorrect_sound = pygame.mixer.Sound(r"wrong-47985-[AudioTrimmer.com].mp3")

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
WIDTH, HEIGHT = screen.get_size()
pygame.display.set_caption("Cyber Escape Room")

BLACK = (10, 10, 10)
WHITE = (255, 255, 255)
GREEN = (0, 255, 100)
DARK_GREEN = (0, 80, 0)
RED = (200, 0, 0)
GRAY = (20, 20, 20)

def get_font(size):
    try:
        return pygame.font.Font("Orbitron-Regular.ttf", size)
    except FileNotFoundError:
        return pygame.font.SysFont("consolas", size)

font = get_font(24)
timer_font = get_font(60)

alphanumeric_list = [
    "A12", "B34", "C56", "D78", "E90", "F23", "G45", "H67", "I89", "J10",
    "K32", "L54", "M76", "N98", "O21", "P43", "Q65", "R87", "S09", "T31",
    "U53", "V75", "W97", "X20", "Y42", "Z64", "A86", "B08", "C30", "D52",
    "E74", "F96", "G19", "H41", "I63", "J85", "K07", "L29", "M51", "N73",
    "O95", "P18", "Q40", "R62", "S84", "T06", "U28", "V50", "W72", "X94",
    "Y17", "Z39", "A61", "B83", "C05", "D27", "E49", "F71", "G93", "H16",
    "I38", "J60", "K82", "L04", "M26", "N48", "O70", "P92", "Q15", "R37",
    "S59", "T81", "U03", "V25", "W47", "X69", "Y91", "Z14", "A36", "B58",
    "C80", "D02", "E24", "F46", "G68", "H90", "I13", "J35", "K57", "L79",
    "M01", "N23", "O45", "P67", "Q89", "R12", "S34", "T56", "U78", "V90"
]


def first_screen():
    """Display the first welcome screen."""
    draw_matrix_background()
    typewriter("Welcome to the Cyber Escape Room!", WIDTH // 2 - 300, HEIGHT // 2 - 100, GREEN, delay=150)
    typewriter("Press ENTER to continue...", WIDTH // 2 - 220, HEIGHT // 2, (0, 255, 180), delay=150)
    pygame.display.update()

    # Start timer when user presses enter
    timer_start_time = None

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                timer_start_time = time.time()  # Start the timer here
                return timer_start_time


def failsafe_screen():
    draw_matrix_background()
    failsafe_message = (
        "You shouldn’t have come here.\n\n"
        "This room is no longer safe.\n"
        "You’ve triggered the failsafe.\n\n"
        "In 15 minutes, the lockdown will turn permanent.\n"
        "Air will thin. Power will surge. No one gets out.\n\n"
        "I built EchoDust to end the noise of the world.\n"
        "And you… walked right into its heart.\n\n"
        "But I’m not unfair.\n"
        "Find the shutdown key. It’s in here somewhere — behind the lies I left behind.\n\n"
        "Solve the puzzles.\n"
        "Or become the next victims of my silence.\n\n"
        "Timer starts now."
    )

    lines = failsafe_message.split('\n')
    y = 100
    for line in lines:
        typewriter(line, WIDTH // 2 - font.size(line)[0] // 2, y, RED, delay=200)
        y += font.get_height() + 10

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                waiting = False



def draw_matrix_background():
    screen.fill(BLACK)
    for i in range(0, WIDTH, 40):
        for j in range(0, HEIGHT, 40):
            pygame.draw.rect(screen, GRAY, (i, j, 40, 40), 1)


def render_timer(remaining_time):
    minutes = remaining_time // 60
    seconds = remaining_time % 60
    timer_text = f"{minutes:02}:{seconds:02}"
    timer_surface = timer_font.render(timer_text, True, RED)
    timer_rect = timer_surface.get_rect(center=(WIDTH // 2, 60))
    screen.blit(timer_surface, timer_rect)


def glitch_effect(duration=4):
    hacking_sound.play(-1)
    start_time = time.time()
    while time.time() - start_time < duration:
        draw_matrix_background()

        for _ in range(5000):
            x = random.randint(0, WIDTH - 1)
            y = random.randint(0, HEIGHT - 1)
            color = random.choice([WHITE, BLACK, (100, 100, 100), (50, 50, 50)])
            screen.set_at((x, y), color)

        for _ in range(15):
            y = random.randint(0, HEIGHT - 1)
            color = random.choice([WHITE, (150, 150, 150), (200, 200, 200)])
            pygame.draw.line(screen, color, (0, y), (WIDTH, y), random.randint(1, 3))

        for _ in range(8):
            x = random.randint(0, WIDTH - 50)
            y = random.randint(0, HEIGHT - 50)
            w = random.randint(50, 200)
            h = random.randint(10, 50)
            color = random.choice([WHITE, BLACK, (50, 50, 50), (80, 80, 80)])
            pygame.draw.rect(screen, color, (x, y, w, h))

        pygame.display.update()
        pygame.time.delay(random.randint(30, 70))
    hacking_sound.stop()


def typewriter(text, x, y, color=GREEN, delay=1):
    displayed_text = ""
    typewriter_sound.play()
    for char in text:
        displayed_text += char
        text_surface = font.render(displayed_text, True, color)
        screen.blit(text_surface, (x, y))
        pygame.display.update()
        pygame.time.delay(delay)
    typewriter_sound.stop()

    # Ensure the final rendered text stays static
    screen.fill(BLACK, (x, y, font.size(text)[0], font.size(text)[1]))  # Clear the area
    final_surface = font.render(text, True, color)
    screen.blit(final_surface, (x, y))
    pygame.display.update()


def intro_screen():
    draw_matrix_background()
    typewriter("You are captured in a mysterious room!", WIDTH // 2 - 250, HEIGHT // 2 - 100)
    typewriter("Solve the puzzles to escape.", WIDTH // 2 - 200, HEIGHT // 2 - 50)
    typewriter("Press ENTER to start the game...", WIDTH // 2 - 220, HEIGHT // 2, (0, 255, 180))
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                return True

def puzzle_game(start_time, total_time, start_index, rfid):
    user_input = ""
    incorrect_attempts = 0
    running = True

    current_chunk = alphanumeric_list[start_index:start_index + 10]
    chunk_surfaces = []
    y_offset = 100
    for item in current_chunk:
        text_surface = font.render(item, True, GREEN)
        chunk_surfaces.append((text_surface, (WIDTH // 2 - 200, y_offset)))
        y_offset += 30

    success = False

    while running:
        draw_matrix_background()

        # Update and render timer continuously
        elapsed_time = int(time.time() - start_time)
        remaining_time = max(0, total_time - elapsed_time)
        render_timer(remaining_time)

        # Handle time-out at any point
        if remaining_time <= 0:
            draw_matrix_background()
            render_centered_text("Time's Up! Game Over.", RED)
            pygame.display.update()
            pygame.time.wait(3000)
            return

        # Draw puzzle or success screen based on game state
        if not success:
            # Show the chunk
            for surface, position in chunk_surfaces:
                screen.blit(surface, position)

            # Instructions and input
            static_texts = [
                ("Enter numbers from vowels in reverse order:", WIDTH // 2 - 300, 400, GREEN),
                (f"Your Input: {user_input}", WIDTH // 2 - 300, 450, WHITE),
                (f"Incorrect Attempts: {incorrect_attempts}/2", WIDTH // 2 - 300, 500, RED)
            ]
            space_between = 40
            for idx, (text, x, y, color) in enumerate(static_texts):
                y_position = HEIGHT // 2 + (idx - len(static_texts) // 2) * space_between
                render_centered_text(text, color, y=y_position)
        else:
            # Success screen with typewriter effect (this will only run once)
            messages = [
                "Level 1 Complete!",
                "Go To Next Puzzle On Your Right",
                "Your Clues Are:",
                "For next puzzle: 3520"
            ]

            # Calculate total height for centering messages
            message_height = font.size("A")[1]
            line_spacing = 20
            total_height = len(messages) * message_height + (len(messages) - 1) * line_spacing
            y_offset = HEIGHT // 2 - total_height // 2  # Center vertically based on total height

            current_y_offset = y_offset
            for message in messages:
                typewriter(message, WIDTH // 2 - font.size(message)[0] // 2, current_y_offset, WHITE, delay=100)
                current_y_offset += message_height + line_spacing  # Space between lines

            # Keep the final messages static after the typewriter effect
            current_y_offset = y_offset  # Reset vertical offset
            for message in messages:
                text_surface = font.render(message, True, WHITE)
                screen.blit(text_surface, (WIDTH // 2 - text_surface.get_width() // 2, current_y_offset))
                current_y_offset += message_height + line_spacing  # Space between lines

            # Continuously render the timer until remaining time becomes zero
            while True:
                elapsed_time = int(time.time() - start_time)
                remaining_time = max(0, total_time - elapsed_time)
                draw_matrix_background()

                # Render the static success messages
                current_y_offset = y_offset
                for message in messages:
                    text_surface = font.render(message, True, WHITE)
                    screen.blit(text_surface, (WIDTH // 2 - text_surface.get_width() // 2, current_y_offset))
                    current_y_offset += message_height + line_spacing

                # Render the timer
                render_timer(remaining_time)
                pygame.display.update()

                # Break the loop when time is up
                if remaining_time <= 0:
                    break

            # Calculate total height for centering messages
            message_height = font.size("A")[1]
            line_spacing = 20
            total_height = len(messages) * message_height + (len(messages) - 1) * line_spacing
            y_offset = HEIGHT // 2 - total_height // 2  # Center vertically based on total height

            current_y_offset = y_offset
            for message in messages:
                typewriter(message, WIDTH // 2 - font.size(message)[0] // 2, current_y_offset, WHITE, delay=100)
                current_y_offset += message_height + line_spacing  # Space between lines

            # Keep the final messages static after the typewriter effect
            current_y_offset = y_offset  # Reset vertical offset
            for message in messages:
                text_surface = font.render(message, True, WHITE)
                screen.blit(text_surface, (WIDTH // 2 - text_surface.get_width() // 2, current_y_offset))
                current_y_offset += message_height + line_spacing  # Space between lines

            pygame.display.update()

        pygame.display.update()

        # Process input events for user typing
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

            if event.type == pygame.KEYDOWN and not success:
                if event.key == pygame.K_RETURN:
                    if user_input == "1q2w":
                        draw_matrix_background()
                        render_centered_text("Special Code Entered. Game Terminated.", RED)
                        pygame.display.update()
                        pygame.time.wait(3000)
                        return

                    number_list = [item[1:] for item in current_chunk[::-1] if item[0] in 'AEIOU']
                    answer = ''.join(number_list)

                    if user_input == answer:
                        glitch_effect(duration=2)
                        success = True
                    else:
                        incorrect_attempts += 1
                        incorrect_sound.play()
                        render_centered_text("Incorrect!", RED, y=550)
                        pygame.display.update()
                        pygame.time.wait(1000)
                        user_input = ""

                        if incorrect_attempts >= 2:
                            draw_matrix_background()
                            render_centered_text("Too many incorrect attempts. Game Over.", RED)
                            pygame.display.update()
                            pygame.time.wait(3000)
                            return

                elif event.key == pygame.K_BACKSPACE:
                    user_input = user_input[:-1]
                else:
                    user_input += event.unicode







def main():
    run_count = update_run_count()
    rfid = binary_numbers[run_count - 1]  # or just rfid = run_count - 1 if you want an int
    start_index = (run_count - 1) * 10
    total_time = 15 * 60  # 15 minutes in seconds

    # Show the first screen and get the timer start time
    timer_start_time = first_screen()
    if not timer_start_time:
        return
    
    failsafe_screen()

    # Show the intro screen and start the timer
    intro_screen()

    # Proceed to the game with the remaining time
    glitch_effect(duration=4)
    puzzle_game(timer_start_time, total_time, start_index, rfid)

    pygame.quit()

if __name__ == "__main__":
    main()
