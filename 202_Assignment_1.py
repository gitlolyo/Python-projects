# 1. Please complete the following:
#   Your First name and Last Name: Siwon Lee
#   Your Student ID: 261279717


# 2. Write your program here:

# Constants
MIN_RESP = 2
MAX_RESP = 5
SECS_IN_MIN = 60
RESP_THRESHOLD = 9
MAX_WPM = 66
BOT_TYPO = 0
HUMAN_TYPO = 3

print("Bot or Human? Let's figure this out!")

# Prompting user to enter an hour of the day (float)
response_time = float(input("When did you receive the response "
                           "(type a float between 0 and 24)? "))

# If the response time is between 2 and 5 am (inclusive), the message came
# from a bot.
if MIN_RESP <= response_time <= MAX_RESP:
    print("You just talked to a bot")
else:
    user_answer_in_minutes = float(input("How long did it take to get your "
                                      "response (in min)? "))

    # Converting user's answer to seconds
    user_answer_seconds = user_answer_in_minutes * SECS_IN_MIN

    # If the response time (in seconds) < 9, the message came from a bot.
    if user_answer_seconds < RESP_THRESHOLD:
        print("You just talked to a bot")
    else:
        total_words = int(input("How many words in your response? "))

        # Using words_total to user_answer_minutes to find wpm
        words_per_minute = float(total_words / user_answer_in_minutes)

        # If the number of words per minute is less than 66, the message came
        # from a human.
        if words_per_minute < MAX_WPM:
            print("You just talked to a fellow human")
        else:
            total_typos = int(input("How many typos in the response ("
                                    "grammatical errors, misspelled words, "
                                    "etc.)? "))

            # If the number of typos is greater than 0, the message came
            # from a human.
            if total_typos > BOT_TYPO:
                print("You just talked to a fellow human")
            else:
                total_t = int(input("Ask the responder how many 't' there are"
                                   "in 'eeooeotetto' and type their answer: "))

                # If they guess right (3), then they are a human.
                if total_t == HUMAN_TYPO:
                    print("You just talked to a fellow human")
                else:
                    print("You just talked to a bot")

