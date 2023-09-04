from collections import Counter
str = "Django is a free and open-source web framework written in Python.It follows the model-template-view architectural pattern and is used for building web applications with complex, database-driven functionality.Some of its notable features include a built-in administrative interface, an ORM (Object-Relational Mapping) system, and support for a wide variety of databases.It also encourages reusable and maintainable code, making it a popular choice for web developers."
w = str.split(" ")
print(w)
wc=Counter(w).most_common()
print(wc)
print("Most frequent word in the given sentence is :" +wc[0][0] +"\n frequnce :",wc[0][1])