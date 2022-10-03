def printadd(arr,arr_leng,find):
    hashmap = {}
    for i in range(0,arr_leng):
        temp = find - arr[i];
        if (temp in hashmap):
            print (f'Pair with given sum {find} is ({temp},{arr[i]}) at indices ({hashmap[temp]},{i})')
            hashmap[arr[i]] = i

list = [3,5,7,10];
k = 17;
leng = len(list);
printadd(list,leng,k);