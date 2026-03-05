# string2_func.py
# 1. split
# 2. strip
# 3. join


my_string = "Python is a popular programming language"
split_list = my_string.split()
print(split_list)
print(split_list[-1])

my_string = "Python is a popular programming language"
split_list = my_string.split(" ")
print(split_list)
print(split_list[-1])

# =============================================================
my_string = "       Python is Awesome!"
print(my_string.strip())

# =============================================================
# 문자열.join(리스트)
my_list = ['apple', 'banna', 'cherry']
joined_string = "-".join(my_list)
print(joined_string)
joined_string = "".join(my_list)
print(joined_string)
joined_string = "\n".join(my_list)
print(joined_string)



