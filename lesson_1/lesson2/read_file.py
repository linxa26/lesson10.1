# file = open('test.txt', 'rt') #read,txt
# # file = open('test.txt', 'rb') #read, binary
# # content = file.read()
# # print(content)

# file = open('test.txt', 'rt')
# for line in file:
#     print(line)
# file.close() это все тоже самое, что и сверху

# эта штка не требует закры
with open('test.txt', 'rt') as file:
    for line in file:
        print(line)

