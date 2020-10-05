the_list = [
    143266561,
    1738152473,
    312377936,
    1027708881,
    1495785517,
    1858250798,
    1693786723,
    1871655963,
    374455497,
    430158267,
]


theBiggest = the_list[0]

for i in range(len(the_list)):
    if theBiggest > the_list[i]:
        continue
    else:
        theBiggest = the_list[i]

print(theBiggest)