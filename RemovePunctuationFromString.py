punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

string = input("Enter a string :")
no_punctuation = ""
for char in string:
    if char not in punctuations:
        no_punctuation = no_punctuation + char
print(no_punctuation)