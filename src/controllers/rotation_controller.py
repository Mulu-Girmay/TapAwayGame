from src.config.settings import ROTATION_SENSITIVITY
from src.utils.matrix_utils import identity_matrix, multiply_matrices, rotation_matrix_x, rotation_matrix_y


class RotationController:
    def __init__(self):
        self.matrix = identity_matrix()
        self.sensitivity = ROTATION_SENSITIVITY

    def rotate(self, dx: float, dy: float) -> None:
        yaw = rotation_matrix_y(dx * self.sensitivity)
        pitch = rotation_matrix_x(dy * self.sensitivity)
        delta = multiply_matrices(yaw, pitch)
        self.matrix = multiply_matrices(delta, self.matrix)

    def reset(self) -> None:
        self.matrix = identity_matrix()
