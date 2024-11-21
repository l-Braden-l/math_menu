#Braden Leach
#Nov 20 2024
#Math menu 


import math 
import time 
#part 1 
def calculate_circle_area(radius):
    area = math.pi * radius**2
    return area 

def calculate_power(base, exponent):
    result = base ** exponent
    return result

def calculate_triangle_area(base, height):
    area = 0.5 * base * height 
    return area

def display_menu():
    print('''         Menu:
        1. Calculate are of a circle
        2. Raise a number to a power
        3. Calculate area of a right triangle
        4. Exit
      ''')

#part 2 
def main():
    while True:
       display_menu()
       choice = float(input('Enter your menu choice (1-4 only):\n'))

       if choice == 1:
          radius = float(input('Enter the radius of the circle (in ft.): '))
          area = calculate_circle_area(radius)
          print(f'The area of the circle is {area:.2f} sq. ft.')
       elif choice == 2:
            base = float(input('Enter the base number: '))
            exponent = int(input('Enter the exponent: '))
            result = calculate_power(base,exponent)
            print(f'{base} raised to the power of {exponent} is: {result}')
       elif choice == 3:
            base = int(input('Enter the base number: '))
            height = int(input('Enter the height number: '))
            area = calculate_triangle_area(base,height)
            print(f'The area of the right triangle is: {area:.2f} sq. ft.')
       elif choice ==4:
            print('exiting the script...')
            time.sleep(2)
            print('Thank you for using my script today!')
            time.sleep(2)
            print('Goodbye!')
            break
       else:
        print('Invalid menu choice! please enter a number between 1 and 4 only.')

if __name__ == '__main__':
    main()