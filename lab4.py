def is_pythagorean_triple(a: int, b: int, c: int) -> bool:
    # implement your code in one line
    if a ** 2 + b ** 2 == c ** 2:
        return True
    else:
        return False


input_data_pythagorean_triple = [(3, 4, 5), (5, 12, 13), (6, 8, 10), (7, 24, 25), (2, 3, 4), (0, 4, 4)]
output_data_pythagorean_triple = [True, True, True, True, False, False]

for input_values, output_value in zip(input_data_pythagorean_triple, output_data_pythagorean_triple):
    assert is_pythagorean_triple(*input_values) == output_value
