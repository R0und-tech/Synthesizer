import pygame
import librosa
import soundfile as sf
import io


FILE_NAME = r"D:\Sintez\noteC.mp3"

dictionary_1 = {"K_a": 4, "K_x": 8, "K_c": 12, "K_v": 16, "K_b": 20, "K_n": 24, "K_m": 28 }

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
            if event.key == pygame.K_a:
                steps = dictionary_1["K_a"]
                control_func(FILE_NAME, steps)

            elif event.key == pygame.K_x:
                steps = dictionary_1["K_x"]
                control_func(FILE_NAME, steps)

            elif event.key == pygame.K_c:
                steps = dictionary_1["K_c"]
                control_func(FILE_NAME, steps)

            elif event.key == pygame.K_v:
                steps = dictionary_1["K_v"]
                control_func(FILE_NAME, steps)

            elif event.key == pygame.K_b:
                steps = dictionary_1["K_b"]
                control_func(FILE_NAME, steps)

            elif event.key == pygame.K_n:
                steps = dictionary_1["K_n"]
                control_func(FILE_NAME, steps)
            
            elif event.key == pygame.K_m:
                steps = dictionary_1["K_m"]
                control_func(FILE_NAME, steps)
