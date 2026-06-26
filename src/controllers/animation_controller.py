class AnimationController:

    def __init__(self):
        self.animations = []

    def add_animation(self, cube):
        self.animations.append({
            "cube": cube,
            "progress": 0
        })

    def update(self, dt):

        for anim in self.animations:

            anim["progress"] += dt * 0.5

            cube = anim["cube"]
            dx, dy, dz = cube.direction

            cube.position = (
                cube.position[0] + dx * 0.1,
                cube.position[1] + dy * 0.1,
                cube.position[2] + dz * 0.1,
            )

        self.animations = [
            a for a in self.animations if a["progress"] < 1
        ]