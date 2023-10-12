import os
import datetime
import reports
import emails

date = datetime.date.today().strftime('%d %m, %Y')
head = f'Processed  Update on {date}'
names = []
weights = []
summary = ''
path = './supplier-data/descriptions/'

for file in os.listdir(path):
    with open(os.path.join(path, file)) as f:
        for lines in f:
            line = lines.strip()
            if len(lines) <= 10 and len(lines) > 0 and 'lb' not in lines:
                names.append('name: ' + line)
            if 'lb' in line:
                weights.append('weight: ' + line)

for name, weight in zip(names,weights):
    summary =+ f'{name}<br />{weight}<br />'
    
if __name__ == "__main__":
    reports.generate_report("/tmp/processed.pdf", date, summary)
    sender = "automation@example.com"
    receiver = "{}@example.com".format(os.environ.get('USER'))
    subject = "Upload Completed - Online Fruit Store"
    body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."

    message = emails.generate_email(sender, receiver, subject, body, "/tmp/processed.pdf")
    emails.send_email(message)