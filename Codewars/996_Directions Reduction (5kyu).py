dirrection = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]


def dirreduc(arr):
    while True:
        for i in range(len(arr)):
            if (arr[i] == 'NORTH' and arr[i+1] == 'SOUTH') or (arr[i+1] == 'NORTH' and arr[i] == 'SOUTH') or \
                    (arr[i] == 'EAST' and arr[i+1] == 'WEST') or (arr[i+1] == 'EAST' and arr[i] == 'WEST'):
                del arr[i]
                del arr[i+1]
            # elif (arr[i] == 'EAST' and arr[i+1] == 'WEST') or (arr[i+1] == 'EAST' and arr[i] == 'WEST'):
            #     arr.pop(arr[i])
            #     arr.pop(arr[i+1])
        else:
            break

    pass


print(dirreduc(dirrection))
# WEST
