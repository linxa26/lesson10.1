expenses = 0
sum = 0
while True:
    user_input = input()
    if user_input == 'stop':
        break
    else:
        sum += user_input
print(sum)
