import math

#dec variable
n =0
sum = 0
squared_n = 0
squared_sum = 0

def compute_and_sum(n):
    sum = 0
    for n in range(1,n+1):
	    sum = sum + n
    print(f"The sum of the first {n} natural numbers is: {sum}")

def sum_of_squares(n):
    squared_num =0
    squared_sum = 0
    for n in range(1,n+1):
        squared_n = pow(n,2)
        squared_sum = squared_sum + squared_num
    print(f"The sum of the square of the first {n} natural numbers is:{squared_sum}")

def main():
    fork(compute_and_sum(n));
    fork(sum_of_squares(n));


#dec var
n = 8
#call functions
compute_and_sum(n);
sum_of_squares(n);
#dec var
n = 15
#call functions
compute_and_sum(n)
sum_of_squares(n)