def describe_sequence(n):
    sequence = list(range(n))
    length_of_sequence = len(sequence)
    type_of_first_element = type(sequence[0]) if sequence else None
    return (sequence, length_of_sequence, type_of_first_element)

print(describe_sequence(10))