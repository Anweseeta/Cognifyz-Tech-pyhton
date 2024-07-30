def reverse_string(s):
    reversed_s = ""
    for char in s:
        reversed_s = char + reversed_s
    return reversed_s

input_string = "hello"
output = reverse_string(input_string)
print(output)  