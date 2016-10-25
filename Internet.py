# Internet

from urllib.request import urlopen

with urlopen("http://www.test.com") as response:
    
    for line in response:
        
        line = line.decode("utf-8")
        print(line)
        
        
