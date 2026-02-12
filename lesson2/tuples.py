from numpy.ma.core import empty

word = ("spam", "eggs", "mouse")

print(word[0])

empty_tuple = ()
print(empty_tuple)

person = ("Anid", 16 , "Engineer")

name, age, profession = person

print(name, "'s", "profession is, ", profession, "and he is", age, "years old")