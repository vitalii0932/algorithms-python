def interpolation_search(sequence: list, element: int) -> int:
    left_index = 0
    right_index = len(sequence) - 1
    left_element = sequence[left_index]
    right_element = sequence[right_index]

    while left_element < element < right_element:
        index = int((element - left_element) * (left_index - right_index) / (left_element - right_element) + left_index)

        if sequence[index] == element:
            return index
        elif sequence[index] < element:
            left_index = index + 1
        else:
            right_index = index - 1

        left_element = sequence[left_index]
        right_element = sequence[right_index]

    return -1


if __name__ == '__main__':
    sequence = [-2, 0, 3, 5, 7, 9, 11, 15, 18]
    cases = {3: True, 8: False}

    for element in cases.keys():
        expected_result = cases[element]
        algorithm_result = interpolation_search(sequence, element)
        is_found = algorithm_result != -1

        if is_found != expected_result:
            print(f'Error in case: {element}, expected {cases[element]}')
        else:
            print(f'Element: {element} in position {algorithm_result}')
