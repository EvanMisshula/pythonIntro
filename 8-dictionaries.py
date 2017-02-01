## Dictionaries

empty_dict = {}
empty_dict2 = dict()
grades = { "Joel" : 80, "Tim" : 95 }

joels_grade = grades["Joel"]

try:
    kates_grade = grades["Kate"]
except KeyError:
    print "no grade for Kate!"

joel_has_grade = "Joel" in grades
kate_has_grade = "Kate" in grades

## default values
joels_grade = grades.get("Joel", 0)
kates_grade = grades.get("Kate", 0)
no_ones_grade = grades.get("No One")

grades["Tim"] = 99
grades["Kate"] = 100
num_students = len(grades)
print num_students 

#nested structure
tweet = {
    "user" : "joelgrus",
    "text" : "Data Science is Awesome",
    "retweet_count" : 100,
    "hashtags" : ["#data", "#science", "#datascience", "#awesome", "#yolo"]
}

print tweet

tweet_keys = tweet.keys()
tweet_values = tweet.values()
tweet_items = tweet.items()

print tweet_keys
print tweet_values
print tweet_items

print "user" in tweet_keys #slow
print "user" in tweet      #fast
print "joelgrus" in tweet_values

word_counts = {}
for word in document:
    previous_count = word_counts.get(word, 0)
    word_counts[word] = previous_count + 1

#adds a key when key lookup fails with count of 0
from collections import defaultdict
word_counts = defaultdict(int)
for word in document:
    word_counts[word] += 1

## Counter
from collections import Counter
c = Counter([0, 1, 2, 0])
print c

# print the 10 most common words and their counts
for word, count in word_counts.most_common(10):
    print word, count
