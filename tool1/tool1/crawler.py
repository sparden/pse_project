from urllib.request import urlopen
from general import *
import nltk
import re
import urllib.request
from bs4 import BeautifulSoup
import urllib
import time


class Crawler:
    
    project_name = ''
    base_url = ''
    domain_name = ''
    queue_file = ''
    crawled_file = ''
    queue=set()
    crawled=set()

    def __init__(self,project_name,base_url,domain_name):
        Crawler.project_name = project_name
        Crawler.base_url = base_url
        Crawler.domain_name = domain_name
        Crawler.queue_file = Crawler.project_name+'/queue.txt'
        Crawler.crawled_file = Crawler.project_name+'/crawled.txt'
        self.boot()
        self.crawl_page('first crawler' , Crawler.base_url)
    @staticmethod
    def boot():
        create_project_dir(Crawler.project_name)
        create_data_file(Crawler.project_name,Crawler.base_url)
        Crawler.queue = file_to_set(Crawler.queue_file)
        Crawler.crawled = file_to_set(Crawler.crawled_file)

    @staticmethod
    def crawl_page(thread_name,page_url):
        if page_url not in Crawler.crawled:
            print(thread_name+' now crawling '+ page_url)
            print('Queue '+ str(len(Crawler.queue))+' | Crawled '+str(len(Crawler.crawled)))
            Crawler.add_links_to_queue(Crawler.gather_links(page_url))
            Crawler.queue.remove(page_url)
            Crawler.crawled.add(page_url)
            Crawler.update_files()

    @staticmethod
    def gather_links(page_url):
        html_string = ''
        #print(page_url)
        try:
            response = urlopen(page_url)
            
            moment=time.strftime("%Y-%b-%d__%H_%M_%S",time.localtime())
            path=Crawler.project_name+'/'+moment+'.txt'
            
            html = urllib.request.urlopen(page_url).read()
            soup = BeautifulSoup(html,"lxml")


            for script in soup(["script", "style"]):
                  script.extract()   

            text = soup.get_text()


            lines = (line.strip() for line in text.splitlines())

            chunks = (phrase.strip() for line in lines for phrase in line.split("  "))

            text = '\n'.join(chunk for chunk in chunks if chunk)

            file1 = open(path,'w') 
 
            for i in text:
                  file1.write(i) 
            file1.close()
 
            if response.getheader('Content-Type') == 'text/html':
                html_bytes = response.read()
                html_string = html_bytes.decode("utf-8")

                

               
            finder = LinkFinder(Crawler.base_url,page_url)
            finder.feed(html_string)
        except:
            print('Error: can not crawl page')
            return set()
        return finder.page_links()

    @staticmethod
    def add_links_to_queue(links):
        for url in links:
            if url in Crawler.queue:
                continue
                
            if url in Crawler.crawled:
                continue
        
            if Crawler.domain_name != get_domain_name(url):
                continue
                
            Crawler.queue.add(url)

    @staticmethod
    def update_files():
        set_to_file(Crawler.queue, Crawler.queue_file)
        set_to_file(Crawler.crawled, Crawler.crawled_file)


