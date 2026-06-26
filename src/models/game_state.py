class GameState:
    def __init__(self):
        self.moves = 0
        self.remaining = 0
        self.won = False
        self.level_index = 0
        self.level_name = ""

    def reset_for_level(self, level_index: int, level_name: str, remaining: int) -> None:
        self.level_index = level_index
        self.level_name = level_name
        self.moves = 0
        self.remaining = remaining
        self.won = False

    def record_move(self) -> None:
        self.moves += 1

    def sync_remaining(self, remaining: int) -> None:
        self.remaining = remaining
        self.won = remaining == 0
