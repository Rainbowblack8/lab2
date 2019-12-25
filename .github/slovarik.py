kal= '''!()-[]{};:'"\,<>./?@#$%^&*_~1234567890'''
s = input("Enter your text:")
choice = input('Enter your choice(1,2):')
if choice == "1":
    d = {}
    for i in s:
        if i.isalpha():
            d[i] = d.get(i, 0) + 1

    for i in d:
        print(i, "=", d[i])
elif choice == "2":
    no_s=""
    for letter in s:
        if letter not in kal:
            no_s = no_s+ letter
    no_s=no_s.split()
    no_s.sort()
    print("Sorted:")
    for word in no_s:
        if len(word) > 3:
            print(word)
else:
    print("Wrong choice")
