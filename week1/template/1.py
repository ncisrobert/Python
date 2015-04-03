for word in stopwords:
    next = word.strip()
    print(next)

while True:
    input = raw_input("Say something interesting: ")
    filtered = input.replace(" ni ", " <beep> ")
    print("Your filtered text was: " + filtered)
