def resistor_label(colors):
    DIGITS = {"black": 0, "brown": 1, "red": 2, "orange": 3,"yellow": 4, "green": 5, "blue": 6,"violet": 7, "grey": 8, "white": 9}
    TOLERANCE = {"grey": 0.05, "violet": 0.1, "blue": 0.25,"green": 0.5, "brown": 1, "red": 2,"gold": 5, "silver": 10}
    if len(colors) == 1:
        return '0 ohms'
    if len(colors) == 4:
        digit = colors[:2]
        multiplier_color = colors[2]
        tolerance_color = colors[-1]
    if len(colors) == 5:
        digit = colors[:3]
        multiplier_color = colors[3]
        tolerance_color = colors[-1]
    digits_str = ''
    for color in digit:
        digits_str = digits_str + str(DIGITS[color])
    number = int(digits_str)
    number = number * 10**(DIGITS[multiplier_color])
    unit = 'ohms'
    if number >= 1_000_000:
        number /= 1_000_000
        unit = 'megaohms'
    elif number >= 1_000:
        number /= 1_000
        unit = 'kiloohms'
    if number == int(number):
        number = int(number)
    return f'{number} {unit} ±{TOLERANCE[tolerance_color]}%'