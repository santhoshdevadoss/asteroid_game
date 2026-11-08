import pygame
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, LINE_WIDTH
from logger import log_event
import random
class Asteroid(CircleShape):
	def __init__(self, x: float, y: float, radius: float) -> None:
		super().__init__(x, y, radius)


	def draw(self,screen: pygame.Surface):
	    pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

	def update(self, dt: float) -> None:
	    speed_vector = self.velocity * dt
	    self.position += speed_vector

	def split(self) :

	    self.kill()
	    if self.radius==ASTEROID_MIN_RADIUS:
	        return
	    else:
	        log_event("asteroid_split")

	        self.velocity1=self.velocity.rotate(random.uniform(20,50))
	        self.velocity2=self.velocity.rotate(random.uniform(-20,-50))
	        new_radius=self.radius-ASTEROID_MIN_RADIUS
	        asteroid1=Asteroid(self.position.x,self.position.y,new_radius)
	        asteroid2=Asteroid(self.position.x,self.position.y,new_radius)
	        asteroid1.velocity = self.velocity1 * 1.2
	        asteroid2.velocity = self.velocity2 * 1.2
