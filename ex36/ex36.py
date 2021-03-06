score = 0

def wakeup():
    global score
    print("You wake up to your alarm. You have 1 hour before you need to leave for work. Do you get up and exercise, or snooze?")

    decision = input("> ")

    if "exerci" in decision:
        score += 1
        print("You have a great workout and arrive at work with time to spare, ready to take on your day")
    elif "snooze" in decision or "sleep" in decision:
        score -= 1
        print("You snooze your alarm and oversleep. You're late to work, stressed")
    else:
        print("Please choose between \"Exercising\" and \"Snoozing\"")
        wakeup()
    meeting_choice()


def meeting_choice():
    global score
    print("You're at work and you have 5 minutes until a big meeting.")
    print("A co-worker comes by and asks for some help.")
    print("Do you: 1) Help them out, or 2) Head to your meeting?")
    decision = input("> ")

    if "help" in decision:
        score += 1
        print("You help your co-worker, who tells your boss about it. You're late to the meeting, but everyone commends your helping a co-worker")
    elif "head" in decision or "meet" in decision:
        score -= 1
        print("You are on time to your meeting, but your upset co-worker makes you look bad in the meeting.")
    else:
        print("Invalid choice.")
        meeting_choice()
    end_of_day()


def end_of_day():
    global score
    print("The work day is about to end, and your boss asks if you can stay to help work on a big project.")
    print("You know your spouse is at home with your young child and is expecting you.")
    print("Do you: 1) Stay at work, or 2) Go home")

    decision = input("> ")
    if "stay" in decision or "work" in decision:
        score -= 1
        print("Your boss is happy, but when you get home, you realize you missed your child's first steps. Your wife is upset")
    elif "home" in decision or "leave" in decision:
        score += 1
        print("Your boss isn't thrilled, but understands you have a young child at home. You get home in time to see your child's first steps!")
    else:
        print("Invalid choice.")
        end_of_day()
    dinner()

# You go home to see what your spouse has made for dinner, or do you pick up dinner on the way home

def dinner():
    global score
    print("You get home and see that your spouse is getting ready to cook dinner.")
    print("You also have a big presentation at work tomorrow that you haven't prepared for.")
    print("Do you 1) Work on your work presentation, or 2) Help out with dinner?")

    decision = input("> ")
    if "work" in decision or "presentation" in decision:
        score -= 1
        print("You manage to prepare for work, but you can tell your spouse is stressed and exhausted at dinner. They seem distant, and you regret your decision.")
    elif "help" in decision or "dinner" in decision:
        score += 1
        print("You and your spouse have a great time fixing dinner together. You feel refreshed and confident you'll nail the work presentation.")
    else:
        print("Invalid choice.")
        dinner()

def display_score():
    print("*" * 20)
    print(f"Your current score is: {score}")
    print("*" * 20)

# Possible Scores:
# * All +1: 4
# * All -1: -4
# -4, 4

def final_score():
    global score
    if score == 4:
        print(f"You scored {score} points. Perfect score!")
    elif score > 0:
        print(f"You scored {score} points. Overall, your day was positive.")
    elif score == -4:
        print(f"You scored {score} points. You may consider reconsidering a few things in order to live a long, lasting and enjoyable life.")
    else:
        print(f"You scored {score} points. You could do better, but you could also do worse!")

def main():
    wakeup()
    final_score()

main()