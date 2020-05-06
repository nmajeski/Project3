# Final Project

## Group Members
Nick Majeski, Sineekarn (Aom) Watcharawikran, Maria Ugaz, Dyna Wilston, Rigo Aguado, Anne Marie Sticksel

## Testing Models for Sentiment Analysis

For this project, we will use Yelp reviews of coffee shops (specifically Chicago Starbucks locations) captured from the Yelp API.

With that data, we will test a variety of models to see which are most accurate, and we will train a model to analyze the sentiment of coffee shop reviews (or reviews in general) to tell if the review is overall positive (satisfied) or negative (unsatisfied) based on our chosen model.

Yelp API only allows you to pull the first 160 characters of a review and provides only the top 3 "most helpful" reviews per business. We pulled 868 reviews, but removed any 3-star review, which brought the count to 750 total reviews.

We did try feeding in additional data from other coffee shops (Dunkin Donuts) to increase the number of reviews to train and test with, but it did not make a difference in the overall result.

We are doing a binary sentiment analysis with "satisfied" and "unsatisfied" as the results, removing "neutral" because neutral reviews tended to add confusion to deciding whether a review was positive or negative overall.

We used TextBlob to measure polarity and subjectivity of words, and we used lists of positive and negative words to measure polarity again.

TextBlob defines Polarity and Subjectivity as follows:

**Polarity**: is a float value within the range [-1.0 to 1.0] where 0 indicates neutral, +1 indicates a very positive sentiment and -1 represents a very negative sentiment.

**Subjectivity**: is a float value within the range [0.0 to 1.0] where 0.0 is very objective and 1.0 is very subjective. Subjective sentence expresses some personal feelings, views, beliefs, opinions, allegations, desires, beliefs, suspicions, and speculations where as Objective sentences are factual. 


Using TextBlob's Naive Bayes classifier to receive a baseline accuracy score so that we could compare scores from four other models we used to train and test our data:

1. Logistic Regression
2. Tree
3. Random Forest
4. Nearest Neighbors

We created a Tableau story to contextualize the review information with a map of locations and summarizes the training/testing scores:
[See the Tableau story](https://public.tableau.com/profile/dyna.wilston#!/vizhome/FinalProjectSummary/Story1?publish=yes)


## Conclusion
Simpler models like Naive Bayes and Linear Regression did better in testing than the more complex models, but the more complex models did slightly better with the training data. All models did better than simply guessing.

Using the models we tested against, we can tell if text results in a "satisfied" or "unsatisfied" review with accuracy comparable to the pretrained Naive Bayes classiifer from TextBlob.

## Sources
* Positive and Negative Opinion Words

 Minqing Hu and Bing Liu. "Mining and Summarizing Customer Reviews." Proceedings of the ACM SIGKDD International Conference on Knowledge Discovery and Data Mining (KDD-2004), Aug 22-25, 2004, Seattle, Washington, USA.
 Retrieved from https://www.cs.uic.edu/~liub/FBS/sentiment-analysis.html#lexicon
* Yelp API
https://www.yelp.com/developers
* Textblob
https://textblob.readthedocs.io/en/dev/