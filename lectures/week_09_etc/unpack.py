# # https://cs50.harvard.edu/python/2022/notes/9/#unpacking


# def total(galleons, sickles, knuts):
#     return (galleons * 17 + sickles) * 29 + knuts


# # print(total(100, 50, 25), "Knuts") # 50775 Knuts

# # coins = [100, 50, 25]
# # print(total(coins[0], coins[1], coins[2]), "Knuts")  # 50775 Knuts

# # coins = [100, 50, 25]
# # print(total(*coins), "Knuts")  # 50775 Knuts

# # coins = {"galleons": 100, "sickles": 50, "knuts": 25}
# # print(total(coins["galleons"], coins["sickles"], coins["knuts"]), "Knuts")
# # Notice how a dictionary called coins is provided. We can index into it using keys, such as “galleons” or “sickles”.

# coins = {"galleons": 100, "sickles": 50, "knuts": 25}
# print(total(**coins), "Knuts")
# # Notice how ** allows you to unpack a dictionary. When unpacking a dictionary, it provides both the keys and values.


# # https://cs50.harvard.edu/python/2022/notes/9/#args-and-kwargs
# def f(*args, **kwargs):
#     print("Named:", kwargs)


# f(galleons=100, sickles=50, knuts=25)
