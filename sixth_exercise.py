tweet = input("Enter a tweet: ")
lenght_count = len(tweet)
if lenght_count < 140:
    print(f"that tweet is {lenght_count} characters long")
else:
    print(f"your {lenght_count} char tweet is {lenght_count-140} chars too long")