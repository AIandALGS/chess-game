from src.constants import SQUARE_WIDTH, SQUARE_HEIGHT

class Utils:

    @staticmethod
    def get_global_position(position):
        global_x = position[0] * SQUARE_WIDTH
        global_y = position[1] * SQUARE_HEIGHT

        return (global_x, global_y) 
