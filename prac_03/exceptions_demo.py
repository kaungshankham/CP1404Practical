"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
2. When will a ZeroDivisionError occur?
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")

# Questions
# When will a ValueError occur?
# ValueError will occur when the input value type is not the same with prompt type.
# When will a ZeroDivisionError occur?
# If users input 0 to the denominator, ZeroDivision Error occur.
# Could you change the code to avoid the possibility of a ZeroDivisionError?
# Yes
