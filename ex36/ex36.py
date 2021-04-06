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

# If you Exercise, gain 1 point. On time to work.
# If you snooze, lose 1 point. Late to work.

# At work, 5 minutes before a big meeting. Coworker asks for help. 2 choices:
# 1. Help them
# 2. Tell them you have a meeting to attend.

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

def main():
    wakeup()

main()
print(f"Your score was: {score}")