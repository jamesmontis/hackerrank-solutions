#From hackerrank discussions, saved for studying purposes
#
#Consider a list (list = []). You can perform the following commands:
#
#    insert i e: Insert integer #
#
#at position
#.
#print: Print the list.
#remove e: Delete the first occurrence of integer
#.
#append e: Insert integer
#
#    at the end of the list.
#    sort: Sort the list.
#    pop: Pop the last element from the list.
#    reverse: Reverse the list.
#
#Initialize your list and read in the value of
#followed by lines of commands where each command will be of the
#
#types listed above. Iterate through each command in order and perform the corresponding operation on your list.#
#
#Input Format
#The first line contains an integer,
#, denoting the number of commands.
#Each line of the
#subsequent lines contains one of the commands described above.
#Constraints
#    The elements added to the list must be integers.



#  inputs 
#12
#insert 0 5
#insert 1 10
#insert 0 6
#print
#remove 6
#append 9
#append 1
#print
#pop
#reverse
#print

if __name__ == '__main__':
    N = int(input())

n = N
l = []
for _ in range(n):
    s = input().split()
    cmd = s[0]
    args = s[1:]
    if cmd !="print":
        cmd += "("+ ",".join(args) +")"
        eval("l."+cmd)
    else:
        print(l)
