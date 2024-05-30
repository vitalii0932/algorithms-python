def linear_search(sequence: list, element: int) -> int:
    for i in range(len(sequence)):
        if sequence[i] == element:
            return i
    return -1


if __name__ == '__main__':
    sequence = [-2, 0, 14, 5, 7, -9, 11, 2, 5]
    cases = {14: True, -6: False}

    for element in cases.keys():
        expected_result = cases[element]
        algorithm_result = linear_search(sequence, element)
        is_found = algorithm_result != -1

        if is_found != expected_result:
            print(f'Error in case: {element}, expected {cases[element]}')
        else:
            print(f'Element: {element} in position {algorithm_result}')
