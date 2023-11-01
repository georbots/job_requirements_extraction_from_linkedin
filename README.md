# Job requirements extraction from LinkedIn
Automatic collection of posted LinkedIn jobs appearing in a specific search, and extraction of the required skills based on all the job descriptions.

The actions performed in this project include:
* Automatic collection of each job title, company name and job description appearing in a specific LinkedIn job search,
* Data cleansing by removing jobs with irrelevant titles and jobs whose descriptions are not in english,
* Data processing and
* Visualization of the results in a wordcloud

The purpose of this project is to extract the most wanted skills by the market for a given job search.


## Installation

To install the required packages use the command:
```
pip install -r requirements.txt
```

ChromeDriver is also needed and can be downloaded [here](https://chromedriver.chromium.org/downloads).

### Data collection and cleansing
Based on a search url and by using selenium, all the results are aqcuired creating a list of job titles, company names and job links.
Using the list of job links job descriptions are then collected, for jobs that have a relevant to the search title. Jobs with descriptions not in english are also discarded.

### Data processing
The processing includes transforming text to lowercase, removing tabulation, panctuation, digits, stopwords from nltk.corpus and other custom stopwords which are irrelevant but are used a lot in job descriptions.

### Visualization
The results are visualized in a simple wordcloud to showcase the most required skills regarding a set of job descriptions.

For the search of machine learning engineer/ data scientist, the result is extracted from approximately 300 job descriptions and looks like this:
![wordcloud_results](https://user-images.githubusercontent.com/80923325/201470625-585af273-159a-402e-8abc-ff1715d63647.png)

  
