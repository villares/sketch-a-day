import numpy as np
import py5

# An implementation of Robert Bridson's Fast Poisson Disk Sampling algorithm
# https://www.cs.ubc.ca/~rbridson/docs/bridson-siggraph07-poissondisk.pdf


class PoissonDiscSampling(object):

    def __init__(self, field_x1_: int, field_y1_: int, field_x2_: int, field_y2_: int,
                 separation_radius_: float, point_size_: float, color_: int, number_of_retries_: int ):
        self.field_x1, self.field_y1, self.field_x2, self.field_y2 = field_x1_, field_y1_, field_x2_, field_y2_
        self.separation_radius, self.number_of_retries = separation_radius_, number_of_retries_
        self.point_size, self.color = point_size_, color_

        self.width = field_x2_ - field_x1_
        self.height = field_y2_ - field_y1_
        self.point_index = 0
        self.point_list = []

        # We will need to build an offset_aray that would define all the other grid spaces we have to look in for
        # points. I built the chart below for reference, but I'm going to sort this by positions most likely to have
        # another point to speed up the rejection of points

        #           [-1, -2], [0, -2], [1, -2],
        # [-2, -1], [-1, -1], [0, -1], [1, -1], [2, -1],
        # [-2, 0],  [-1, 0],  [0, 0],  [1, 0],  [2, 0],
        # [-2, 1],  [-1, 1],  [0, 1],  [1, 1],  [2, 1],
        #           [-1, 2],  [0, 2],  [1, 2]
        #
        # Note we don't need the point at [0, 0] since we do a quick check to make sure it is not -1

        self.grid_offset_array = np.array([[0, -1], [1, 0], [0, 1], [-1, 0], [-1, -1], [1, -1], [1, 1], [-1, 1],
                                          [0, -2], [2, 0], [0, 2], [-2, 0], [-1, -2], [1, -2], [2, -1], [2, 1],
                                          [1, 2], [-1, 2], [-2, 1], [-2, -1]], dtype=int)


        # Step 0.
        # Initialize an n - dimensional background grid for storing samples and accelerating spatial searches.
        # We pick the cell size to be bounded by r /√n, so that each grid cell will contain at most one sample,
        # and thus the grid can be implemented as a simple n - dimensional array of integers:
        # the default −1 indicates no sample, a non - negative integer gives the index of the sample located in a cell.

        # Note I am calling r separation_radius and since this is a 2d artwork, our n is 2

        self.grid_space_size = separation_radius_ / py5.sqrt(2)

        self.grid_columns: int = py5.ceil(self.width / self.grid_space_size)
        self.grid_rows: int = py5.ceil(self.height / self.grid_space_size)

        # Build a numpy array of the grid all filled with -1
        self.grid_array = np.full((self.grid_columns, self.grid_rows), -1, dtype=int)

        # Step 1.
        # Select the initial sample, x0, randomly chosen uniformly
        # from the domain. Insert it into the background grid, and initialize
        # the “active list” (an array of sample indices) with this index (zero).
        self.active_list = []

        initial_point = py5.Py5Vector2D(py5.random(self.field_x1, self.field_x2),
                                        py5.random(self.field_y1, self.field_y2))

        self.accept_point(initial_point)

        # Step 2.
        # While the active list is not empty, choose a random index from it (say i).
        # Generate up to k points chosen uniformly from the spherical annulus
        # between radius r and 2r around xi. For each point in turn, check if it is within distance r
        # of existing samples (using the background grid to only test nearby samples).
        # If a point is adequately far from existing samples, emit it as the next sample
        # and add it to the active list. If after k attempts no such point is
        # found, instead remove i from the active list.

        while self.active_list:
            active_point = py5.random_choice(self.active_list)[0]
            active_point_location = py5.Py5Vector2D(self.point_list[active_point][0], self.point_list[active_point][1])
            self.try_to_add_point(active_point, active_point_location)

    def accept_point(self, point: py5.Py5Vector2D):
        grid_x, grid_y = self.find_grid_position(point)
        self.grid_array[grid_x, grid_y] = self.point_index
        self.active_list.append(self.point_index)
        self.point_list.append([point.x, point.y])
        self.point_index += 1

    def find_grid_position(self, point: py5.Py5Vector2D):
        return_x: int = py5.floor((point.x - self.field_x1) // self.grid_space_size)
        return_y: int = py5.floor((point.y - self.field_y1) // self.grid_space_size)
        return return_x, return_y

    def try_to_add_point(self, point_index: int, point_location: py5.Py5Vector2D):
        for _ in range(self.number_of_retries):
            # Get a random unit vector (magnitude of 1)
            test_point = py5.Py5Vector2D.random()

            # Find a random magnitude between 1 and 2 radius in size
            random_magnitude = py5.random(self.separation_radius, 2 * self.separation_radius)
            test_point.set_mag(random_magnitude)

            # Finally add the active point location, so that this new test point is an offset of the original point
            # we are testing
            test_point += point_location

            if self.is_valid_point(test_point):
                # If we found a valid point we already set it in the point_array
                # so, we don't need to continue looking for points, and can accept the point and break
                self.accept_point(test_point)
                return

        # If we've exhausted our retries, remove the point from the active list
        self.active_list.remove(point_index)
        return

    def is_valid_point(self, point: py5.Py5Vector2D):
        # First check to see if we are in field boundary, and if not, return false
        if point.x < self.field_x1 or point.x > self.field_x2 or point.y < self.field_y1 or point.y > self.field_y2:
            return False

        # Next we need to find our place in the grind
        grid_x, grid_y = self.find_grid_position(point)

        # Now we do a quick check to see if there is already a point in this space
        if self.grid_array[grid_x][grid_y] >= 0:
            return False

        grid_spaces_to_search = np.subtract([grid_x, grid_y], self.grid_offset_array)

        points_to_check = []
        for grid_space in grid_spaces_to_search:
            if 0 <= grid_space[0] < self.grid_columns and 0 <= grid_space[1] < self.grid_rows:
                grid_value = self.grid_array[grid_space[0], grid_space[1]]
                if grid_value >= 0:
                    points_to_check.append(self.point_list[grid_value])

            for checked_point in points_to_check:
                if point.dist(py5.Py5Vector2D(checked_point)) < self.separation_radius:
                    return False

        # If we have made it this far, we haven't found any reason to refuse it, so return True
        return True

    def draw(self):
        py5.stroke(self.color)
        py5.stroke_weight(self.point_size)
        py5.points(self.point_list)

    def draw_background(self, background_color: int):
        py5.stroke(self.color)
        py5.stroke_weight(4)
        py5.fill(background_color)
        border = self.point_size * 2
        py5.rect_mode(py5.CORNERS)
        py5.rect(self.field_x1 - border, self.field_y1 - border, self.field_x2 + border, self.field_y2 + border)
