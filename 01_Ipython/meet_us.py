def divide_name(name):
    return "|".join(list(name))

for name in ["John", "Mike", "Emily"]:
    print(f"Hello {divide_name(name)}!")
