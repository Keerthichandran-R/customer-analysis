
import pandas as pd

# Load the customer feedback data
df = pd.read_csv("customer_feedback.csv")

# Display basic statistics
print("Average Rating:", df['Rating'].mean())

# Find most common sentiment
print("Most common sentiment:", df['Sentiment'].mode()[0])

# Count of feedbacks per sentiment type
sentiment_counts = df['Sentiment'].value_counts()
print("\nSentiment Distribution:")
print(sentiment_counts)

# Filter negative feedbacks
negative_feedbacks = df[df['Sentiment'] == 'Negative']
print("\nSample Negative Feedbacks:")
print(negative_feedbacks[['CustomerID', 'Feedback']].head())
