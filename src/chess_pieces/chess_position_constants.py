from src.chess_pieces.chess_type import ChessType

WHITE_INITIAL_POSITIONS = {
    (0, 6): ChessType.WHITE_PAWN,
    (1, 6): ChessType.WHITE_PAWN,
    (2, 6): ChessType.WHITE_PAWN,
    (3, 6): ChessType.WHITE_PAWN,
    (4, 6): ChessType.WHITE_PAWN,
    (5, 6): ChessType.WHITE_PAWN,
    (6, 6): ChessType.WHITE_PAWN,
    (7, 6): ChessType.WHITE_PAWN,
    (0, 7): ChessType.WHITE_ROOK,
    (7, 7): ChessType.WHITE_ROOK,
    (1, 7): ChessType.WHITE_KNIGHT,
    (6, 7): ChessType.WHITE_KNIGHT,
    (2, 7): ChessType.WHITE_BISHOP,
    (5, 7): ChessType.WHITE_BISHOP,
    (3, 7): ChessType.WHITE_QUEEN,
    (4, 7): ChessType.WHITE_KING,
}

BLACK_INITIAL_POSITIONS = {
    (0, 1): ChessType.BLACK_PAWN,
    (1, 1): ChessType.BLACK_PAWN,
    (2, 1): ChessType.BLACK_PAWN,
    (3, 1): ChessType.BLACK_PAWN,
    (4, 1): ChessType.BLACK_PAWN,
    (5, 1): ChessType.BLACK_PAWN,
    (6, 1): ChessType.BLACK_PAWN,
    (7, 1): ChessType.BLACK_PAWN,
    (0, 0): ChessType.BLACK_ROOK,
    (7, 0): ChessType.BLACK_ROOK,
    (1, 0): ChessType.BLACK_KNIGHT,
    (6, 0): ChessType.BLACK_KNIGHT,
    (2, 0): ChessType.BLACK_BISHOP,
    (5, 0): ChessType.BLACK_BISHOP,
    (3, 0): ChessType.BLACK_QUEEN,
    (4, 0): ChessType.BLACK_KING,
}
