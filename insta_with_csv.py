from requests import get
from json import loads, dump
from re import compile
from os import system,path
import argparse
from bs4 import BeautifulSoup
from pandas import read_csv, read_json
import sys

try:
	parser = argparse.ArgumentParser()
	parser.add_argument("--csv", help="Provides the CSV file containing usernames")
	args = parser.parse_args()
	csv_filename = args.csv
	if csv_filename:
		if not path.exists(csv_filename):
			print("Path is wrong")
			sys.exit()
		for username in read_csv(csv_filename):
			page = get("https://www.instagram.com/"+username+"/")
			soup = BeautifulSoup(page.text,'html.parser')
			all_script = soup.find_all('script')
			json_data = loads(all_script[3].text)
			script_tag = soup.find('script', text=compile('window\._sharedData'))
			shared_data = script_tag.string.partition('=')[-1].strip(' ;')
			json_value = loads(shared_data)
			with open(username+".json", "w") as write_file:
				dump(json_value, write_file, indent=4)
			df = read_json(username+".json")
			df.to_csv(username+'.csv')
		print("Done")
except KeyboardInterrupt:
	print("Interrupted Process")
except Exception as e:
	print(e)