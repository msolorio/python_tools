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


class Brace:
    def __init__(self, char, line_num):
        self.char = char
        self.line_num = line_num


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
            brace = self.__stack.pop()
            return f"Error: Missing closing brace: '{brace.char}'. Line: {brace.line_num}."

        return "Linting successful."


    def __lint_line(self, line: str, line_num: int):
        for char in line:
            if self.__is_opening_brace(char):
                brace = Brace(char, line_num)
                
                self.__stack.push(brace)

            if self.__is_closing_brace(char):
                if self.__stack.is_empty():
                    return {
                        "status": "Error", 
                        "message": f"Error: Missing opening brace: '{char}'. Line: {line_num}."
                    }

                top = self.__stack.pop()

                if not(self.__is_matching_brace(top.char, char)):
                    return {
                        "status": "Error",
                        "message": f"Error: Mismatched brace error: \n- Found '{char}'. Line: {line_num}. \n- Expected: '{top.char}'. Line: {top.line_num}." 
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

if __name__ == "__main__":
    main()
