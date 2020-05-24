The problem is similar to our old post Segregate 0s and 1s in an array, and both of these problems are variation of famous Dutch national flag problem.
The problem was posed with three colours, here `0′, `1′ and `2′. The array is divided into four sections:
a[1..Lo-1] zeroes
a[Lo..Mid-1] ones 
a[Mid..Hi] unknown
a[Hi+1..N] twos 
Complexity Analysis:

# Time Complexity: O(n).
Only one traversal of the array is needed.
# Space Complexity: O(1).
No extra space is required.