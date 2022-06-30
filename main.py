# create company people and roles
people = ["Ann", "Chelsea", "Nichole", "Max"]
title = ["Marketing Coordinator", "Software Developer", "Sales Representative", "Technical Writer"]
company_org = {}

# add people and roles to company_org dictionary
for i in range(len(people)):
    person = people[i]
    person_title = title[i]
    company_org[person] = person_title

# display company people and roles
print(company_org)
