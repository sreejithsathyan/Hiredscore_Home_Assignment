# Import required moudules
from candidate import Candidate
from datetime import datetime

# calculate gap days in experience
def calculate_gap_days(end_date, start_date):
    if end_date and start_date:

        # Convert into date time format
        end_date = datetime.strptime(end_date, "%b/%d/%Y")
        start_date = datetime.strptime(start_date, "%b/%d/%Y")

        # Calculate days by substrting both dates 
        gap_days = (start_date - end_date).days - 1
        return gap_days if gap_days > 0 else 0
    else:
        return 0


# Extract and process candidate expereience
def process_candidates_data(data):
    candidates = []
    all_experiences = []
    # Itereting main data set
    for value in data:
        # Extract candidate name
        candidate_name = value["contact_info"]["name"]["formatted_name"]
        candidate = Candidate(candidate_name)

        # Set previous end_date fro gap cal
        previous_end_date = None

        # Iterating selected candidate experience
        for exp in value["experience"]:
            job_title = exp["title"] 
            job_location = exp["location"]["short_display_address"] 
            start_date = exp["start_date"] 
            end_date =  exp["end_date"]
            
            # Add experience of a candidate to a list "all_experiences"
            all_experiences.append({
                "role": job_title,
                "start_date" : start_date,
                "end_date" : end_date,
                "location" : job_location
                })

        # Sort expereience based on date
        all_experiences.sort(key=lambda x: datetime.strptime(x["start_date"], "%b/%d/%Y"))

        for exp_ in all_experiences:
            candidate.add_experience(
                exp_["role"],
                exp_["start_date"],
                exp_["end_date"],
                exp_["location"],
            )

            if previous_end_date:
                gap_days = calculate_gap_days(previous_end_date, exp_["start_date"])
                if gap_days > 0:
                    candidate.add_experience("Gap_in_CV",previous_end_date, exp_["start_date"],"",f"Gap in CV for {gap_days} days")
            previous_end_date = exp_["end_date"]

        candidates.append(candidate)    
    return candidates



        

