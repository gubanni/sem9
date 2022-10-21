

def calc(number1, number2, operation): 
    if operation == '+':
        return number1+number2
    elif operation == '-':
        return number1-number2
    elif operation == '*':
        return number1*number2
    elif operation == '/':
        try:
            return number1/number2
        except ArithmeticError:
            return "Деление на 0"
    elif operation.lower() == 'mod':
        try:
            return number1%number2
        except ArithmeticError:
            return "Деление на 0"        
    elif operation.lower() == 'div':
        try:
            return number1//number2
        except ArithmeticError:
            return "Деление на 0" 
    elif operation.lower() == 'pow':
        return number1**number2
    else:
        return "Неизвестный оператор"