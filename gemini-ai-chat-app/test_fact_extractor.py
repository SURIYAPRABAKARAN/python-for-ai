from fact_extractor import extract_user_facts
from profile_service import load_profile , save_profile

# result = extract_user_facts("hi my name is suriya .26 years old , java professinol with 3+ years experience. I;m skilled with spring boot ,  kafka , react , java 11 , docker , microservice , RestApi. currenctly I'm started learning of Ai engineering things")

user_message =  "hi my name is suriya .26 years old , java professinol .My Ctc is 12LPA"

profile = load_profile()

new_facts = extract_user_facts(user_message)

profile.update(new_facts)

save_profile(profile)

print("Process Completed")