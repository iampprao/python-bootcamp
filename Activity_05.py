input_line = input('enter elements of a list ')
print("\n")
number_string_list = input_line.split(' ')
print('list: ', number_string_list)

for i in range(len(number_string_list)):
    number_string_list[i]=int(number_string_list[i])
print("sum= ",sum(number_string_list))
