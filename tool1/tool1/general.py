import os #allows to create directory
from urllib.parse import urlparse
from html.parser import HTMLParser
from urllib import parse

def create_project_dir(directory):
    if not os.path.exists(directory):
        print('creating project ' +directory)
        os.makedirs(directory)
    else :
        print ('already has '+directory)

def create_data_file(project_name,base_url):
    queue = project_name + '/queue.txt'
    crawled= project_name + '/crawled.txt'
    if not os.path.isfile(queue):
        write_file(queue,base_url)
    if not os.path.isfile(crawled):
        write_file(crawled,'')


'''
def create_html_page(name,html_string):
    name=name+'/n.txt'

    write_file(name,html_string)
'''

def write_file(path,data):
    f=open(path,'w')
    f.write(data)
    f.close()


def append_to_file(path, data):
    with open(path,'a') as file:
        file.write(data + '\n')


def delete_file_contents(path):
    with open(path,'w'):
        #do nothing
        pass


def file_to_set(file_name):
    results=set()
    with open(file_name,'rt') as f :
        for line in f:
            results.add(line.replace('\n',''))
    return  results


def set_to_file(links,file):
    delete_file_contents(file)
    for link in sorted(links):
        append_to_file(file,link)
#dfds

def get_domain_name(url):
    try:

        results = get_sub_domain_name(url).split('.')
        x=(len(results))
        if x==2 :
            return results[-2]+'.'+results[-1]
        elif x==3:
            return results[-3]+'.'+results[-2]+'.'+results[-1]
        '''for i in range(x-1,0,-1):
            if i==0:
                return results[i]
            else:
                return results[i]+'.'
        '''
    except:
        return ''

def get_sub_domain_name(url):
    try:
        return urlparse(url).netloc
    except:
        return ''


class LinkFinder(HTMLParser):
    def __init__(self,base_url,page_url):
        super().__init__()
        self.base_url=base_url
        self.page_url=page_url
        self.links=set()
    def handle_starttag(self,tag,attrs):
        #print(tag)
        if tag=='a':
            for(attribute,value) in attrs:
                if attribute=='href':
                   url = parse.urljoin(self.base_url,value)
                   self.links.add(url)
       # if tag=='b':
	    

    def page_links(self):
        return self.links

    def error(self,message):
        pass
#a=get_domain_name('http://paytm.com/')
#print(a)
#create_project_dir('ABC')
#create_data_file('ABC','http://www.abc.com')
