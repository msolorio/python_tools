import sys

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
        
    
    def lint(self, text_str: str):
        lines = text_str.split('\n')
        
        for idx, line in enumerate(lines):
            line_num = idx + 1
            result = self.__lint_line(line, line_num)

            if result["status"] == "Error":
                return result["message"]


        if not(self.__stack.is_empty()):
            char = self.__stack.pop()
            return f"Does not have a closing brace: {char}."

        return "Linting successful."


    def __lint_line(self, line: str, line_num: int):
        for char in line:
            if self.__is_opening_brace(char):
                self.__stack.push(char)

            if self.__is_closing_brace(char):
                if self.__stack.is_empty():
                    return {
                        "status": "Error", 
                        "message": f"Line: {line_num}. Does not have an opening brace: {char}."
                    }

                top = self.__stack.pop()

                if not(self.__is_matching_brace(top, char)):
                    return {
                        "status": "Error",
                        "message": f"Line: {line_num}. Mismatched brace error: {char}." 
                    }

        return { "status": "Success" }


    def __is_matching_brace(self, opening: str, closing: str):
        matches = {'{': '}', '[': ']', '(': ')'}
        match = matches[opening]
        
        return closing == match


    def __is_opening_brace(self, char: str):
        return char in self.__OPENING_BRACES


    def __is_closing_brace(self, char: str):
        return char in self.__CLOSING_BRACES


class File:
    def get_text_str(self, filepath: str):
        return open(filepath, 'r').read()


def main():
    linter = Linter()
    filepath = sys.argv[1]
    text_str = File().get_text_str(filepath)

    result = linter.lint(text_str)

    print(result)


main()
