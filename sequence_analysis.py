def product_of_list(lst):
    if not lst:
        return 1
    return lst[0] * product_of_list(lst[1:])

def sequence_analysis(n):
    sequence = list(range(n))
    sum_of_elements = sum(sequence)
    product_of_elements = product_of_list(sequence)
    return {
        'list': sequence,
        'sum': sum_of_elements,
        'product': product_of_elements
    }


print(sequence_analysis(10))