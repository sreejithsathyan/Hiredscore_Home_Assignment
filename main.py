# Import required moudules
import requests
import json
from data_processor import process_candidates_data 

# Load config file
def load_config(config_file):
	with open(config_file, 'r') as f:
		return json.load(f)

# fetch data from API
def fetch_data(url):
	response = requests.get(url)
	response.raise_for_status()
	return response.json()


def main(config_file):
	config = load_config(config_file)
	data = fetch_data(config["url"])
	if data:
		candidates = process_candidates_data(data)

		# Writing into output file
		candidates_dict = [candidate.to_dict() for candidate in candidates]
		with open(config["output_filename"], 'w') as outfile:
			json.dump(candidates_dict, outfile, indent=4)

		# For printing as per the sample output
		for candidate in candidates:
			print(f"Hello {candidate.name},")
			for exp in candidate.experiences:
				if exp["role"] == 'Gap_in_CV':
					print(exp["description"])
				else:
					print(f" Worked as: {exp['role']}, From {exp['start_date']} To {exp['end_date']} in {exp['location']}")
			print("________________________________________________")


if __name__ == "__main__":
	config_file = "config.json"
	main(config_file)