# word = "mississippi"
# # counter = {}

# # for letter in word:
# #     if letter not in counter:
# #         counter[letter] = 0
# #     counter[letter] += 1

# # print(counter)





# # from collections import defaultdict
# # counter = defaultdict(int)

# # for letter in word:
# #     counter[letter] += 1

# # print(counter)



# from collections import Counter
# # # print(list(word))
# # print(Counter("mississippi"))


# # inventory = Counter(
# #     apple=10
# #     ,orange=15
# #     ,banana=0
# #     ,tomato=-15
# # )
# # print(inventory)


# letters = Counter({"i": 4, "s": 4, "p": 2, "m": 1})
# letters.update("missouri")
# print(letters)
# print(letters['i'])
# print(letters.most_common(1))
# print(letters.most_common(2))
# print(letters.most_common(3))
# print(letters.most_common(3)[::-1])
# print(letters.most_common(3)[:-3:-1])




# from collections import Counter

# def count_letters(filename):
#     letter_counter = Counter()
#     with open(filename) as file:
#         for line in file:
#             line_letters = [
#                 char for char in line.lower() if char.isalpha()
#             ]
#             letter_counter.update(Counter(line_letters))

#     return letter_counter

# letter_counter = count_letters("pyzen.txt")
# print(letter_counter)



from collections import Counter

def print_ascii_bar_chart(data, symbol="#"):
    counter = Counter(data).most_common()
    chart = {category: symbol * frequency for category, frequency in counter}
    max_len = max(len(category) for category in chart)
    for category, frequency in chart.items():
        padding = (max_len - len(category)) * " "
        print(f"{category}{padding} |{frequency}")

sales = Counter(banana=15, tomato=4, apple=39, orange=30)

print_ascii_bar_chart(sales, symbol="+")