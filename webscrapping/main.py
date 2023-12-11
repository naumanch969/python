from bs4 import BeautifulSoup
import time
import requests

print('Put some skill that you are not familiar with')
# unfamiliar_skill = input('>')
# print(f'Filtering out {unfamiliar_skill}')

def find_jobs():
    html_text = requests.get('https://www.upwork.com/nx/find-work/best-matches').text
    soup = BeautifulSoup(html_text, 'lxml')
    print(soup.prettify())
    jobs = soup.find('div', class_ = 'air3-grid-container mb-4x gap-0')
    # print(jobs)
    # for index,job in enumerate(jobs):
        # published_date = job.find('span', class_ = 'sim-posted').span.text.replace(' ', '')
        # if 'few' in published_date:
        #     company_name = job.find('h3', class_ = 'joblist-comp-name').text
        #     skills = job.find('span', class_ = 'srp-skills').text.replace(' ', '')
        #     more_info = job.header.h2.a['href']
        #     if unfamiliar_skill not in skills:
        #         with open(f'posts/{index}.txt', 'w') as file:
        #             file.write(f"Company Name: {company_name.strip()} \n")
        #             file.write(f"Required Skills: {skills.strip()} \n")
        #             file.write(f"More Info: {more_info} \n")
        #             file.write(f"Published Date: {published_date} \n")
        #         print(f'File Saved: {index}.txt')                    

if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 0.5
        print(f"Waiting {time_wait}  minutes...")
        time.sleep(time_wait * 60)