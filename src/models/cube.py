from dataclasses import dataclass, field

from src.config.settings import CUBE_SPACING, CUBE_SIZE, EXIT_DISTANCE, EXIT_SPEED


@dataclass
class Cube:
    cube_id: int
    position: tuple[int, int, int]
    direction: tuple[int, int, int]
    state: str = "idle"
    translation: tuple[float, float, float] = field(default_factory=lambda: (0.0, 0.0, 0.0))
    travel_distance: float = 0.0

    @property
    def selectable(self) -> bool:
        return self.state == "idle"

    @property
    def moving(self) -> bool:
        return self.state == "moving"

    @property
    def removed(self) -> bool:
        return self.state == "removed"

    @property
    def world_position(self) -> tuple[float, float, float]:
        x, y, z = self.position
        tx, ty, tz = self.translation
        return (
            (x + tx) * CUBE_SPACING,
            (y + ty) * CUBE_SPACING,
            (z + tz) * CUBE_SPACING,
        )

    def start_exit(self) -> bool:
        if not self.selectable:
            return False

        self.state = "moving"
        self.travel_distance = 0.0
        self.translation = (0.0, 0.0, 0.0)
        return True

    def update(self, dt: float) -> bool:
        if not self.moving:
            return False

        self.travel_distance += EXIT_SPEED * dt
        dx, dy, dz = self.direction
        self.translation = (
            dx * self.travel_distance,
            dy * self.travel_distance,
            dz * self.travel_distance,
        )

        if self.travel_distance >= EXIT_DISTANCE:
            self.translation = (
                dx * EXIT_DISTANCE,
                dy * EXIT_DISTANCE,
                dz * EXIT_DISTANCE,
            )
            self.state = "removed"
            return True

        return False

    @property
    def size(self) -> float:
        return CUBE_SIZE
