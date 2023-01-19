# CS-571-HW1

    Peter Mavronicolas
    Old Dominion Univeristy
    Spring 2023, Jan. 19, 2023

## Question 1
```commandline
//1 = Parent process (main())

int main()
{
          /* fork a child process */
         //2-4 = fork() function calls
            fork();
	fork();
fork();
          int i;
          //5-11= for loop with 7 iterations
          for (i=0; i <7; i++) 
             fork();/* fork another child process */
          //12 = final fork() function call
         fork();
         return 0;
}

Answer:

2^12 = 4096 processes:

1 = Parent process (main())
2-4 = fork() function calls
5-11= for loop with 7 iterations
12 = final fork() function call

```
## Question 2
```commandline
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
```
### Output
```commandline
/usr/bin/python3 /Users/austinpete/Documents/GitHub/CS-571-HW1/fork.py 
The sum of the first 8 natural numbers is: 36
The sum of the square of the first 8 natural numbers is:0
The sum of the first 15 natural numbers is: 120
The sum of the square of the first 15 natural numbers is:0

Process finished with exit code 0
```
## Question 3

## Question 4