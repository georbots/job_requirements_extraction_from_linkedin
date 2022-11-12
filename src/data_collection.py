from selenium import webdriver
import time
import pandas as pd
import csv
import bs4
import requests


from langdetect import detect
from selenium.webdriver.common.by import By


def get_company_names(n, driver):
    company_name = []
    try:
        for i in range(n):
            company = driver.find_elements_by_class_name('base-search-card__subtitle')[i].text
            company_name.append(company)
    except IndexError:
        print("Index Error")
    company_final = pd.DataFrame(company_name, columns=["company"])
    return company_final


def get_job_titles(n, driver):
    titlename = []
    try:
        for i in range(n):
            title = driver.find_elements_by_class_name('base-search-card__title')[i].text

            titlename.append(title)
    except IndexError:
        print("Index Error")
    titlefinal = pd.DataFrame(titlename, columns=["title"])
    return titlefinal


def get_job_links(driver):
    joblist = driver.find_elements_by_class_name('base-card__full-link')
    hreflist = []
    for e in joblist:
        hreflist.append(e.get_attribute('href'))

    linklist = pd.DataFrame(hreflist, columns=["joblinks"])
    return linklist


def open_page_and_scroll_to_bottom():
    url = 'https://www.linkedin.com/jobs/search?keywords=Machine%20Learning%20Engineer&location=European%20Union&geo' \
                'Id=91000000&f_E=2%2C3%2C4%2C5&f_JT=F&position=2&pageNum=0&currentJobId=3309397601'
    driver = webdriver.Chrome(r'C:\Users\JARVIS\Desktop\linkedin_scraper\chromedriver.exe')
    driver.implicitly_wait(10)
    driver.get(url)

    y = driver.find_elements(by=By.CLASS_NAME, value='results-context-header__job-count')[0].text
    n = pd.to_numeric(y)

    i = 2
    while i <= int((n + 200) / 25) + 1:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        i = i + 1

        try:
            send = driver.find_element_by_xpath("//button[@aria-label='Load more results']")
            driver.execute_script("arguments[0].click();", send)
            time.sleep(2)
        except:
            pass
            time.sleep(5)

    return n, driver


def filter_out_irrelevant_jobs_by_title():
    with open(r'C:\Users\JARVIS\Desktop\linkedin_scraper\data\linkedin_new_example.csv', newline='') as f:
        reader = csv.reader(f)
        data = list(reader)

    keywords = ['Data', 'ML', 'AI', 'Machine Learning']
    cleansed_list = []
    for i in data:
        if any(substring in i[2] for substring in keywords):
            cleansed_list.append(i)

    cleansed_list = pd.DataFrame(cleansed_list, columns=['', 'company', 'title', 'joblinks'])
    cleansed_list.to_csv(r'C:\Users\JARVIS\Desktop\linkedin_scraper\data\cleansed_jobs_new_example.csv', index=False)


def download_job_descriptions():
    with open(r'C:\Users\JARVIS\Desktop\linkedin_scraper\data\cleansed_jobs_new_example.csv', newline='') as f:
        reader = csv.reader(f)
        data = list(reader)

    for case in data:
        print("Getting description of case", case[0])
        result = requests.get(case[3])
        soup = bs4.BeautifulSoup(result.text, 'html.parser')
        result = soup.find_all("div",
                               {"class": "show-more-less-html__markup show-more-less-html__markup--clamp-after-5"})

        job_details = []
        for div in result:
            job_details.append(div.text)

        job_description = " ".join(job_details)

        case[3] = job_description
        time.sleep(3)

    data = pd.DataFrame(data, columns=['', 'company', 'title', 'job_descriptions'])

    data = data.reset_index()  # make sure indexes pair with number of rows

    # exclude cases not in english
    for index, row in data.iterrows():
        print(index, row['job_descriptions'])
        if detect(row['job_descriptions']) != 'en':
            data.drop(index, inplace=True)

    data.to_csv(r'C:\Users\JARVIS\Desktop\linkedin_scraper\data\downloaded_jobs_with_details_new_example.csv', index=False)


if __name__ == "__main__":
    num, webdriver = open_page_and_scroll_to_bottom()

    x = get_company_names(num, webdriver).join(get_job_titles(num, webdriver)).join(get_job_links(webdriver))
    x.to_csv(r'C:\Users\JARVIS\Desktop\linkedin_scraper\data\linkedin_new_example.csv')

    filter_out_irrelevant_jobs_by_title()

    download_job_descriptions()

    webdriver.close()

