# This is how you can override the HTMLParser class
# Enter your code here. Read input from STDIN. Print output to STDOUT
from html.parser import HTMLParser as hp

class MyHtmlParser(hp):
    def handle_starttag(self, tag, attrs):
        print('Start : ' + tag)
        if attrs:
            print(*['-> {} > {}'.format(attrs[y][0], attrs[y][1]) for y in range(len(attrs))], sep='\n')
            
    def handle_endtag(self, tag):
        print('End   : ' + tag)
        
    def handle_startendtag(self, tag, attrs):
        print('Empty : ' + tag)
        if attrs:
            print(*['-> {} > {}'.format(attrs[y][0], attrs[y][1]) for y in range(len(attrs))],sep='\n')
    
    def handle_comment(self, data):
        pass

html=["<html><head><title>HTML Parser - I</title></head>",
"<body data-modal-target class='1'><h1>HackerRank</h1><br /></body></html>"]
    
parser = MyHtmlParser()
parser.feed(''.join(html))