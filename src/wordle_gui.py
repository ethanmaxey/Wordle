from wordle import *
import pygame, sys, random, pandas

dictionary_csv = pandas.read_csv("words.csv")

WORDS = dictionary_csv[dictionary_csv.columns[0]].tolist()

solution = random.choice(WORDS)

black = (0, 0, 0)
white = (255, 255, 255)
green = (108, 169, 101)
yellow = (200, 182, 83)
grey = (120, 124, 127)
red = (255, 0, 0)

width, height = 420, 600

class Board:
    rowPos, colPos = 0, 0
    board = [["" for block in range(5)] for block in range(6)]
    current_game_status = IN_PROGRESS
    invalid_word = False

pygame.init()
big_font = pygame.font.Font(None, 52)
little_font = pygame.font.Font(None, 26)
screen = pygame.display.set_mode((width, height))

def add_guess_to_board():
    
    temp_guess = ''.join(board_instance.board[board_instance.rowPos])
    
    if len(temp_guess) == 5:
        
        play_output_dictionary = play(solution, temp_guess, board_instance.rowPos)
        
        highlight_text_colors(play_output_dictionary['response'], board_instance.rowPos)
        
        check_for_game_over(play_output_dictionary['status'], play_output_dictionary['message'])
        
        if (play_output_dictionary['status'] == IN_PROGRESS):
            board_instance.rowPos += 1
            board_instance.colPos = 0

def mouse_is_over_button():

    return True if (pygame.mouse.get_pos()[0] >= 147 and pygame.mouse.get_pos()[0] <= 270 and pygame.mouse.get_pos()[1] >= 550 and pygame.mouse.get_pos()[1] <= 585) else False

def highlight_guess_button(event):
    
    if mouse_is_over_button() and len(''.join(board_instance.board[board_instance.rowPos])) == 5: 
        
        guess_button = big_font.render('GUESS', True, white, black)
        screen.blit(guess_button, (screen.get_width() / 2 -  guess_button.get_rect().width / 2, 550))

def mouse_clicking_guess_button_functionality(event):
    
    if (mouse_is_over_button()): add_guess_to_board()

def display_clickable_button(event):
    
    if len(''.join(board_instance.board[board_instance.rowPos])) == 5 and board_instance.current_game_status == IN_PROGRESS:
        
        guess_button = big_font.render('GUESS', True, grey, black)
        screen.blit(guess_button, (screen.get_width() / 2 -  guess_button.get_rect().width / 2, 550))
                    
    else: 
        
        guess_button = big_font.render('GUESS', True, black, black)
        screen.blit(guess_button, (screen.get_width() / 2 -  guess_button.get_rect().width / 2, 550))

def display_game_ending_message(message):
    
    guess_button = big_font.render('GUESS', True, black, black) 
    
    screen.blit(guess_button, (screen.get_width() / 2 -  guess_button.get_rect().width / 2, 550))

    display_font = big_font if board_instance.current_game_status == WON else little_font 
    color = green if board_instance.current_game_status == WON else red
    
    message_object = display_font.render(message, True, color)

    screen.blit(message_object, (screen.get_width() / 2 -  message_object.get_rect().width / 2, 550))
    
def check_for_game_over(status, message):
    
    if status != IN_PROGRESS: 
        
        board_instance.current_game_status = status
        display_game_ending_message(message)   

def display_wordle_title():
    wordle_title = big_font.render('Wordle', True, white)     
    screen.blit(wordle_title, (150, 10))

def typing_letters_functionality(event):
    
    if event.unicode.isalpha() and board_instance.board[board_instance.rowPos][4] == "":
        
        board_instance.board[board_instance.rowPos][board_instance.colPos] = event.unicode.upper()
        board_instance.colPos += 1

def enter_key_button_functionality(event):
    
    if (event.key == pygame.K_RETURN): add_guess_to_board()

def backspace_key_functionality(event):
    
    if (event.key == pygame.K_BACKSPACE and board_instance.colPos > 0):
                        
        board_instance.colPos -= 1
        board_instance.board[board_instance.rowPos][board_instance.colPos] = ""
        
        pygame.draw.rect(screen, black, [(board_instance.colPos) * 80 + 12, board_instance.rowPos * 80 + 50, 75, 75])

def draw_blank_board():
    
    for colNum in range(0, 5):
        for rowNum in range(0, 6):
            
            pygame.draw.rect(screen, grey,  [colNum * 80 + 12, rowNum * 80 + 50, 75, 75], 2)
            
            color = red if board_instance.invalid_word else white
            
            piece_text = big_font.render(board_instance.board[rowNum][colNum], True, white)
            screen.blit(piece_text, (colNum * 80 + 40, rowNum * 80 + 70))
            
def highlight_text_colors(response, rowNum):
    
    [pygame.draw.rect(screen, green if status == EXACT else (yellow if status == EXISTS else grey), [(index) * 80 + 12, rowNum * 80 + 50, 75, 75]) for index, status in enumerate(response)]
    
def key_press_and_mouse_click_handler(event):

    if board_instance.current_game_status == IN_PROGRESS:

        if event.type == pygame.KEYDOWN:
            
            enter_key_button_functionality(event)
            backspace_key_functionality(event)
            typing_letters_functionality(event)
            
        elif event.type == pygame.MOUSEBUTTONUP: mouse_clicking_guess_button_functionality(event)
        
        elif event.type == pygame.MOUSEMOTION: highlight_guess_button(event)
        
def game_loop():
    
    while True:
        
        draw_blank_board()
        display_wordle_title()
        
        for event in pygame.event.get():
            
            if board_instance.current_game_status == IN_PROGRESS: display_clickable_button(event)
            
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()    
            
            key_press_and_mouse_click_handler(event)
        
        pygame.display.update()
        
board_instance = Board()       
game_loop()