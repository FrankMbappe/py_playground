def build_str(string, count):
    result = ""
    for i in range(count):
        result += string
    return result


def display_flag(stars_count):
    for count in range(stars_count):
        print(build_str("*", count))
    for count in range(stars_count, 0, -1):
        print(build_str("*", count))


def display_mountain(stars_count):
    space_displayed_count = stars_count // 2
    stars_displayed_count = 1
    iter_count = space_displayed_count + 1

    for i in range(iter_count):
        spaces = build_str(" ", space_displayed_count)
        stars = build_str("*", stars_displayed_count)
        print(spaces + stars)
        space_displayed_count -= 1
        stars_displayed_count += 2


def main():
    # FLag
    flag_stars_count = int(input("How many stars for the flag? : "))
    display_flag(flag_stars_count)

    # Mountain
    mountain_stars_count = int(input("How many stars for the mountain? Please enter an odd number : "))
    while mountain_stars_count % 2 == 0:
        mountain_stars_count = int(input("For the mountain you should enter an odd number : "))

    display_mountain(mountain_stars_count)


main()
