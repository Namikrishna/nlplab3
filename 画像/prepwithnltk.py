import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer

# Download required resources (only once)
nltk.download('punkt_tab')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('omw-1.4')  # For lemmatizer

# Sample text
text = "Natural Language Processing with NLTK includes tokenizing, stemming, removing stopwords, and lemmatization."

# 1. Tokenization
tokens = word_tokenize(text)
print("1️⃣ Tokens:", tokens)

# 2. Stopword Removal
stop_words = set(stopwords.words('english'))
filtered_tokens = [word for word in tokens if word.lower() not in stop_words]
print("2️⃣ After Stopword Removal:", filtered_tokens)

# 3. Stemming
stemmer = PorterStemmer()
stemmed_words = [stemmer.stem(word) for word in filtered_tokens]
print("3️⃣ After Stemming:", stemmed_words)

# 4. Lemmatization
lemmatizer = WordNetLemmatizer()
lemmatized_words = [lemmatizer.lemmatize(word) for word in filtered_tokens]
print("4️⃣ After Lemmatization:", lemmatized_words)
