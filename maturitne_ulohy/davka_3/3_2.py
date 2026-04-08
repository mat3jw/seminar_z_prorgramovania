def is_balanced(expression):
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}
    
    for char in expression:
        if char in "([{":
            stack.append(char)
        elif char in ")]}":
            if not stack or stack.pop() != pairs[char]:
                return False
    return len(stack) == 0

# Testovacie prípady
test_cases = [
    "{[()]}", "{{[[(())]]}}", "{[(])}", "[[{{(())}}]]", 
    "{{[()]}]", "{{[()]}}}", "{{[([)]]}}", "{{[()]}}{}[]", 
    "{{[()]}}{[}", "{{[()]}}}{}[]"
]

for expr in test_cases:
    result = "OK" if is_balanced(expr) else "nesprávne"
    print(f"{expr:20} – {result}")
