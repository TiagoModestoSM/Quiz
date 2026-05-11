# Arquivo: quiz.py
# Roda o código principal

import pygame
import sys
from display import *


# Carregar perguntas
def load_questions(perguntas):
    questions_list = []
    try:
        with open(perguntas, 'r', encoding = 'utf-8') as file:
            lines = file.readlines()
            
            index = 0
            while index < len(lines):
                
                question = {
                    'text': lines[index].strip(),
                    'A': lines[index + 1].strip(),
                    'B': lines[index + 2].strip(),
                    'C': lines[index + 3].strip(),
                    'D': lines[index + 4].strip(),
                    'E': lines[index + 5].strip(),
                    'answer': lines[index + 6].strip().upper()
                }
                questions_list.append(question)
                index += 7
    except FileNotFoundError:
        print("ERRO: O arquivo de perguntas não foi encontrado, verifique o nome do arquivo ou se ele existe")
        sys.exit()
        
    return questions_list



# Jogar

def play_game():
    questions = load_questions('perguntas.txt')
    current_index = 0
    score = 0
    state = 'PLAYING'
    
    running = True
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            if event.type == pygame.KEYDOWN and state == "PLAYING":
                user_answer = ""
                
                # Mapear as teclas para responder o quiz
                if event.key == pygame.K_a: user_answer = "A"
                elif event.key == pygame.K_b: user_answer = "B"
                elif event.key == pygame.K_c: user_answer = "C"
                elif event.key == pygame.K_d: user_answer = "D"
                elif event.key == pygame.K_e: user_answer = "E"
                
                # Verificar a opção escolhida
                if user_answer != "":
                    if user_answer == questions[current_index]['answer']:
                        score += 100

                    current_index += 1

                    if current_index >= len(questions):
                        state = "GAME_OVER"

        # Desenhando o jogo
        screen.fill(BG_COLOR)