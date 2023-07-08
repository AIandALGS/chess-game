import pygame
import copy

from manager.chess_manager import ChessManager
from manager.sound_manager import EffectsManager

from src.chess_pieces.chess_move import ChessMove
from src.utilities.matrix import Matrix
from src.utilities.utils import Utils
from src.gui.mouse import Mouse

from src.constants import (
    BOARD_SIZE,
    SQUARE_SIZE,
    LIGHT_SQUARE,
    DARK_SQUARE,
    WHITE_INITIAL_POSITIONS,
    BLACK_INITIAL_POSITIONS,
    CASTLING_RIGHTS,
    WHITE_KING_POSITION,
    WHITE_KING_LEFT_POSITION,
    WHITE_KING_RIGHT_POSITION,
    BLACK_KING_POSITION,
    BLACK_KING_LEFT_POSITION,
    BLACK_KING_RIGHT_POSITION,
    LEFT_ROOK_POSITION,
    RIGHT_ROOK_POSITION,
)


class Board:
    def __init__(self):
        self.__current_player = "white"
        self.__castling_rights = CASTLING_RIGHTS
        self.__board = self.initialize_board()
        self.__rects = self.initialize_rects()
        self.__effects_manager = EffectsManager()
        self.__mouse = Mouse()
        self.__legal_moves = ChessMove.get_legal_moves(
            self.__board, self.__current_player, self.__castling_rights
        )
        self.__player_moves = []
        self.__selected = False
        self.__current_position = None

    @staticmethod
    def get_empty_square(board, position):
        return board[position] is None

    def initialize_board(self):
        board = dict()

        for y in range(BOARD_SIZE):
            for x in range(BOARD_SIZE):
                position = (x, y)
                board[position] = None

        for white_position, white_type in WHITE_INITIAL_POSITIONS.items():
            board[white_position] = white_type

        for black_position, black_type in BLACK_INITIAL_POSITIONS.items():
            board[black_position] = black_type

        return board

    def initialize_rects(self):
        rects = dict()

        for position in self.__board:
            global_position = Utils.get_global_position(position)
            rect = pygame.Rect(*global_position, *SQUARE_SIZE)
            rects[position] = rect

        return rects

    def get_list_of_rects(self):
        return self.__rects.values()

    def check_collision_and_clicked(self, mouse_clicked, rect):
        return mouse_clicked and rect.collidepoint(Mouse.get_position())

    def clear_moveset(self):
        self.__player_moves.clear()
        self.__selected = False
        self.__current_position = None

    def get_player_moves(self, position):
        if Utils.is_player_piece(self.__board, position, self.__current_player):
            self.__player_moves = copy.copy(self.__legal_moves[position])
            self.__selected = True
            self.__current_position = position

    def change_player(self):
        self.__current_player = "black" if self.__current_player == "white" else "white"
        self.__legal_moves = ChessMove.get_legal_moves(
            self.__board, self.__current_player, self.__castling_rights)

        if ChessMove.is_checkmate(
            self.__board, self.__current_player, self.__legal_moves
        ):
            self.__effects_manager.play_checkmate_sound()

        elif ChessMove.is_stalemate(
            self.__board, self.__current_player, self.__legal_moves
        ):
            self.__effects_manager.play_stalemate_sound()

        elif ChessMove.is_check(self.__board, self.__current_player):
            self.__effects_manager.play_check_sound()

    def can_castle_left(self, position):
        player_castling_rights = self.__castling_rights[self.__current_player]
        chess_type = self.__board[self.__current_position]
        king_piece = chess_type is not None and "king" in chess_type.name.lower()
        king_position = WHITE_KING_POSITION if self.__current_player == "white" else BLACK_KING_POSITION
        left_king_position = WHITE_KING_LEFT_POSITION if self.__current_player == "white" else BLACK_KING_LEFT_POSITION

        return player_castling_rights[LEFT_ROOK_POSITION] and player_castling_rights[king_position] and position == left_king_position and king_piece

    def can_castle_right(self, position):
        player_castling_rights = self.__castling_rights[self.__current_player]
        chess_type = self.__board[self.__current_position]
        king_piece = chess_type is not None and "king" in chess_type.name.lower()
        king_position = WHITE_KING_POSITION if self.__current_player == "white" else BLACK_KING_POSITION
        right_king_position = WHITE_KING_RIGHT_POSITION if self.__current_player == "white" else BLACK_KING_RIGHT_POSITION

        return player_castling_rights[RIGHT_ROOK_POSITION] and player_castling_rights[king_position] and position == right_king_position and king_piece

    def castle_left(self):
        king_position = WHITE_KING_POSITION if self.__current_player == "white" else BLACK_KING_POSITION
        left_king_position = WHITE_KING_LEFT_POSITION if self.__current_player == "white" else BLACK_KING_LEFT_POSITION

        rook_position = (left_king_position[0] + 1, left_king_position[1])

        self.__board[rook_position] = self.__board[LEFT_ROOK_POSITION]
        self.__board[left_king_position] = self.__board[king_position]
        self.__board[king_position] = None
        self.__board[LEFT_ROOK_POSITION] = None

        self.__effects_manager.play_castle_sound()

    def castle_right(self):
        king_position = WHITE_KING_POSITION if self.__current_player == "white" else BLACK_KING_POSITION
        right_king_position = WHITE_KING_RIGHT_POSITION if self.__current_player == "white" else BLACK_KING_RIGHT_POSITION

        rook_position = (right_king_position[0] - 1, right_king_position[1])

        self.__board[rook_position] = self.__board[RIGHT_ROOK_POSITION]
        self.__board[right_king_position] = self.__board[king_position]
        self.__board[king_position] = None
        self.__board[RIGHT_ROOK_POSITION] = None

        self.__effects_manager.play_castle_sound()

    def default_move(self, position):
        self.__effects_manager.play_sound(self.__board, position)

        self.__board[position] = self.__board[self.__current_position]
        self.__board[self.__current_position] = None

    def make_move(self, position):
        if self.can_castle_left(position):
            self.castle_left()
        elif self.can_castle_right(position):
            print("true")
            self.castle_right()
        else:
            self.default_move(position)

        self.update_castling_rights(
            (position, self.__current_position))
        self.__board = Matrix.rotate_board(self.__board)
        self.clear_moveset()
        self.change_player()

    def update_moves(self, mouse_clicked, position):
        for move in self.__player_moves:
            if self.check_collision_and_clicked(mouse_clicked, move):
                self.make_move(position)

    def update_castling_rights(self, positions):
        for position in positions:
            if position in self.__castling_rights[self.__current_player]:
                self.__castling_rights[self.__current_player][position] = False

    def update(self, events):
        mouse_clicked = Mouse.get_mouse_click(events)
        position = Mouse.get_local_mouse_position()

        if mouse_clicked:
            if not self.__selected or self.__current_position != position:
                self.get_player_moves(position)
            else:
                self.clear_moveset()

        self.update_moves(mouse_clicked, position)

    def draw_board(self, screen):
        for position in self.__board:
            x = position[0]
            y = position[1]

            if (not (x % 2) and not (y % 2)) or (x % 2 and y % 2):
                pygame.draw.rect(screen, LIGHT_SQUARE, self.__rects[position])
            else:
                pygame.draw.rect(screen, DARK_SQUARE, self.__rects[position])

    def render(self, screen):
        for position in self.__board:
            if self.__board[position] is not None:
                chess_txtr, chess_rect = ChessManager.get_chess_piece(
                    self.__board, position
                )
                screen.blit(chess_txtr, chess_rect)

        self.__mouse.render(
            screen, self.get_list_of_rects(), self.__player_moves)
