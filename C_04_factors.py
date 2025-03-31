def find_factors(to_factor):
    all_factors = []

    # find square root of number to be factored so that our loop is efficient.
    stop_raw = to_factor ** 0.5
    stop = int(stop_raw + 1)

    # loop and check each number from one upwards to check if it's a
    # factor.  Stop when we get to the square root of the number (ie: 'half way')
    for item in range(1, stop):
        num_left = to_factor % item
        # If number fits evenly it will add it to the list
        if num_left == 0:
            all_factors.append(item)

            # retrieve the second 'partner' factor as an integer
            partner = to_factor // item

            # only add factor to list if it is not already in the list
            if partner not in all_factors:
                all_factors.append(partner)

    all_factors.sort()

    if len(all_factors) > 1:
        print(f"The factors of {to_factor} are: {all_factors}\n")

    return all_factors


to_find = int(input("What do you want to find the factors of? "))
found_factors = find_factors(to_find)
print(found_factors)
