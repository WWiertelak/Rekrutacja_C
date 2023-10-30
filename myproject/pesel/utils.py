def is_valid_pesel(pesel):
    '''Checks if PESEL is valid.'''
    # Check if PESEL is 11 digits long and contains only digits
    if len(pesel) != 11 or not pesel.isdigit():
        return False
    # Check control sum
    weights = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]
    check_sum = sum(w * int(p) for w, p in zip(weights, pesel))
    check_digit = 10 - (check_sum % 10)
    if check_digit == 10:
        check_digit = 0
    # Check last digit
    if int(pesel[-1]) != check_digit:
        return False

    return True


def extract_birth_date(pesel):
    '''Extracts birth date from PESEL.'''
    year = int(pesel[:2])
    month = int(pesel[2:4])
    day = int(pesel[4:6])

    if 1 <= month <= 12:
        year += 1900
    elif 21 <= month <= 32:
        month -= 20
        year += 2000
    elif 81 <= month <= 92:
        month -= 80
        year += 1800

    return f"{year:04}-{month:02}-{day:02}"


def extract_gender(pesel):
    '''Check gender from PESEL.'''
    if int(pesel[-2]) % 2 == 0:
        return "Kobieta"
    else:
        return "Mężczyzna"
