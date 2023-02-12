import csv

with open('hosts.csv', mode='w') as f:
        file_writer = csv.writer(f, delimiter=';', lineterminator='\r')
        file_writer.writerow(['hostname', 'vendor', 'model', 'location'])
        file_writer.writerow(['swi', 'Cisco', '3750', 'London '])
        file_writer.writerow(['sw2', 'Cisco', '3850', 'Liverpool'])
        file_writer.writerow(['sw3', 'Cisco', '3650', 'Liverpool'])
        file_writer.writerow(['sw4', 'Cisco', '3650', 'London'])





