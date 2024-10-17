import random
moods = ["happy", "sad", "calm", "agitated", "excited", "distracted", "angry", "loving", "unstoppable"]
days_of_the_week = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
time_of_day = ["morning", "afternoon", "evening"]
for days in days_of_the_week:
    for time in time_of_day:
        mood = random.choice(moods)
        print(f"My mood: {days} at {time} was {mood}.")
