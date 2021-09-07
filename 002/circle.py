def distance(x1, y1, x2, y2):

    distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

    return distance


def circ_random(a, b, decimal_places):

    return round(random.uniform(a, b), decimal_places)


def random_circ_point(lower_x, lower_y, decimal_places):

    total_x = 0

    total_y = 0

    amount_of_coords = 0

    for i in range(0, 1000):

        random_y = circ_random(lower_x, 1, decimal_places)

        y_upper_bound = 1 - random_y**2

        random_x = circ_random(lower_y, y_upper_bound, decimal_places)

        if distance(0, 0, random_x, random_y) < 1:

            #print([random_x, random_y])

            total_x += random_x

            total_y += random_y

            amount_of_coords += 1

        else:
            break


    return [round(total_x / amount_of_coords, decimal_places), round(total_y / amount_of_coords, decimal_places)]

print(random_circ_point(0, 0, 6))





"""
def circle_point_guesser(x, y, precision):

    guess_x = 0

    guess_y = 0

    places = int(len(str(precision).split('.')[1]))

    while (distance(guess_x, guess_y, x, y) > precision):

        if guess_x > x:

            if guess_y > y:

                for i in range(0, 20):

                    circ_random(0)


            elif guess_y < y:

            elif guess_y = y:

        if guess_x < x:

            if guess_y > y:

            elif guess_y < y:

            elif guess_y = y:

        if guess_x = x:

            if guess_y > y:

            elif guess_y < y:

            elif guess_y = y:

"""
