def word_count(s):
    # Your code here

    inside = {}
    remove = [
    '"', 
    ':', 
    ';', 
    ',', 
    '.', 
    '-', 
    '+', 
    '=', 
    '/', 
    '\\', 
    '|', 
    '[', 
    ']', 
    '{', 
    '}', 
    '(', 
    ')', 
    '*', 
    '^', 
    '&']

    for key in remove:
        s = s.replace(key, "")

    split_arry = s.split()

    for word in split_arry:
        word = word.lower()

        if word in inside is not None:
            inside[word] = inside[word] + 1
        else:
            inside[word] = 1

    return inside   


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))