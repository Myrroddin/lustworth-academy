init -1 python:
    import math

    class Vector:
        def __init__(self, x, y):
            self.x = x
            self.y = y
        
        def __add__(self, b):
            x = self.x + b.x
            y = self.y + b.y
            return Vector(x, y)
        
        def __sub__(self, b):
            x = self.x - b.x
            y = self.y - b.y
            return Vector(x, y)
        
        def __mul__(self, b):
            x = self.x * b
            y = self.y * b
            return Vector(x, y)

        def __rmul__(self, b):
            return self.__mul__(b)

        def __div__(self, b):
            x = self.x / b
            y = self.y / b
            return Vector(x, y)

        def __truediv__(self, b):
            return self.__div__(b)
        
        def __eq__(self, other):
            if isinstance(other, Vector):
                return self.x == other.x and self.y == other.y
            elif isinstance(other, tuple) and len(other) == 2:
                return self.x == other[0] and self.y == other[1]
            return NotImplemented
        
        def magnitude(self):
            return math.sqrt(self.x ** 2 + self.y ** 2)
        
        def normalized(self):
            mag = self.magnitude()
            if mag == 0:
                return Vector(0, 0)
            return self / mag
        
        def __iter__(self):
            return iter((self.x, self.y))
        
        def __str__(self):
                return "({:0.1f}, {:0.1f})".format(self.x, self.y)

    class RigidBody:
        def __init__(self, mass, maxSpd):
            self.mass = mass
            self.maxSpd = maxSpd
            # kinematics
            self.pos = Vector(0, 0)
            self.vel = Vector(0, 0)
            self.acc = Vector(0, 0)

            self.netForce = Vector(0, 0)
        
        def update_physics(self, dt):
            # update acceleration
            self.acc = self.netForce / self.mass
            # update velocity
            self.vel += self.acc * dt
            # cap speed at maxSpd
            spd = self.speed()
            if spd > self.maxSpd:
                self.vel = self.maxSpd * self.vel.normalized()
            elif spd < 0.1:
                self.vel = Vector(0, 0)
            # update position
            self.pos += self.vel * dt
            # reset forces
            self.netForce = Vector(0, 0)
        
        def add_force(self, force):
            self.netForce += force
        
        def colliding(self, other):
            rectA = self.get_bounds()
            rectB = other.get_bounds()
            return rectA.colliderect(rectB)
        
        def speed(self):
            return self.vel.magnitude()

        def get_bounds(self):
                raise Exception("get_bounds() not implemented.")
