# 1. Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
num = 'Thirty'
day = 'Days'
conector = 'Of'
language = 'Python'
space = ' '
sentence1 = num + space + day +  space + conector + space + language
print(sentence1)

# 2. Concatenate the string 'Coding', 'For', 'All' to a single string, 'Coding For All'.
coding = 'Coding'
for_ = 'For'
all_ = 'All'
sentence2 = coding + space + for_ + space + all_
print(sentence2)

# 3/4 Declare a variable named company and assign it to an initial value "Coding For All". and print it
company = "Coding For All"
print(company)

# 5. Print the length of the company string using len() method and print().
print(len(company))

# 6. Change all the characters to uppercase characters using upper() method. 
print(company.upper())

# 7. Change all the characters to lowercase characters using lower() method.
print(company.lower())

# 8. Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
print(company.capitalize())
print(company.title())
print(company.swapcase())

# 9. Cut(slice) out the first word of Coding For All string.
x = slice(7,15)
print(company[x])

first_word = company.split()[0]
print(first_word)

word = company.split()
word_1 = word[0]
print(word_1)

# 10. Check if Coding For All string contains a word Coding using the method index, find or other methods.