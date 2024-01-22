
class Candidate:

    def __init__(self,name):
        self.name = name
        self.votes = 0

    def add_votes(self):
        self.votes +=1

    
    def __str__(self):
        return f"Candidate :{self.name}, Votes : {self.votes}"



class VotingSystem:

    def __init__(self):
        self.candidates = []

    
    def add_candidate(self,candidate):
        self.candidates.append(candidate)


    def vote(self, candidate_name):

        for candidate in self.candidates:
            if candidate.name == candidate.name:
                candidate.add_votes()
        return print(f"No candidate found with the name {candidate_name}.")     

    def show_results(self):
        for candidate in self.candidates:
            print(candidate) 




def main():
    # Create a voting system
    voting_system = VotingSystem()

    # Add candidates
    for name in ["Alice", "Bob", "Charlie", "Diana", "Evan"]:
        voting_system.add_candidate(Candidate(name))

    # Simulate voting
    print("Vote for a candidate by typing their name. Type 'exit' to finish.")
    while True:
        vote = input("Vote for: ").capitalize()
        if vote == 'Exit':
            break
        voting_system.vote(vote)

    # Show results
    print("\nElection Results:")
    voting_system.show_results()

if __name__ == "__main__":
    main()