# One day you decide to arrange all your cats in a giant circle.
# Initially, none of your cats have any hats on.
# You walk around the circle 100 times, always starting at the same spot,
# with the first cat (cat # 1).
# Every time you stop at a cat,
# you either put a hat on it if it doesn’t have one on,
# or you take its hat off if it has one on.
#
# In The first round, you stop at every cat, placing a hat on each one.
# In The second round, you only stop at every second cat
# (#2, #4, #6, #8, etc.).
# In The third round, you only stop at every third cat
# (#3, #6, #9, #12, etc.).
# You continue this process until you’ve made 100 rounds around the cats
# (e.g., you only visit the 100th cat).
#
# Write a program that simply outputs which cats have hats at the end.
# Optional:
# Make a function that can calculate hats with any amount of rounds and cats.

def put_hats_on_cats(cats_amount: int = 100) -> list:
    cats_with_hats = []
    x = 1
    while x ** 2 <= cats_amount:
        cats_with_hats.append(x ** 2)
        x += 1
    return cats_with_hats


print(put_hats_on_cats())
