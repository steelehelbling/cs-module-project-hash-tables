
remove_list = '";:,.-+=/|\[]{}()*^&'

with open("robin.txt") as f:
    read_file = f.read().strip().split()


inside = {}

for word in read_file:

    cleaned_word = word.strip(remove_list).lower()

    if cleaned_word not in inside:
        inside[cleaned_word] = 1

    else:
        inside[cleaned_word] += 1

amount_sort = sorted(
    inside.items(), key=lambda item: item[1], reverse=True)
highest_of_list = len(sorted(inside.keys(), key=lambda x: len(x))[-1])

for i, n in amount_sort:
    amount = ' ' * (highest_of_list - len(i)) + n * '#'
    print(f"{i}  {amount}")