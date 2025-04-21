from textblob import TextBlob
import pandas as pd

# Load CSV
df = pd.read_csv("social_media_data.csv")

# Task 1 Goal: Analyze engagement (likes + retweets) and map to sentiment
# No sentiment analysis needed since it’s already provided!

# Calculate total engagement
df["Engagement"] = df["Likes"] + df["Retweets"]

# Save results
df.to_csv("results.csv", index=False)
print("Done! Check results.csv")