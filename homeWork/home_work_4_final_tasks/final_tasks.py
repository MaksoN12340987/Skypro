# Напишите функцию count_morse_characters(), которая принимает строку, состоящую из символов азбуки Морзе, и 
# возвращает количество символов (точек и/или тире) в ней
def count_morse_characters(input_string):
    input_string.replace(" ", "")

    point_counter = 0
    dash_counter = 0
    for i in range(len(input_string)):
        if input_string[i] == ".":
            point_counter += 1
        else:
            dash_counter += 1
    
    return (f"В строке {len(input_string)} символов, точек: {point_counter}, тире: {dash_counter} ")

string_morse = count_morse_characters(input())
print(string_morse)
