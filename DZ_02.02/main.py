import csv

# data =  [['hostname', 'vendor', 'model', 'location'],
#         ['swi', 'Cisco', '3750', 'London '],
#         ['sw2', 'Cisco', '3850', 'Liverpool'],
#         ['sw3', 'Cisco', '3650', 'Liverpool'],
#         ['sw4', 'Cisco', '3650', 'London']]

with open('hosts.csv', mode='w') as f:
        names = ['hostname', 'vendor', 'model', 'location']
        file_writer = csv.writer(f, delimiter=';', lineterminator='\r', fieldnames=names)
        file_writer.writerow(['swi', 'Cisco', '3750', 'London '])
        file_writer.writerow(['sw2', 'Cisco', '3850', 'Liverpool'])
        file_writer.writerow(['sw3', 'Cisco', '3650', 'Liverpool'])
        file_writer.writerow(['sw4', 'Cisco', '3650', 'London'])





