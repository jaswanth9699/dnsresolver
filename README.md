# dns-resolver
DNS resolver from CSE 310 (Computer Networks)
### How to run:

My program is ran through the command line. All my tests were done from the console
inside my IDE, Pycharm. You must have DNSPython installed, as this is the library I used to
query the DNS servers. Running the python script takes one argument, the website to query,
and outputs a mydig_output.txt to the same folder as mydig.py. Here is an example command
line command:
```
C:\...\(Path to mydig.py)> python mydig.py www.cs.stonybrook.edu
```
### Data:

I included an excel sheet where I tested my DNS Resolver against Ubuntu's local resolver and Google's Resolver. I tested my program on the top 25 sites as listed on https://www.alexa.com/topsites. I found that although my DNS Resolver was not as fast as the other two resolvers, it was just as reliable in obtaining results. I found this to be a major success for my first time network programming.
