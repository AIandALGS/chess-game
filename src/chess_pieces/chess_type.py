from strenum import StrEnum


class ChessType(StrEnum):

    # White pieces
    WHITE_KING: str = "data/textures/white/white_king.png"
    WHITE_QUEEN: str = "data/textures/white/white_queen.png"
    WHITE_ROOK: str = "data/textures/white/white_rook.png"
    WHITE_KNIGHT: str = "data/textures/white/white_knight.png"
    WHITE_BISHOP: str = "data/textures/white/white_bishop.png"
    WHITE_PAWN: str = "data/textures/white/white_pawn.png"

    # Black pieces
    BLACK_KING: str = "data/textures/black/black_king.png"
    BLACK_QUEEN: str = "data/textures/black/black_queen.png"
    BLACK_ROOK: str = "data/textures/black/black_rook.png"
    BLACK_KNIGHT: str = "data/textures/black/black_knight.png"
    BLACK_BISHOP: str = "data/textures/black/black_bishop.png"
    BLACK_PAWN: str = "data/textures/black/black_pawn.png"
