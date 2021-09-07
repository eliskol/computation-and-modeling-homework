def bruteforce(message):

    alphabet = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWYXZ"

    for a in range(0, 101):

        for b in range(0, 101):

            output_list = []

            for char_code in message:

                char_code = char_code - b

                if char_code < 0:
                    break

                if a != 0:
                    char_code = char_code / a

                    if char_code % 1 != 0 or char_code > 52:
                        break

                    else:
                        output_list.append(alphabet[int(char_code)])

                else:
                    break
            else:
                print(''.join(output_list))