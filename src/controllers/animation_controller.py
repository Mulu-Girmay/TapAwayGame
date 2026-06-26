class AnimationController:
    def __init__(self):
        self.animations = []

    @property
    def busy(self) -> bool:
        return len(self.animations) > 0

    def add_animation(self, cube) -> bool:
        if not cube.start_exit():
            return False

        self.animations.append(cube)
        return True

    def update(self, dt):
        completed = []
        remaining = []

        for cube in self.animations:
            if cube.update(dt):
                completed.append(cube)
            else:
                remaining.append(cube)

        self.animations = remaining
        return completed
