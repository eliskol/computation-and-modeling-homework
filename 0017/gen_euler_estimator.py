class EulerEstimator:
    def __init__(self, derivatives):
        self.derivatives = derivatives
        self.dimensions = [key for key in derivatives]

    def calc_derivative_at_point(self, point):
        return {dimension: self.derivatives[dimension](point[0], point[1]) for dimension in self.dimensions}

    def calc_estimated_points(self, point, step_size, num_steps):
        current_point = point
        point_array = [current_point]
        for i in range(num_steps):
            current_point = (current_point[0] + step_size, {dimension: current_point[1][dimension] + step_size * self.calc_derivative_at_point(current_point)[dimension] for dimension in self.dimensions})
            point_array.append(current_point)
        return point_array
