import sys
import pygame
from time import sleep


class EventLoop:
    def __init__(self, finished, display_lives):
        self.finished = finished
        self.display_lives = display_lives

    @staticmethod
    def check_events(ai_settings, menu, mario):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                EventLoop.check_keydown_events(event, mario)
            if event.type == pygame.KEYUP:
                EventLoop.check_keyup_events(event, mario)
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                EventLoop.check_play_button(ai_settings, menu, mouse_x, mouse_y)

    @staticmethod
    def check_keydown_events(event, mario):
        if event.key == pygame.K_RIGHT:
            print('RIGHT')
            mario.moving_right = True
            mario.orientation = "Right"
        elif event.key == pygame.K_LEFT:
            print('LEFT')
            mario.moving_left = True
            mario.orientation = "Left"
        elif event.key == pygame.K_UP:
            print('UP')
            mario.moving_up = True
            mario.orientation = "Up"
        elif event.key == pygame.K_DOWN:
            print('DOWN')
            mario.moving_down = True
            mario.orientation = "Down"
        elif event.key == pygame.K_SPACE:
            print('JUMP')
            mario.jump = True
            mario.jumping = True
            mario.orientation = "Jump"
        # elif event.key == pygame.K_c:
        #     mario.vel.x += 2
        elif event.key == pygame.K_q:
            sys.exit()

    @staticmethod
    def check_keyup_events(event, mario):
        if event.key == pygame.K_RIGHT:
            mario.moving_right = False
        elif event.key == pygame.K_LEFT:
            mario.moving_left = False
        elif event.key == pygame.K_UP:
            mario.moving_up = False
        elif event.key == pygame.K_DOWN:
            mario.moving_down = False
        elif event.key == pygame.K_SPACE:
            mario.jump_cut = True
        # elif event.key == pygame.K_c:
        #     mario.vel.x -= 2

    @staticmethod
    def check_play_button(ai_settings, menu, mouse_x, mouse_y):
        """Starts a new game when the player clicks play"""
        button_clicked = menu.play_button.rect.collidepoint(mouse_x, mouse_y)
        if button_clicked and not ai_settings.finished:
            pygame.mixer.music.play(-1)
            EventLoop.display_lives = True
            # Hide the mouse cursor.
            pygame.mouse.set_visible(False)
            ai_settings.finished = True