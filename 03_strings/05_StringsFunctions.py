text = "   Hello   world  "

#strings are immutable (any function does not change the original string)
text.strip()   # "Hello Python World"
text.lstrip()  # "Hello Python World  "
text.rstrip()  # "  Hello Python World"

print(text) # origial text variable is same 

print("data-engineer".replace("-", " ")) #replace function can be used on an replaced string
# "data engineer"

string = "apple,banana,mango"
# ['apple', 'banana', 'mango']
print(string.split(",") ) #converts into list


words = ["Python", "SQL", "Pandas"]
print(", ".join(words))
# 'Python, SQL, Pandas'

"HELLO WORLD".lower()       # 'hello world'
"hello world".upper()       # 'HELLO WORLD'
"hello world".title()       # 'Hello World'
"hello world".capitalize()  # 'Hello world'

filename = "sales.csv"
print(filename.endswith(".csv"))  # True

print("banana".count("a"))