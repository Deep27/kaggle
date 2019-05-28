print(bool(1))
print(bool(0))
print(bool("abc"))
print(bool(""))
print(bool([1, 2, 3]))
print(bool([]))

if 0:
    print(0)
elif "spam":
    print("spam")


def quiz_message(grade):
    if grade < 50:
        outcome = 'failed'
    else:
        outcome = 'passed'
    print('You', outcome, 'the quiz with a grade of', grade)


quiz_message(80)


def quiz_message_tern(grade):
    outcome = 'failed' if grade < 50 else 'passed'
    print('You', outcome, 'the quiz with a grade of', grade)


quiz_message_tern(45)
