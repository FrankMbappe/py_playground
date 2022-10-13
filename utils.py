text = "L 5 wddeed qdwqqwd wqdqqd dqwqwdqw dqwddqw\n" \
       "L 8 wddeed qdwqqwd wqdqqd dqwqwdqw dqwddqw\n" \
       "L 1 wddeed qdwqqwd wqdqqd dqwqwdqw dqwddqw\n" \
       "L 9 wddeed qdwqqwd wqdqqd dqwqwdqw dqwddqw\n" \
       "L 2 wddeed qdwqqwd wqdqqd dqwqwdqw dqwddqw\n" \
       "L 15 wddeed qdwqqwd wqdqqd dqwqwdqw dqwddqw\n"

array = text.splitlines()


def sort_elements(arr):
    numbers = list(map(lambda e: int(str(e).split(" ")[1]), arr))
    numbers_dict = {k: v for k, v in enumerate(numbers)}
    sorted_numbers_dict = sorted(numbers_dict.items(), key=lambda k: k[1], reverse=True)
    return sorted_numbers_dict


print(sort_elements(array))
