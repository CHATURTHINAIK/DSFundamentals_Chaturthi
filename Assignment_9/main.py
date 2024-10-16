import nltk
from nltk.tokenize import sent_tokenize
import matplotlib.pyplot as plt

nltk.download('punkt')

# Read the input reviews from input.txt
def read_reviews(filename):
    with open(filename, 'r') as file:
        reviews = file.readlines()
    return reviews

# Categorize reviews based on sentiment
def categorize_reviews(reviews):
    positive_reviews = []
    neutral_reviews = []
    negative_reviews = []

    for review in reviews:
        if '(positive)' in review:
            positive_reviews.append(review.replace('(positive)', '').strip())
        elif '(neutral)' in review:
            neutral_reviews.append(review.replace('(neutral)', '').strip())
        elif '(negative)' in review:
            negative_reviews.append(review.replace('(negative)', '').strip())

    return positive_reviews, neutral_reviews, negative_reviews

# Generate a summary by combining sentences from the reviews
def summarize_reviews(reviews):
    all_text = ' '.join(reviews) 
    sentences = sent_tokenize(all_text) 
    summary = ' '.join(sentences[:5]) 
    return summary

# Write summary to a file
def write_summary(filename, summary):
    with open(filename, 'w') as file:
        file.write(summary)

# Plot the counts using matplotlib
def plot_sentiment_counts(sentiment_counts):
    sentiments = list(sentiment_counts.keys())
    counts = list(sentiment_counts.values())

    plt.bar(sentiments, counts, color=['green', 'blue', 'red'])
    plt.xlabel('Sentiment')
    plt.ylabel('Count')
    plt.title('Sentiment Classification of Reviews')
    plt.show()

# Main function
def main():
    reviews = read_reviews('input.txt')

    # Categorize the reviews into positive, neutral, and negative lists
    positive_reviews, neutral_reviews, negative_reviews = categorize_reviews(reviews)

    # Summarize each category
    positive_summary = summarize_reviews(positive_reviews)
    neutral_summary = summarize_reviews(neutral_reviews)
    negative_summary = summarize_reviews(negative_reviews)

    # Write each summary to its respective file
    write_summary('positive_summary.txt', positive_summary)
    write_summary('neutral_summary.txt', neutral_summary)
    write_summary('negative_summary.txt', negative_summary)

    # Calculate sentiment counts
    sentiment_counts = {
        'Positive': len(positive_reviews),
        'Neutral': len(neutral_reviews),
        'Negative': len(negative_reviews)
    }

    # Plot sentiment counts
    plot_sentiment_counts(sentiment_counts)

    print("Summaries written to files and sentiment plot displayed successfully.")

main()