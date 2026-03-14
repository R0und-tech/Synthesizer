import pygame
import librosa
import soundfile as sf
import io

FILE_NAME = r"D:\Sintez\noteC.mp3"

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
    sf.write(buffer, y_shifted_1, sr, format='WAV')
    return buffer.seek(0)


def pygame_load(buffer) -> None:
    pygame.mixer.music.load(buffer)
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(0)


def control_func(FILE_NAME: str, n_steps: int) -> None:
    y_shifted_1, sr = shifting(FILE_NAME, n_steps)
    buffer = convert(y_shifted_1, sr)
    pygame_load(buffer)



screen = pygame.display.set_mode((400, 300))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key in dictionary_1:
                control_func(FILE_NAME, dictionary_1[event.key])
        
        
        

