burger = "BPB"

for i in range(N-1):
    burger = "B"+burger+"P"+burger+"B"

def count_patties(stringg):
    i=0
    for x in stringg:
        if x == 'P':
            i+=1
    return i

print(count_patties(burger[-X:]))