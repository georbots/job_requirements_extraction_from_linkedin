import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud


data = pd.read_csv(r'C:\Users\JARVIS\Desktop\linkedin_scraper\data\downloaded_jobs_with_details_new_example.csv', dtype=str).fillna('bye')
data = data.reset_index()  # make sure indexes pair with number of rows


# Create and generate a word cloud image:
wordcloud = WordCloud(width=800, height=400).generate(' '.join(data['job_descriptions']))
print("\n***********\n")
#
plt.figure(figsize=(20, 10))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.savefig('wordcloud_results.png')

plt.show()

