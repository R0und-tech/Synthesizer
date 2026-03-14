import pygame
import librosa
import soundfile as sf
import numpy as np
import io


FILE_NAME = r"D:\Sintez\noteC.mp3"
SIN_BACK = (30, 30, 50)

dictionary_1 = {
    
    pygame.K_z: -1, pygame.K_x: -2, pygame.K_c: -3, pygame.K_v: -4, pygame.K_b: -5, pygame.K_n: -6, pygame.K_m: -7,
    
    pygame.K_a: 1, pygame.K_s: 2, pygame.K_d: 3, pygame.K_f: 4, pygame.K_g: 5, pygame.K_h: 6, pygame.K_j: 7,

    pygame.K_q: 8, pygame.K_w: 9, pygame.K_e: 10, pygame.K_r: 11, pygame.K_t: 12, pygame.K_y: 13, pygame.K_u: 14
}

pygame.init()
pygame.mixer.init()

def shifting(FILE_NAME, n_steps):
    y, sr = librosa.load(FILE_NAME)
    y_shifted_1 = librosa.effects.pitch_shift(y, sr=sr, n_steps=n_steps)
    return y_shifted_1, sr


def convert(y_shifted_1, sr):
    buffer = io.BytesIO()
    sf.write(buffer, y_shifted_1, sr, format='wav')
    buffer.seek(0)
    return buffer


def pygame_load(buffer) -> None:
    sound = pygame.mixer.Sound(buffer)
    sound.set_volume(0.05)
    sound.play()

def create_simple_sine(frequency=440, width=300, height=150):
    sin = pygame.Surface((width, height))
    sin.fill(SIN_BACK)

    points = []

    for x in range(width):
        y = height // 2 + int(50 * np.sin(2 * np.pi * frequency * x / width))
        points.append((x, y))

    if points:
        pygame.draw.lines(sin, (0, 150, 255), False, points, 2)

    return sin

def sin_draw(sin):
    sin_form_rect = sin.get_rect(center=(400, 300))
    screen.blit(sin, sin_form_rect)

current_sin = None 

def control_func(FILE_NAME: str, n_steps: int) -> None:
    global current_sin
    y_shifted_1, sr = shifting(FILE_NAME, n_steps)
    buffer = convert(y_shifted_1, sr)
    pygame_load(buffer)
    current_sin = create_simple_sine()
    



screen = pygame.display.set_mode((800, 600))
background = pygame.Surface(screen.get_size())
background.fill((30, 30, 50))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            print("***")
            if event.key in dictionary_1:
                control_func(FILE_NAME, dictionary_1[event.key])

    screen.blit(background, (0,0))

    if current_sin:
        sin_draw(current_sin)

    pygame.display.flip()
