from single_var_euler_estimator import EulerEstimator

def derivative(t):
    return t + 1

euler = EulerEstimator(derivative)
assert euler.calc_derivative_at_point((1, 4)) == 2
assert euler.calc_estimated_points((1, 4), 0.5, 4) == [(
    1, 4), (1.5, 5.0), (2.0, 6.25), (2.5, 7.75), (3.0, 9.5)]
[(1, 4), (1.5, 5.0), (2.0, 6.25), (2.5, 7.75), (3.0, 9.5)]


def derivative(t):
    return t ** 2

euler = EulerEstimator(derivative)
assert euler.calc_derivative_at_point((2, 7)) == 4
assert euler.calc_estimated_points((2, 7), 0.25, 10) == [(2, 7), (2.25, 8.0), (2.5, 9.265625), (2.75, 10.828125), (
    3.0, 12.71875), (3.25, 14.96875), (3.5, 17.609375), (3.75, 20.671875), (4.0, 24.1875), (4.25, 28.1875), (4.5, 32.703125)]
