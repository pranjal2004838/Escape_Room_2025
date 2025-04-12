import pygame
import time
import random
import os

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
    if run_count > 5:
        run_count = 1

    with open(count_file, "w") as file:
        file.write(str(run_count))
    
    return run_count

pygame.init()
pygame.mixer.init()

# Load sounds
typewriter_sound = pygame.mixer.Sound(r"typewriter-typing-68696.mp3")
hacking_sound = pygame.mixer.Sound(r"tv-static-noise-291374.mp3")
clock_sound = pygame.mixer.Sound(r"one-minute-mechanical-clock-ticking-sound-effect-253099.mp3")
game_over_sound = pygame.mixer.Sound(r"game-over-38511.mp3")

# Screen setup
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Cyber Escape Room")

# Colors
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

alphanumeric_list = []
vowels = "AEIOU"
consonants = "BCDFGHJKLMNPQRSTVWXYZ"

for i in range(1, 51):
    if random.random() < 0.4:  # 40% chance to pick a vowel
        letter = random.choice(vowels)
    else:  # 60% chance to pick a consonant
        letter = random.choice(consonants)
    alphanumeric_list.append(f"{letter}{i}")

random.shuffle(alphanumeric_list)  # Shuffle the list for added randomness

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
    timer_rect = timer_surface.get_rect(center=(WIDTH // 2, 40))
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

def typewriter(text, x=None, y=None, color=GREEN, delay=10, center=True):
    displayed_text = ""
    if center:
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect(center=(WIDTH // 2 if x is None else x, y))
        x = text_rect.x
    for char in text:
        displayed_text += char
        text_surface = font.render(displayed_text, True, color)
        screen.blit(text_surface, (x, y))
        pygame.display.update()
        typewriter_sound.play()
        pygame.time.delay(delay)
    typewriter_sound.stop()
    final_surface = font.render(text, True, color)
    screen.blit(final_surface, (x, y))
    pygame.display.update()

def intro_screen():
    draw_matrix_background()
    typewriter("You are captured in a mysterious room!", y=200)
    typewriter("Solve the puzzles to escape.", y=250)
    typewriter("Press ENTER to start the game...", y=300, color=(0, 255, 180))
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                return True

def puzzle_game(start_time, total_time, start_index):
    user_input = ""
    incorrect_attempts = 0
    running = True

    current_chunk = alphanumeric_list[start_index:start_index + 10]
    chunk_surfaces = []
    y_offset = 100
    for item in current_chunk:
        text_surface = font.render(item, True, GREEN)
        chunk_surfaces.append((text_surface, (50, y_offset)))
        y_offset += 30

    while running:
        draw_matrix_background()

        for surface, position in chunk_surfaces:
            screen.blit(surface, position)

        elapsed_time = int(time.time() - start_time)
        remaining_time = max(0, total_time - elapsed_time)
        render_timer(remaining_time)

        info_texts = [
            ("Enter numbers from vowels in reverse order:", 50, 400, GREEN),
            (f"Your Input: {user_input}", 50, 450, WHITE),
            (f"Incorrect Attempts: {incorrect_attempts}/3", 50, 500, RED)
        ]
        for text, x, y, color in info_texts:
            screen.blit(font.render(text, True, color), (x, y))

        pygame.display.update()

        if remaining_time <= 0:
            draw_matrix_background()
            typewriter("Time's Up! Game Over.", y=HEIGHT // 2, color=RED)
            pygame.display.update()
            time.sleep(3)
            return

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    number_list = [item[1:] for item in current_chunk[::-1] if item[0] in 'AEIOU']
                    answer = ''.join(number_list)
                    if user_input == answer:
                        draw_matrix_background()
                        glitch_effect(duration=3)
                        draw_matrix_background()
                        while remaining_time > 0:
                            draw_matrix_background()
                            render_timer(remaining_time)
                            typewriter("Level 1 Complete!", y=HEIGHT // 2, color=GREEN)
                            typewriter("Go To Next Puzzle On Your Right", y=HEIGHT // 2 + 30)
                            typewriter("Your Clues Are:", y=HEIGHT // 2 + 60)
                            typewriter("For next puzzle: 3520", y=HEIGHT // 2 + 100)
                            typewriter("To Fetch RFID Tag: 5", y=HEIGHT // 2 + 140)
                            pygame.display.update()
                            time.sleep(1)
                            elapsed_time = int(time.time() - start_time)
                            remaining_time = max(0, total_time - elapsed_time)
                            if remaining_time <= 60:
                                clock_sound.play(-1)
                                if remaining_time <= 0:
                                    clock_sound.stop()
                                    draw_matrix_background()
                                    typewriter("Time's Up! Game Over.", y=HEIGHT // 2, color=RED)
                                    pygame.display.update()
                                    time.sleep(3)
                                    return
                    else:
                        incorrect_attempts += 1
                        typewriter("Incorrect!", x=50, y=550, color=RED, center=False)
                        pygame.display.update()
                        time.sleep(2)
                        user_input = ""
                        if incorrect_attempts >= 3:
                            draw_matrix_background()
                            typewriter("Too many incorrect attempts. Game Over.", y=250, color=RED)
                            pygame.display.update()
                            time.sleep(3)
                            return
                elif event.key == pygame.K_BACKSPACE:
                    user_input = user_input[:-1]
                else:
                    user_input += event.unicode

def main():
    run_count = update_run_count()
    start_index = (run_count - 1) * 10
    if not intro_screen():
        return
    start_time = time.time()
    glitch_effect(duration=4)
    puzzle_game(start_time, 15 * 60, start_index)
    pygame.quit()

if __name__ == "__main__":
    main()
