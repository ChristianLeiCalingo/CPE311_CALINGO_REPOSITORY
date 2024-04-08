def contig_subseq(n, num_list):
    for x in num_list:
        result = x + x
        
    print("The total Contiguous Subsequence is:", result)
    
num_list = []
n = int(input("How many number you would like to input: "))
counter = 0

while counter < n:
    number = int(input("Enter the number: "))
    num_list.append(number)
    counter+=1
contig_subseq(n,num_list)
    