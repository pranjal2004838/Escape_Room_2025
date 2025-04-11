import pygame
import time
import random

# Initialize pygame and mixer
pygame.init()
pygame.mixer.init()

# Load sounds
typewriter_sound = pygame.mixer.Sound(r"typewriter-typing-68696.mp3")
hacking_sound = pygame.mixer.Sound(r"tv-static-noise-291374.mp3")
clock_sound = pygame.mixer.Sound(r"one-minute-mechanical-clock-ticking-sound-effect-253099.mp3")

# Screen settings
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

# Fonts (fallback to system font if Orbitron is missing)
def get_font(size):
    try:
        return pygame.font.Font("Orbitron-Regular.ttf", size)
    except FileNotFoundError:
        return pygame.font.SysFont("consolas", size)

font = get_font(24)
timer_font = get_font(60)

# Alphanumeric strings (with hidden pattern)
alphanumeric_list = [
    "A1", "B2", "E3", "C4", "O5", "D6", "I7", "F8", "U9", "G10",
    "H11", "J12", "A13", "K14", "E15", "L16", "I17", "M18", "O19", "N20",
    "P21", "Q22", "U23", "R24", "A25", "S26", "E27", "T28", "I29", "V30",
    "W31", "X32", "O33", "Y34", "A35", "Z36", "E37", "B38", "U39", "C40",
    "D41", "F42", "I43", "G44", "O45", "H46", "U47", "J48", "A49", "K50",
    "L51", "M52", "E53", "N54", "I55", "P56", "O57", "Q58", "A59", "R60",
    "S61", "T62", "U63", "V64", "E65", "W66", "I67", "X68", "O69", "Y70",
    "Z71", "B72", "A73", "C74", "E75", "D76", "I77", "F78", "U79", "G80",
    "H81", "J82", "O83", "K84", "A85", "L86", "E87", "M88", "I89", "N90",
    "P91", "Q92", "U93", "R94", "E95", "S96", "I97", "T98", "O99", "V100"
]

def draw_matrix_background():
    screen.fill(BLACK)
    for i in range(0, WIDTH, 40):
        for j in range(0, HEIGHT, 40):
            pygame.draw.rect(screen, GRAY, (i, j, 40, 40), 1)

def render_glow_text(text, x, y, base_color=GREEN, delay=50):
    displayed_text = ""
    for char in text:
        displayed_text += char
        draw_matrix_background()
        shadow = font.render(displayed_text, True, DARK_GREEN)
        screen.blit(shadow, (x+2, y+2))
        text_surface = font.render(displayed_text, True, base_color)
        screen.blit(text_surface, (x, y))
        pygame.display.update()
        pygame.time.delay(delay)

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

def typewriter(text, x, y, color=GREEN, delay=100):
    displayed_text = ""
    for char in text:
        displayed_text += char
        draw_matrix_background()
        text_surface = font.render(displayed_text, True, color)
        screen.blit(text_surface, (x, y))
        pygame.display.update()
        typewriter_sound.play()
        pygame.time.delay(delay)
    typewriter_sound.stop()

def intro_screen():
    draw_matrix_background()
    typewriter("You are captured in a mysterious room!", 150, 200)
    typewriter("Solve the puzzles to escape.", 200, 250)
    typewriter("Press ENTER to start the game...", 200, 300, (0, 255, 180))
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                return True

def puzzle_game(start_time, total_time):
    start_index = 0
    user_input = ""
    incorrect_attempts = 0
    running = True

    while running:
        draw_matrix_background()

        elapsed_time = int(time.time() - start_time)
        remaining_time = max(0, total_time - elapsed_time)

        render_timer(remaining_time)

        current_chunk = alphanumeric_list[start_index:start_index + 10]
        y_offset = 100
        for item in current_chunk:
            render_glow_text(item, 50, y_offset)
            y_offset += 30

        render_glow_text("Enter numbers from vowels in reverse order:", 50, 400)
        render_glow_text(f"Your Input: {user_input}", 50, 450, WHITE)
        render_glow_text(f"Incorrect Attempts: {incorrect_attempts}/3", 50, 500, RED)

        pygame.display.update()

        if remaining_time <= 0:
            draw_matrix_background()
            typewriter("Time's Up! Game Over.", 150, HEIGHT // 2, RED)
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
                            render_glow_text("Level 1 Complete!", 150, HEIGHT // 2, GREEN)
                            render_glow_text("Go To Next Puzzle On Your Right", 150, HEIGHT // 2 + 30)
                            render_glow_text("Your Clues Are:", 150, HEIGHT // 2 + 50)
                            render_glow_text("For next puzzle: 3520", 150, HEIGHT // 2 + 100)
                            render_glow_text("To Fetch RFID Tag: 5", 150, HEIGHT // 2 + 150)
                            pygame.display.update()
                            time.sleep(1)
                            elapsed_time = int(time.time() - start_time)
                            remaining_time = max(0, total_time - elapsed_time)
                            if remaining_time <= 60:
                                clock_sound.play(-1)
                                if remaining_time <= 0:
                                    clock_sound.stop()
                                    draw_matrix_background()
                                    typewriter("Time's Up! Game Over.", 150, HEIGHT // 2, RED)
                                    pygame.display.update()
                                    time.sleep(3)
                                    return
                        return
                        render_glow_text("Level 1 Complete!", 150, HEIGHT // 2, GREEN)
                        render_glow_text("Go To Next Puzzle On Your Right", 150, HEIGHT // 2 + 30)
                        render_glow_text("Your Clues Are:", 150, HEIGHT // 2 + 50)
                        render_glow_text("For next puzzle: 3520", 150, HEIGHT // 2 + 100)
                        render_glow_text("To Fetch RFID Tag: 5", 150, HEIGHT // 2 + 150)
                        pygame.display.update()
                        time.sleep(5)
                        return
                        render_timer(remaining_time)
                        render_glow_text("Level 1 Complete!", 150, HEIGHT // 2, GREEN)
                        render_glow_text("Go To Next Puzzle On Your Right", 150, HEIGHT // 2 + 30)
                        render_glow_text("Your Clues Are:", 150, HEIGHT // 2 + 50)
                        render_glow_text("For next puzzle: 3520", 150, HEIGHT // 2 + 100)
                        render_glow_text("To Fetch RFID Tag: 5", 150, HEIGHT // 2 + 150)
                        pygame.display.update()
                        time.sleep(5)
                        return
                    else:
                        incorrect_attempts += 1
                        render_glow_text("Incorrect!", 50, 550, RED)
                        pygame.display.update()
                        time.sleep(2)
                        user_input = ""
                        if incorrect_attempts >= 3:
                            draw_matrix_background()
                            typewriter("Too many incorrect attempts. Game Over.", 100, 250, RED)
                            pygame.display.update()
                            time.sleep(3)
                            return
                elif event.key == pygame.K_BACKSPACE:
                    user_input = user_input[:-1]
                else:
                    user_input += event.unicode

def main():
    if not intro_screen():
        return

    start_time = time.time()
    glitch_effect(duration=4)
    puzzle_game(start_time, 15 * 60)
    
    
    pygame.quit()

if __name__ == "__main__":
    main()
