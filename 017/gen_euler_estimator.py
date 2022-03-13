class EulerEstimator:
    def __init__(self, derivatives):
        self.derivatives = derivatives
        self.functions = [key for key in derivatives]

    def calc_derivative_at_point(self, point):
        return {function: self.derivatives[function](point[0], point[1]) for function in self.functions}

    def calc_estimated_points(self, point, step_size, num_steps):
        current_point = point
        point_array = [current_point]
        for i in range(num_steps):
            current_point = (current_point[0] + step_size, {function: current_point[1][function] + step_size * self.calc_derivative_at_point(current_point)[function] for function in self.functions})
            point_array.append(current_point)
        return point_array
