def bruteforce(message):

    alphabet = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWYXZ"

    for a in range(0, 101):

        for b in range(0, 101):

            output_list = []
            decoded_numbers = []

            for char_code in message:

                char_code = char_code - b

                if char_code < 0:
                    break

                if a != 0:
                    char_code = char_code / a

                    if char_code % 1 != 0 or char_code > 52:
                        break

                    else:
                        decoded_numbers.append(int(char_code))
                        output_list.append(alphabet[int(char_code)])

                else:
                    break
            else:
                print(decoded_numbers)
                print(''.join(output_list))

bruteforce([377, 717, 71, 513, 105, 921, 581, 547, 547, 105, 377, 717, 241, 71, 105, 547, 71,377, 547, 717, 751, 683, 785, 513, 241, 547, 751])