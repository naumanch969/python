import requests
import schedule
import time

mobile_number =+23055712534

def send_message():
    resp = requests.post('https://textbelt.com/text',{
        'phone':mobile_number,
        'message':'This is message from automation app of python',
        # 'key':'texbelt',
        'key':'textbelt',
    })
    print(resp.json())

schedule.every().day.at('12:00').do(send_message)

# schedule.every(10).seconds.do(send_message)

while True:
    schedule.run_pending()
    time.sleep(1)