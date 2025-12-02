def validate_isbn(isbn, length):
    # Check if ISBN is the correct length
    if len(isbn) != length:
        print(f'ISBN-{length} code should be {length} digits long.')
        return False
    
    # Check for invalid characters
    if length == 10:
        # ISBN-10 can have digits or X as the last character
        if not (isbn[:-1].isdigit() and (isbn[-1].isdigit() or isbn[-1].upper() == 'X')):
            print('Invalid character was found.')
            return False
    else:  # length == 13
        # ISBN-13 should be all digits
        if not isbn.isdigit():
            print('Invalid character was found.')
            return False
    
    # Extract main digits and check digit
    main_digits = isbn[:length-1]
    given_check_digit = isbn[length-1].upper()  # Handle X for ISBN-10
    
    # Convert main digits to list of integers
    main_digits_list = [int(digit) for digit in main_digits]
    
    # Calculate the check digit from other digits
    if length == 10:
        expected_check_digit = calculate_check_digit_10(main_digits_list)
    else:
        expected_check_digit = calculate_check_digit_13(main_digits_list)
    
    # Check if the given check digit matches with the calculated check digit
    if given_check_digit == expected_check_digit:
        print('Valid ISBN Code.')
        return True
    else:
        print('Invalid ISBN Code.')
        return False


def calculate_check_digit_10(main_digits_list):
    # Note: You don't have to fully understand the logic in this function.
    digits_sum = 0
    # Multiply each of the first 9 digits by its corresponding weight (10 to 2) and sum up the results
    for index, digit in enumerate(main_digits_list):
        digits_sum += digit * (10 - index)
    
    # Find the remainder of dividing the sum by 11, then subtract it from 11
    result = 11 - digits_sum % 11
    
    # The calculation result can range from 1 to 11.
    # If the result is 11, use 0.
    # If the result is 10, use upper case X.
    # Use the value as it is for other numbers.
    if result == 11:
        expected_check_digit = '0'
    elif result == 10:
        expected_check_digit = 'X'
    else:
        expected_check_digit = str(result)
    
    return expected_check_digit


def calculate_check_digit_13(main_digits_list):
    # Note: You don't have to fully understand the logic in this function.
    digits_sum = 0
    # Multiply each of the first 12 digits by 1 and 3 alternately (starting with 1), and sum up the results
    for index, digit in enumerate(main_digits_list):
        if index % 2 == 0:
            digits_sum += digit * 1
        else:
            digits_sum += digit * 3
    
    # Find the remainder of dividing the sum by 10, then subtract it from 10
    result = 10 - digits_sum % 10
    
    # The calculation result can range from 1 to 10.
    # If the result is 10, use 0.
    # Use the value as it is for other numbers.
    if result == 10:
        expected_check_digit = '0'
    else:
        expected_check_digit = str(result)
    
    return expected_check_digit


def main():
    user_input = input('Enter ISBN and length: ')
    
    # Check if input contains comma
    if ',' not in user_input:
        print('Enter comma-separated values.')
        return
    
    values = user_input.split(',')
    
    # Check if we have exactly 2 values
    if len(values) != 2:
        print('Enter comma-separated values.')
        return
    
    isbn = values[0].strip()
    length_str = values[1].strip()
    
    # Check if length is numeric
    if not length_str.isdigit():
        print('Length must be a number.')
        return
    
    length = int(length_str)
    
    # Check if length is valid
    if length == 10 or length == 13:
        validate_isbn(isbn, length)
    else:
        print('Length should be 10 or 13.')


# Comment out the main function call to allow for the rest of the tests to work properly
# main()
