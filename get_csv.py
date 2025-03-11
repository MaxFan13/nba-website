import pandas as pd

# Read the CSV file
socialMedia = pd.read_csv("socialMedia.csv")

# Calculate average Likes per Platform and PostType
socialMediaAvg = socialMedia.groupby(["Platform", "PostType"])["Likes"].mean().reset_index()
socialMediaAvg = socialMediaAvg.rename(columns={"Likes": "AvgLikes"})
socialMediaAvg.to_csv("socialMediaAvg.csv", index=False)  # Save to CSV

# Calculate average Likes per Date
socialMediaTime = socialMedia.groupby("Date")["Likes"].mean().reset_index()
socialMediaTime = socialMediaTime.rename(columns={"Likes":"AvgLikes"})
socialMediaTime.to_csv("socialMediaTime.csv", index=False)  # Save to CSV
