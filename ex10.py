tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line"
backslash_cat = "I'm \\ a \\ cat."

fat_cat = '''
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
'''

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)

thin_cat = "I'll do a list:\n\t* Cat food\n\t* Fishies\n\t* Catnip\n\t* Grass"

print(thin_cat)

newline = "\n"
fruit1 = "Mango"
fruit2 = "Papaya"

formatter = "{} {} {}"

print(formatter.format(fruit1,newline,fruit2))
