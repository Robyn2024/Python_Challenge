
import os
import csv


election_votes = os.path.join('PyPoll','Resources','election_data.csv')


total_votes=0
charles_votes=0
diana_votes=0
raymon_votes=0


with open(election_votes,newline="", encoding="utf-8") as elections:

    csvreader=csv.reader(elections,delimiter=",")

    header=next(csvreader)

    for row in csvreader:
        total_votes+=1

        if row[2]=="Charles Casper Stockham":
            charles_votes+=1
        elif row[2]=="Diana DeGette":
            diana_votes+=1
        elif row[2]=="Raymon Anthony Doane":
            raymon_votes+=1

candidates=["Charles Casper Stockham","Diana DeGette","Raymon Anthony Doane"]
votes=[charles_votes, diana_votes, raymon_votes]


dict_candidates_and_votes=dict(zip(candidates,votes))
key= max(dict_candidates_and_votes, key=dict_candidates_and_votes.get)

charles_percent=(charles_votes/total_votes)*100
diana_percent=(diana_votes/total_votes)*100
raymon_percent=(raymon_votes/total_votes)*100

print(f"Election Results")
print(f"-----------------------------")
print(f"Total Votes:{total_votes}")
print(f"-----------------------------")
print(f"Charles Casper Stockham: {charles_percent:.3f}%({charles_votes})")
print(f"Diana DeGette: {diana_percent:.3f}%({diana_votes})")
print(f"Raymon Anthony Doane: {raymon_percent:.3f}%({raymon_votes})")
print(f"-----------------------------")
print(f"Winner:{key}")
print(f"-----------------------------")

election_votes= os.path.join('PyPoll','analysis','analysis_results')
with open(election_votes, "w") as text_file:
    print(f"Election Results",file=text_file)
    print("\n",file=text_file)
    print(f"----------------------------",file=text_file)
    print("\n",file=text_file)
    print(f"Total Votes: {total_votes}",file=text_file)
    print("\n",file=text_file)
    print(f"----------------------------",file=text_file)
    print("\n",file=text_file)
    print(f"Charles Casper Stockham: {charles_percent:.3f}% ({charles_votes})",file=text_file)
    print("\n",file=text_file)
    print(f"Diana DeGette: {diana_percent:.3f}% ({diana_votes})",file=text_file)
    print("\n",file=text_file)
    print(f"Raymon Anthony Doane: {raymon_percent:.3f}% ({raymon_votes})",file=text_file)
    print("\n",file=text_file)
    print(f"----------------------------",file=text_file)
    print("\n",file=text_file)
    print(f"Winner: {key}",file=text_file)
    print("\n",file=text_file)
    print(f"----------------------------",file=text_file)