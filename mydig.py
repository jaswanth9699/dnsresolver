import dns.message
import dns.query
import sys
import time
import datetime

#Recursive function which will recursively process the responses from the dns servers to find the ip


def recursive_dns(url: str, ip: str, root: str):
    query = dns.message.make_query(url, "A", 1, None, False, None, None, None, None)
    response = dns.query.udp(query, ip, 1, 53, None, None, 0, False, False, False)

    if not len(response.answer) == 0:                       #If response has an answer section use that
        if " CNAME " in response.answer[0].to_text():       #Handles if a CNAME is returned instead of an ip
            for x in response.answer:
                file.write("%s\n" % x.to_text())
            return recursive_dns(extract(response.answer[0].to_text()), root, root)
        else:                                               #Other case is A in which that is the final result
            return response.answer
    elif not len(response.additional) == 0:                 #Grabs next dns server ip if provided in additional section
        for e in response.additional:
            try:
                if " A " not in e.to_text():                #ensures A response
                    continue
                else:
                    return recursive_dns(url, extract(e.to_text()), root)
            except dns.exception.Timeout:
                continue
            break
    else:
        for c in response.authority:                        #Other case of a nameserver being returned in the authority section
            try:
                if " NS " not in c.to_text():               #ensures NS response
                    continue
                else:
                    next_ip = recursive_dns(extract(c.to_text()), root, root)
                    return recursive_dns(url, extract(next_ip[0].to_text()), root)
            except dns.exception.Timeout:
                continue
            break


def extract(b: str):        #Helper function to trim message down to either the name of the name server or the ip address
    index = len(b) - b[::-1].index(" ") - 1
    return b[index + 1:]


find_url = sys.argv[1]
file = open("mydig_output.txt", "w+")                       #output file
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]    #array for output handling
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]   #array for output handling
roots = ["198.41.0.4", "199.9.14.201", "192.33.4.12", "199.7.91.13", "192.203.230.10", "192.5.5.241", "192.112.36.4",
         "198.97.190.53", "192.36.148.17", "192.58.128.30", "193.0.14.129", "199.7.83.42", "202.12.27.33"]      #array of root servers to test

file.write("QUESTION SECTION:\n%s IN A\n\nANSWER SECTION:\n" % find_url)
start = time.time()
i = 12
while not False:        #starts the recursive function
    try:
        if i >= 13:         #Goes through all root servers incase it times out on any
            i = 0
        test = recursive_dns(find_url, roots[i], roots[i])
    except dns.exception.Timeout:
        continue
    break

end = time.time()
millis = str(int(round((end * 1000) - (start * 1000))))

now = datetime.datetime.now()
for a in test:
    file.write("%s\n" % a.to_text())
file.write("\nQuery time: %s msec\nWHEN: %s %s %s %s:%s:%s %s\nMSG SIZE rcvd: %s" % (millis, days[now.weekday()], months[now.month - 1], str(now.day),
                                                                                     str(now.time().hour), str(now.time().minute), str(now.time().second),
                                                                                     str(now.year), test.__sizeof__()))