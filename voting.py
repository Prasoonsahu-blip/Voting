import os
print("Elect for good")
print("To vote for Candidate 1 PRESS 1")
print("To vote for Candidate 2 PRESS 2")
print("To vote for Candidate 3 PRESS 3")
print("To vote for Candidate 4 PRESS 4")
print("Press 10 to Print result")
i=int(input("Enter your choice"))
votes=[0,0,0,0]
while i!=10:
    if i>=1 and i<=4:
        votes[i-1]+=1
    else:
        print("Invalid input")
    input("Press Enter for next voter...")
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Elect for good")
    print("To vote for Candidate 1 PRESS 1")
    print("To vote for Candidate 2 PRESS 2")
    print("To vote for Candidate 3 PRESS 3")
    print("To vote for Candidate 4 PRESS 4")
    print("Press 10 to Print result")
    i=int(input("Enter your choice"))
print("\nVoting Results")
for j in range(4):
    print(f"Candidate {j+1}: {votes[j]} votes")