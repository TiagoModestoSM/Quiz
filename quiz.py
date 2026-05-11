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
        
        if state == "PLAYING":
            current_question = questions[current_index]
            
            header_text = TITLE_FONT.render(f"Pergunta {current_index + 1} de {len(questions)}", True, HIGHLIGHT_COLOR)
            screen.blit(header_text, (50,30))
            
            question_text = QUESTION_FONT.render(current_question['text'], True, TEXT_COLOR)
            screen.blit(question_text, (50, 120))
            
            text_a = OPTIONS_FONT.render(current_question['A'], True, TEXT_COLOR)
            text_b = OPTIONS_FONT.render(current_question['B'], True, TEXT_COLOR)
            text_c = OPTIONS_FONT.render(current_question['C'], True, TEXT_COLOR)
            text_d = OPTIONS_FONT.render(current_question['D'], True, TEXT_COLOR)
            text_e = OPTIONS_FONT.render(current_question['E'], True, TEXT_COLOR)
            
            screen.blit(text_a, (50, 200))
            screen.blit(text_b, (50, 250))
            screen.blit(text_c, (50, 300))
            screen.blit(text_d, (50, 350))
            screen.blit(text_e, (50, 400))
            
            instruction_text = OPTIONS_FONT.render("Pressione a tecla A, B, C, D ou E no teclado.", True, HIGHLIGHT_COLOR)
            screen.blit(instruction_text, (50, 500))
            
        elif state == "GAME_OVER":
            end_text = TITLE_FONT.render("FIM DO QUIZ! PARABÉNS... OU NÃO", True, HIGHLIGHT_COLOR)
            screen.blit(end_text, (150, 200))
            
            score_text = TITLE_FONT.render(f"Sua Pontuação: {score} de {len(questions)}", True, TEXT_COLOR)
            screen.blit(score_text, (230, 300))
            
        pygame.display.flip()
            
    pygame.quit()

# Inicia o jogo
if __name__ == "__main__":
    play_game()