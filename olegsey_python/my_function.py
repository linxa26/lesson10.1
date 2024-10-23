def get_sum(file):
    with open(file, 'r') as file:
        sum = 0
        for payment in file:
            sum += int(payment)
        return sum

# def get_number(file):
#     with open(file, 'r') as file:
#         if


