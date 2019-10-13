import random
from datetime import datetime, timedelta
import csv

random.seed()

timestamp = datetime.now()
file_name = 'generated_data.csv'

reading_1 = 30
reading_2 = 28

offset_length_1 = 0
offset_length_2 = 0

last_read = datetime.now()
last_offset_1 = datetime.now()
last_offset_2 = datetime.now()

overwrite = input('Overwrite file? y/n: ')
newfile = 'w' if overwrite == 'y' else 'a'

with open(file_name, 'a', newline='') as f:
		writer = csv.writer(f,delimiter=",")
		writer.writerow(['datetime','measurement','reading'])

print('LOGGING... Ctrl-C to Cancel')
while True:
	if datetime.now() - last_offset_1 > timedelta(seconds=offset_length_1):
		offset_1 = (random.random() - 0.5)
		offset_length_1 = int(random.random()*60*5)
		last_offset_1 = datetime.now()
	noise = (random.random() - 0.5)

	if datetime.now() - last_offset_2 > timedelta(seconds=offset_length_2):
		offset_2 = (random.random() - 0.5)
		offset_length_2 = int(random.random()*60*5)
		last_offset_2 = datetime.now()
	noise = (random.random() - 0.5)

	"""
	if datetime.now() - timestamp > timedelta(seconds=60):
		file_name = f'data_{datetime.now().strftime("%Y%m%d-%H%M%S")}.csv'
		timestamp = datetime.now()
	"""

	if datetime.now() - last_read > timedelta(seconds=1):
		reading_1 += noise + offset_1
		reading_2 += noise + offset_2
		last_read = datetime.now()
		with open(file_name, 'a', newline='') as f:
			writer = csv.writer(f,delimiter=",")
			writer.writerow([datetime.now(),'Temp1',reading_1])
			writer.writerow([datetime.now(),'Temp2',reading_2])