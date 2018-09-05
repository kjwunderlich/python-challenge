import os
import csv

csvpath = os.path.join(r"C:\Users\Owner\Desktop\MINSTP201808DATA2\03-Python\Homework\PyPoll\Resources\election_data.csv")

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)

    total_votes = 0
    candidate_count = {}

    for row in csvreader:
        total_votes = total_votes + 1
        candidate = str(row[2])
        if candidate in candidate_count:
            candidate_count[candidate] += 1
        else:
            candidate_count[candidate] = 1

candidate_percentage = {candidate: votes/total_votes for candidate, votes in candidate_count.items()} 

winner = None

for candidate, votes in candidate_count.items():
    if winner is None:
        winner = candidate
    elif candidate_count[winner] < votes:
        winner = candidate

print("Election Results")
print("-------------------------")
print("Total Votes: " + str(total_votes))
print("-------------------------")
for candidate in candidate_count:
    print("{}: {:.3%} ({})".format(candidate, candidate_percentage[candidate], candidate_count[candidate]))
print("-------------------------")
print("Winner: " + str(winner))

output_path = os.path.join("election_data_new.csv")
with open(output_path, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')
    csvwriter.writerow(["Election Results"])
    csvwriter.writerow(["Total Votes: " + str(total_votes)])
    for candidate in candidate_count:
        csvwriter.writerow(["{}: {:.3%} ({})".format(candidate, 
            candidate_percentage[candidate], candidate_count[candidate])])
    csvwriter.writerow(["Winner: " + str(winner)])