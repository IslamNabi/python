class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.current_token = None
        self.token_index = 0

    def next_token(self):
        # Move to the next token in the list
        if self.token_index < len(self.tokens):
            self.current_token = self.tokens[self.token_index]
            self.token_index += 1
        else:
            # If we reach the end of the list, set current_token to None
            self.current_token = None

    def parse(self):
        # Start parsing by initializing the current token
        self.next_token()
        # Begin parsing an expression
        tree = self.expression()
        # If there are tokens remaining, it means the expression was not fully parsed
        if self.current_token is not None:
            raise SyntaxError("Unexpected token")
        return tree

    def expression(self):
        # Parse a term
        node = self.term()
        # Keep parsing terms separated by '+' or '-' operators
        while self.current_token in ('+', '-'):
            op = self.current_token
            # Move to the next token
            self.next_token()
            # Parse the next term
            node = Node(op, node, self.term())
        return node

    def term(self):
        # Parse a factor
        node = self.factor()
        # Keep parsing factors separated by '*' or '/' operators
        while self.current_token in ('*', '/'):
            op = self.current_token
            # Move to the next token
            self.next_token()
            # Parse the next factor
            node = Node(op, node, self.factor())
        return node

    def factor(self):
        # Check if the current token is a number
        if self.current_token.isdigit():
            # If it's a number, create a leaf node with the number value
            node = Node(self.current_token)
            # Move to the next token
            self.next_token()
            return node
        elif self.current_token == '(':
            # If it's an opening parenthesis, parse an expression within parentheses
            self.next_token()
            node = self.expression()
            # Check if the expression is followed by a closing parenthesis
            if self.current_token != ')':
                raise SyntaxError("Expected closing parenthesis")
            # Move to the next token
            self.next_token()
            return node
        else:
            # If it's neither a number nor an opening parenthesis, it's an invalid token
            raise SyntaxError("Invalid token")

def print_tree(node, indent=0):
    # Print the value of the current node with indentation
    print(" " * indent + str(node.value))
    # If there is a left child, recursively print the left subtree with increased indentation
    if node.left:
        print_tree(node.left, indent + 4)
    # If there is a right child, recursively print the right subtree with increased indentation
    if node.right:
        print_tree(node.right, indent + 4)

# Example usage
tokens = ['(', '3', '+', '4', ')', '*', '5']
parser = Parser(tokens)
tree = parser.parse()
print("Syntax tree:")
print_tree(tree)
