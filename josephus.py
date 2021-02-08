# Code for solving the Josephus Problem

def main():
    n = int(input("Prisoners: "))
    k = 2
    who_goes_free(n, k)

def who_goes_free(n, k):
    prison = [[]]
    circle = 0
    for j in range(n):
        prison[0].append(j + 1) # adds prisoners
    i = 0
    while(len(prison[i]) != 1):
        if(circle == 0):
            # builds a new set of prisoners
            prison.append([])
            for j in range(len(prison[i])):
                prison[i + 1].append(prison[i][j])

        else:
            # builds a new set of prisoners
            prison.append([])
            prison[i + 1].append(prison[i][len(prison[i]) - 1])
            for j in range(len(prison[i]) - 1):
                prison[i + 1].append(prison[i][j])
        i = i + 1
        circle = len(prison[i]) % 2
        for j in range(int(len(prison[i]) / k)):
            del prison[i][j + 1 : j + 2]
    print(prison[i])

main()
