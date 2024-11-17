# Напишите функцию count_morse_characters(), которая принимает строку, состоящую из символов азбуки Морзе, и 
# возвращает количество символов (точек и/или тире) в ней
def count_morse_characters(input_string):
    point_counter = 0
    dash_counter = 0
    for i in range(len(input_string)):
        if input_string[i] == ".":
            point_counter += 1
        else:
            dash_counter += 1
    
    return (point_counter + dash_counter)


string_morse = input().replace(" ", "")
print(count_morse_characters(string_morse))
