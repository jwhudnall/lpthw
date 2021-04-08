# Word Choice Game

# Pseudocode
from sys import exit


score = 0
# Wake up in the morning: 2 choices
# 1. Exercise
# 2. Snooze
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

# At work, 5 minutes before a big meeting. Coworker asks for help. 2 choices:
# 1. Help them
# 2. Tell them you have a meeting to attend.
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

# If you help them, gain 1 point. Coworker tells your boss how much you helped. Good Meeting.
# If you don't help, lose 1 point. Upset coworker leads into bad meeting.

# *Decision* #
# Work day ending, and boss asks you to stay late. You know your spouse is at home with your young child and is expecting you.

# 1. Stay at work. lose 1 point. Miss baby's first steps.
# 2. Go home. Gain 1 point. Boss isn't thrilled, but you convince them you have a spouse and child at home that need your support
#, so they respect your decision.

# Score Evaluation Function
# 3 points: On track for a balanced life
# 1 point: Could improve things.
# -1 point: Likely not happy
# -3 points: Should consider reprioritizing things.

def display_score():
    print(f"Your current score is: {score}")

def main():
    wakeup()
    display_score()
    meeting_choice()
    display_score()

main()
