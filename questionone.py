N,X,Y,Z = [3,1,1,1] #[int(x) for x in input().split()]

red = [N]
green = []
blue = []


def is_all_ones(array):
    for x in array:
        if x != 1:
            return False
    return True

def count_ones(array):
    i=0
    for x in array:
        if x == 1:
            i+=1
    return i


while(not(is_all_ones(red)) and not(is_all_ones(blue)) and not(is_all_ones(green))):
    for i,r in enumerate(red):
        red[i] = red[i] - 1
        for g in range(X):
            green.append(r)
    for i,g in enumerate(green): # since this can increment i down by 2, and we want blue 1's not blue zeros, this could be problematic
        red.append(g-1)
        green = green[:i].append(green[i+1:])
        for b in range(Z):
            blue.append(g-2)
    for i,b in enumerate(blue):
        if b > 1:
            blue = blue[:i].append(blue[i+1:])
            for k in range(Y):
                blue.append(b-1)
    print(red,blue,green)

print(count_ones(blue))




