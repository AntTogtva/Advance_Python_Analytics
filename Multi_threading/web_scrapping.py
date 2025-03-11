# web scrapping using multithreading 

'''
scenario : Web Scrapping 
web scrapping oftern involves making numerous network requests to fatch web pages . 
these tasks are I/O bound because they spend a lot of time waiting for responsses from searver . 
multiprocessing can significantly improve the performance by allowing multiple web pages to be fetched conccurrently 
'''
'''
https://www.geeksforgeeks.org/understanding-time-complexity-simple-examples/

https://www.geeksforgeeks.org/g-fact-86/

https://www.geeksforgeeks.org/difference-between-process-and-thread/
'''

import threading
import requests

from bs4 import BeautifulSoup

urls =[
    "https://www.geeksforgeeks.org/understanding-time-complexity-simple-examples/",

"https://www.geeksforgeeks.org/g-fact-86/",

"https://www.geeksforgeeks.org/difference-between-process-and-thread/",

]

def fetch_contents(url):
    response = requests.get(url,verify=False)
    soup =BeautifulSoup(response.content,'html.parser')
    print(f'Fatched {len(soup.text)} characters from {url}')

threads = []
for url in urls :
    thread = threading.Thread(target=fetch_contents,args=(url,))
    threads.append(thread)
    thread.start()

for thread in threads : 
    thread.join()

print("all web pages fatched ")
