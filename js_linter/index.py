class Stack:
    def __init__(self):
        self.__data = []
    
    def push(self, brace: str):
        self.__data.append(brace)

    def pop(self):
        return self.__data.pop()

    def read(self):
        return self.__data[-1]
    
    def is_empty(self):
        return len(self.__data) == 0


class Linter:
    __OPENING_BRACES = ['{', '[', '(']
    __CLOSING_BRACES = ['}', ']', ')']
    
    def __init__(self):
        self.__stack = Stack()

    def lint(self, text):
        for char in text:
            if self.__is_opening_brace(char):
                self.__stack.push(char)

            if self.__is_closing_brace(char):
                if self.__stack.is_empty():
                    return f"{char}: Does not have an opening brace."

                top = self.__stack.pop()

                if not(self.__is_matching_brace(top, char)):
                    return f"{char}: Mismatched brace error."

        if not(self.__stack.is_empty()):
            top = self.__stack.pop()
            return f"{top}: Does not have a closing brace."

        return "Linting successful."


    def __is_matching_brace(self, opening, closing):
        matches = {'{': '}', '[': ']', '(': ')'}
        match = matches[opening]
        
        return closing == match


    def __is_opening_brace(self, char):
        return char in self.__OPENING_BRACES


    def __is_closing_brace(self, char):
        return char in self.__CLOSING_BRACES

my_linter = Linter()

my_file = "{[()]}"

print(my_linter.lint(my_file))


