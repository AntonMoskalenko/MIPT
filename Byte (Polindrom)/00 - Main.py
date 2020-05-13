def main():
    something = input('Enter text: ')

    if is_palindrom(simplify_text(something)):
        print('Yes, it is a polindrom')
    else:
        print('No, it is not a polindrom')


def reverse(text):
    return text[::-1]


def simplify_text(text):
    i = 0
    replacement = []
    text = text.lower()
    for i in range(len(text)):
        if ord(text[i]) in range(65, 90) or ord(text[i]) in range(97, 122):
            pass
        else:
            replacement.append(text[i])
        i += 1

    for symbol in replacement:
        text = text.replace(symbol, '')

    return text


def is_palindrom(text):
    return text == reverse(text)


main()