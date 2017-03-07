arr = [int(x) for x in number]

# Count how many pairs are not equal
# arr, the number in array form
# start, index 0
# end, last index of arr
# count, the minimum changes needed to make the number a palindrome
def count_min_changes(arr, start, end):
    count = 0
    
    while start <= end:
        head = arr[start]
        tail = arr[end]
        
        if not head == tail:
            count+=1
            
        start+=1
        end-=1
    return count

# Make the necessary changes
# arr, the number in array form
# min_changes, the minimum amount of changes possible to make arr a palindrome
# k, given amount of changes
# start, index 0
# end, last index of arr
def make_changes(arr, min_changes, k, start, end):
    if min_changes > k: #not enough changes to make the arr a palindrome
        return "-1"
    if k > len(arr): #k is more than the length of arr therefore return the maximum possible arr
        return max_number(arr)

    while start <= end:
        head = arr[start]
        tail = arr[end]
        
        if head == tail and not head == 9:
            if k-2 >= min_changes: #if (the given amount of changes - 2) is still greater than the min_changes, change the numbers to 9
                arr[start] = 9
                arr[end] = 9
                k-=2
        elif not head == tail:
            if head == 9 or tail == 9:
                if head == 9:
                    arr[end] = 9
                else:
                    arr[start] = 9
                min_changes-=1
                k-=1
            else: #2 different numbers
                if k-2 >= 0 and k-2 >= min_changes-1: #available change is still above minimum possible changes
                    arr[start] = 9
                    arr[end] = 9
                    k-=2
                    min_changes-=1
                elif k-1 >= min_changes-1:
                    if head > tail:
                        arr[end] = arr[start]
                    else:
                        arr[start] = arr[end]
                    k-=1
                    min_changes-=1
        start+=1
        end-=1
    if k == 1 and len(arr)%2 > 0: #only 1 change is possible, therefore change the middle digit to 9
        mid = len(number)//2
        arr[mid] = 9
    
    return arr

# Change the array to a maximum array
# arr, the number array
# arr, max array where all digits are 9
def max_number(arr):
    for i in range(len(arr)):
        arr[i] = 9
    return arr
        
min_changes = count_min_changes(arr, 0, len(arr)-1)
new_number = make_changes(arr, min_changes, k, 0, len(arr)-1)
print("".join(str(x) for x in new_number))
