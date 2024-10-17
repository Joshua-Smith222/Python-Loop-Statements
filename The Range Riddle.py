# Task 1
import random
moods = ["happy", "sad", "calm", "agitated", "excited", "distracted", "angry", "loving", "unstoppable"]
days_of_the_week = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
for i in range(len(days_of_the_week)):
    mood = random.choice(moods)
    print(f"My mood: {days_of_the_week[i]}, was {mood}.")
