import pandas as pd
from nltk.corpus import stopwords
from textblob import Word
from custom_stop_words import other_stop_words


data = pd.read_csv(r'C:\Users\JARVIS\Desktop\linkedin_scraper\data\downloaded_jobs_with_details_new_example.csv', dtype=str).fillna('bye')
data = data.reset_index()  # make sure indexes pair with number of rows


# lower case
data['job_descriptions'] = data['job_descriptions'].apply(lambda x: " ".join(x.lower()for x in x.split()))
# remove tabulation and punctuation
data['job_descriptions'] = data['job_descriptions'].str.replace('[^\w\s]',' ')
# digits
data['job_descriptions'] = data['job_descriptions'].str.replace('\d+', '')
# remove custom stopwords
data['job_descriptions'] = data['job_descriptions'].apply(lambda x: " ".join(x for x in x.split() if x not in other_stop_words))
# remove stop words
stop = stopwords.words('english')
data['job_descriptions'] = data['job_descriptions'].apply(lambda x: " ".join(x for x in x.split() if x not in stop))
# lemmatization
data['job_descriptions'] = data['job_descriptions'].apply(lambda x: " ".join([Word(word).lemmatize() for word in x.split()]))

print("Preprocessed data: \n")
print(data['job_descriptions'])

data.to_csv(r'C:\Users\JARVIS\Desktop\linkedin_scraper\data\jobs_with_details_omg_new_example.csv')

