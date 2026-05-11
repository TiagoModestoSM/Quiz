# Arquivo: display.py
# Guardar informações da configuração da tela

import pygame

# Interface do Jogo
pygame.init()

# Def Janela
HEIGHT = 600
WIDTH = 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mini-Game Quizz!")

# Setar cores
BG_COLOR = pygame.Color("#1E1E39") # Testar outra cor depois
TEXT_COLOR = pygame.Color("#FFFFFF") # Branco 100%
TEXT_COLOR_2 = pygame.Color("#FFD700") # Dourado? 

# Fontes de texto
TITLE_FONT = pygame.font.SysFont("arial", 40, bold=True)
QUESTION_FONT = pygame.font.SysFont("arial", 30)
OPTIONS_FONT = pygame.font.SysFont("arial", 25)