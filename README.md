# dns-resolver
DNS resolver from CS Dept(Computer Networks)
 I developed a Domain Name Resolver that leverages TCP/IP protocols to fetch various DNS records, such as IPv4, IPv6, Name Server, and Mail Server information. The project aimed at providing a more secure way to retrieve DNS information."
Technical Details:
● "The resolver was designed to interact directly with DNS servers using TCP/IP protocols, extracting critical information about domain names efficiently."
● "To enhance security, I implemented DNSSEC within the resolver. This involved validating the cryptographic signatures of DNS records to confirm their integrity and authenticity, thereby offering protection against DNS spoofing attacks.

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
