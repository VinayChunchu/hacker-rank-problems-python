'''

Camel Case is a naming style common in many programming languages. In Java, method and variable names typically start with a lowercase letter, with all subsequent words starting with a capital letter (example: startThread). Names of classes follow the same pattern, except that they start with a capital letter (example: BlueCar).

Your task is to write a program that creates or splits Camel Case variable, method, and class names.

Input Format

Each line of the input file will begin with an operation (S or C) followed by a semi-colon followed by M, C, or V followed by a semi-colon followed by the words you'll need to operate on.
The operation will either be S (split) or C (combine)
M indicates method, C indicates class, and V indicates variable
In the case of a split operation, the words will be a camel case method, class or variable name that you need to split into a space-delimited list of words starting with a lowercase letter.
In the case of a combine operation, the words will be a space-delimited list of words starting with lowercase letters that you need to combine into the appropriate camel case String. Methods should end with an empty set of parentheses to differentiate them from variable names.
Output Format

For each input line, your program should print either the space-delimited list of words (in the case of a split operation) or the appropriate camel case string (in the case of a combine operation).
Sample Input

S;M;plasticCup()

C;V;mobile phone

C;C;coffee machine

S;C;LargeSoftwareBook

C;M;white sheet of paper

S;V;pictureFrame

Sample Output

plastic cup

mobilePhone

CoffeeMachine

large software book

whiteSheetOfPaper()

picture frame

Explanation

Use Scanner to read in all information as if it were coming from the keyboard.

Print all information to the console using standard output (System.out.print() or System.out.println()).

Outputs must be exact (exact spaces and casing).

'''


def split_camel_case(camel_case_str, name_type):
    # Remove parentheses for methods before splitting
    if name_type == 'M' and camel_case_str.endswith('()'):
        camel_case_str = camel_case_str[:-2]
    
    result = []
    current_word = []
    
    # Traverse through the camel case string
    for char in camel_case_str:
        if char.isupper():
            # When encountering an uppercase letter, we split the word
            if current_word:
                result.append(''.join(current_word).lower())
            current_word = [char]  # Start a new word
        else:
            current_word.append(char)
    
    if current_word:
        result.append(''.join(current_word).lower())  # Append last word
    
    return ' '.join(result)

def combine_words(words_str, name_type):
    words = words_str.split()
    
    # Start with the first word in lowercase or capitalize if it's a class name
    if name_type == 'C':
        result = words[0].capitalize()
    else:
        result = words[0].lower()

    # Capitalize subsequent words for camel case
    for word in words[1:]:
        result += word.capitalize()

    # If it's a method name, add parentheses at the end
    if name_type == 'M':
        result += '()'

    return ''.join(result)

def process_input(line):
    parts = line.split(';')
    operation = parts[0]
    name_type = parts[1]
    input_string = parts[2]
    
    if operation == 'S':  # Split operation
        return split_camel_case(input_string, name_type)
    elif operation == 'C':  # Combine operation
        return combine_words(input_string, name_type)

def main():
    import sys
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        print(process_input(line))

if __name__ == "__main__":
    main()
