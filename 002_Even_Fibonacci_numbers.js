/*
Each new term in the Fibonacci sequence is generated by adding the previous two terms.
By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, 
find the sum of the even - valued terms.
*/


function fibonacci(max) {
    next = 0
    first = 1
    second = 2
    sum = second
    while (next < max) {
        next = first+second
        if (next%2==0) sum += next
        first = second
        second = next
    }
    return sum
} 

console.log(fibonacci(4000000))