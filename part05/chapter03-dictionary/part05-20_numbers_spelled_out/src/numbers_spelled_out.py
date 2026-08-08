def dict_of_numbers():
    dictionary = {}
    ones = [
        "zero", "one", "two", "three", "four", 
        "five", "six", "seven", "eight", "nine",
        "ten", "eleven", "twelve", "thirteen", "fourteen", 
        "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"
    ]
    
    tens = [
        "", "", "twenty", "thirty", "forty", 
        "fifty", "sixty", "seventy", "eighty", "ninety"
    ]
    for i in range(0, 20):
        dictionary[i] = ones[i]
    for j in range(20, 100):
        first_digit = j // 10
        second_digit = j % 10
        if second_digit != 0:
            dictionary[j] = f"{tens[first_digit]}-{ones[second_digit]}"
        else:
            dictionary[j] = tens[first_digit]
    return dictionary