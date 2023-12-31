input=[45,56,11,89,3,65,48,23,15,1,13]
input=[57,56,11,89,3,65,48,23,15,1,13]
input=[57,56,11,89,3,65,48,23,15,1]
input=[57,56,11,89,3,65,48,23,15,1,130]
input=[57,57,11,89,3,65,48,23,15,1,130]
# input=[]

def tri_insertion(input_array):
    for j in range(1,len(input_array)):
        key = input_array[j]
        # Insert input_array[j] into the sequence input_array[1..j-1]
        i = j-1
        while i >= 0  and input_array[i] > key:
            input_array[i+1] = input_array[i]
            i = i-1
        input_array[i+1] = key

        assert input_array[i+1] >= input_array[i] if i > 0 else True

    return input_array

print(tri_insertion(input))

def tri_insertion_reverse(input_array):
    for j in range(1,len(input_array)):
        key = input_array[j]
        # Insert input_array[j] into the sequence input_array[1..j-1]
        i = j-1
        while i >= 0  and input_array[i] < key:
            input_array[i+1] = input_array[i]
            i = i-1
        input_array[i+1] = key

        assert input_array[i+1] <= input_array[i] if i > 0 else True

    return input_array

print(tri_insertion_reverse(input))