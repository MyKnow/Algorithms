# [def(int, list)] updatelistOfTeams
# Function that updates a global list called "listOfTeams"
#
# - Parameters
# [int] depth: Integer that used for backtracking
# [list] stack: Integer list that represents possible combinations of start team.
def updatelistOfTeams(depth: int, stack: list):
    # Update listOfTeams when depth reaches N // 2 people that maximum lenght of the teams
    if (depth == N//2):
        # [set(int)] remaining
        # : Obtain set of link team by difference between 
        # set of all members and set of start team.
        remaining = set(range(N)) - set(stack)

        # Group to start and link teams into a 
        # list, and append them to listOfTemas.
        listOfTeams.append( [set(stack), remaining] )
        
        return
    
    # For optimization
    if stack and stack[0] != 0:
        return

    # [int] start
    # : Define start indexbased on stack length for non-decreasing sort 
    start = stack[-1] + 1 if stack else 0

    # Get number of Member
    for numberOfMember in range(start, N):
        # Append numberOfMember into stack
        stack.append(numberOfMember)
        # Try appending next member
        updatelistOfTeams(depth+1, stack)
        # Backtracking
        stack.pop()

# [def(set)) -> list] getSequence
# Function that returns list of possible combinations of src to non-decreasing sort
def getSequence(src: set):
    tmpList = list()
    # Append (i, j) tuple into tmpList by non-decreasing sort
    for i in src:
        for j in src:
            if i < j:
                tmpList.append( (i, j) )
    return tmpList

# [int] N: 
# : Integer representing number of people (range(even): 4 ≤ N ≤ 20)
N = int(input())

# [list(list)] S
# : 2-Dimensional list that represents status of each combinations
S = [list(map(int, input().split())) for _ in range(N)]

# [list(list(set))] listOfTeams
# : 2-Dimensional list that including set of possible team distribution
listOfTeams = list()

# Update listOfTeams
updatelistOfTeams(0, [])

# Update minValue
minValue = float('inf')

# Get member list of both team
for teamA, teamB in listOfTeams:
    # [list(int)] result
    # : list of integer for calculate minValue
    result = [0, 0]

    # Get index and teamA, teamB members
    for idx, team in enumerate( (teamA, teamB) ):
        # Get possible combinations for each team and update the results.
        for i, j in getSequence(team):
            result[idx] += S[i][j] + S[j][i]
    minValue = min(minValue, abs(result[0]-result[1]))

print(minValue)