import datetime as dt
import time

end_time = dt.datetime(2023,7,10)
sites_to_block = ['www.xhamster.com']
host_path = '/etc/hosts'
redirect_number = '127.0.0.1'


while True:
    if dt.datetime.now() < end_time:
        print('start blocking')
        with open(host_path,'r+') as host_file:
            content = host_file.read()
            for website in sites_to_block:
                if website not in content:
                    host_file.write(redirect_number + " "  + website + "\n" )
                else:
                    pass
    else:
        with open(host_path,'r+') as host_file:
            content = host_file.readlines()
            host_file.seek(0)
            for lines in content:
                if not any(website in lines for website in sites_to_block):
                    host_file.write(lines)

            host_file.truncate()
        
        time.sleep(5)













































































































































# 127.0.0.1       localhost
# 127.0.1.1       NCPC

# # The following lines are desirable for IPv6 capable hosts
# ::1     ip6-localhost ip6-loopback
# fe00::0 ip6-localnet
# ff00::0 ip6-mcastprefix
# ff02::1 ip6-allnodes
# ff02::2 ip6-allrouters







