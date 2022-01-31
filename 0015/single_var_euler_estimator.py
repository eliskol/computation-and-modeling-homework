class EulerEstimator:
    def __init__(self, derivative):
        self.derivative = derivative

    def calc_derivative_at_point(self, point):
        return self.derivative(point[0])

    def calc_estimated_points(self, point, step_size, num_steps):
        current_point = point
        point_array = [current_point]
        for i in range(num_steps):
            current_point = (current_point[0] + step_size, current_point[1] + step_size * self.calc_derivative_at_point(current_point))
            point_array.append(current_point)

        return point_array
