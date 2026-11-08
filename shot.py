import pygame
from circleshape import CircleShape
from constants import LINE_WIDTH
from constants import SHOT_RADIUS

class Shot(CircleShape):
    def __init__(self, x: float, y: float) -> None:
        super().__init__(x, y, SHOT_RADIUS)

    def draw(self,screen: pygame.Surface):
	    pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt: float) -> None:
	    speed_vector = self.velocity * dt
	    self.position += speed_vector
