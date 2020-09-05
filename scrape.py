import  requests
import helpers
import csv

csv_headers= ['id', 'creation_time', 'product', 'platform', 'priority', 'severity', 'summary']
priorities = ['P1', 'P2', 'P3', 'P4', 'P5']
statuses =['RESOLVED', 'VERIFIED']

def scrape():
    with open('rough_dataset.csv', 'a') as file:
        writer = csv.DictWriter(file, csv_headers)
        writer.writeheader()
        
    for priority in priorities:
        for status in statuses:
            status, response = helpers.search_bugs(('status', status), 
                                                ('priority', priority),
                                                ('type','defect'),
                                                ('resolution', 'FIXED'),
                                                ('include_fields','id, creation_time, product, platform, priority, severity, summary'))
            if status == 200:
                bugs = response['bugs']
                with open('rough_dataset.csv', 'a', newline='', encoding="utf-8") as file:
                    writer = csv.DictWriter(file, csv_headers)
                    for bug in bugs:
                        writer.writerow(bug)

if __name__ == "__main__":
    scrape()