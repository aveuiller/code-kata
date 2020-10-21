import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.


class Speeder:
    MIN_VIRAGE_ANGLE = 30
    VIRAGE_OFFSET = 500
    MAX_VIRAGE_ANGLE = 90

    def __init__(self):
        self.boost_available = True

    def _configure_speed(self, nc_angle, nc_dist):
        speed = 100
        if abs(nc_angle) > self.MAX_VIRAGE_ANGLE:
            speed = 10
        elif abs(nc_angle) == 0 and nc_dist > 4000 and self.boost_available:
            speed = "BOOST"
            self.boost_available = False

        return speed

    def next_move(self, x, y, nc_x, nc_y, nc_angle, nc_dist):
        dest_x = next_checkpoint_x
        dest_y = next_checkpoint_y
        speed = self._configure_speed(nc_angle, nc_dist)

        print(f"dest_x: {dest_x}; dest_y: {dest_y}; speed: {speed}", file=sys.stderr, flush=True)

        return str(dest_x) + " " + str(dest_y) + " " + str(speed)

SPEEDER = Speeder()

# game loop
while True:
    # next_checkpoint_x: x position of the next check point
    # next_checkpoint_y: y position of the next check point
    # next_checkpoint_dist: distance to the next checkpoint
    # next_checkpoint_angle: angle between your pod orientation and the direction of the next checkpoint
    (
        x, y,
        next_checkpoint_x, next_checkpoint_y,
        next_checkpoint_dist, next_checkpoint_angle
    ) = [int(i) for i in input().split()]

    opponent_x, opponent_y = [int(i) for i in input().split()]

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)
    print(
        f"x: {x}; y: {y}; next_x: {next_checkpoint_x} next_y: {next_checkpoint_y}, "
        f"dist: {next_checkpoint_dist}, angle: {next_checkpoint_angle}, ",
        file=sys.stderr, flush=True
    )
    # You have to output the target position
    # followed by the power (0 <= thrust <= 100)
    # i.e.: "x y thrust"
    line = SPEEDER.next_move(
        x, y,
        next_checkpoint_x, next_checkpoint_y,
        next_checkpoint_angle, next_checkpoint_dist
    )
    print(line)
