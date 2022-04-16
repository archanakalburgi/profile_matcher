import logging
from linkedin_jobs_scraper import LinkedinScraper
from linkedin_jobs_scraper.events import Events, EventData
from linkedin_jobs_scraper.query import Query, QueryOptions, QueryFilters
from linkedin_jobs_scraper.filters import RelevanceFilters, TimeFilters, TypeFilters, ExperienceLevelFilters, RemoteFilters
import csv
import pandas as pd

'''
change 
slow_mo=3(increase it)
limit=3500
'''

# Change root logger level (default is WARN)
logging.basicConfig(level = logging.INFO)

linked_data = []
def on_data(data: EventData):
    linked_data.append([data.title, data.job_function, data.location,data.date, data.link ,data.apply_link, data.description, data.seniority_level])


def on_error(error):
    print('[ON_ERROR]', error)


def on_end():
    columns = ['title', 'company', 'location', 'date', 'link', 'apply_link', 'description', 'seniority_level']
    df = pd.DataFrame(linked_data, columns=columns)
    df.to_csv('linkedin_jobs.csv', index=False, encoding='utf-8')
    print('[ON_END]')


scraper = LinkedinScraper(
    chrome_executable_path="/Users/archanakalburgi/Downloads/project_660/chromedriver", # Custom Chrome executable path (e.g. /foo/bar/bin/chromedriver) 
    chrome_options=None,  # Custom Chrome options here
    headless=True,  # Overrides headless mode only if chrome_options is None
    max_workers=1,  # How many threads will be spawned to run queries concurrently (one Chrome driver for each thread)
    slow_mo=2,  # Slow down the scraper to avoid 'Too many requests (429)' errors
)

# Add event listeners. call back
scraper.on(Events.DATA, on_data)
scraper.on(Events.ERROR, on_error)
scraper.on(Events.END, on_end)

# tasks
queries = [
    # Query(
    #     options=QueryOptions(
    #         optimize=True,  # Blocks requests for resources like images and stylesheet
    #         limit=100  # Limit the number of jobs to scrape
    #     )
    # ),
    Query(
        query='Engineer',
        options=QueryOptions(
            locations=['United States'],
            optimize=True,
            limit=100,
            filters=QueryFilters(
                # company_jobs_url='https://www.linkedin.com/jobs/search/?f_C=1441%2C17876832%2C791962%2C2374003%2C18950635%2C16140%2C10440912&geoId=92000000',  # Filter by companies
                relevance=RelevanceFilters.RECENT,
                time=TimeFilters.ANY,
                type=[TypeFilters.INTERNSHIP],
                experience=None,                
            )
        )
    )
]

scraper.run(queries)
