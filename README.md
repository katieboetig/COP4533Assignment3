Programming Assignment: Highest Value Longest Common Sequence

**Problem Statement**  
You are given two strings A and B over a fixed alphabet. Each character in the alphabet has  
a nonnegative integer value. Your task is to compute a common subsequence of A and B that  
maximizes the total value, and to output both this maximum value and the corresponding  
subsequence itself.  
If a sequence C \= c1c2 . . . ck is chosen, then its value is  
Val(C) \= SIGMA(v(ci)), from i=1 to k  
where v(ci) is the value assigned to character ci. Your program must output both Val(C)  
and one optimal subsequence C.

**Input Format**  
The input is given in the following format:  
K  
x1 v1  
x2 v2  
...  
xK vK  
A  
B  
• K is the number of characters in the alphabet.  
• Each of the next K lines contains a character and its value.  
• A is the first string.  
• B is the second string.

**Output**  
Print: (a) a single integer: the maximum value of a common subsequence of A and B.  
(b) On the next line, one optimal common subsequence that achieves this value. If multiple  
optimal subsequences exist, you may output any one of them.

**Worked Example**  
Input:  
Alphabet values:  
a \-\> 2  
b \-\> 4  
c \-\> 5  
A \= aacb  
B \= caab  
Output:  
9  
cb  
Verification:  
Val(cb) \= 5 \+ 4 \= 9\.

**Question 1: Empirical Comparison**  
Use at least 10 nontrivial input files (i.e., contain strings of length at least 25). Graph the  
runtime of the 10 files.  
All resulting data is in the "results.txt" file, and then that data is transferred into the "plot\_graph.py" file. To rebuild, run the following:  
python data/plot\_graph.py  
That will create a new png, but for your convenience, this has already been created and uploaded (runtime\_analysis.png) to the repository.

**Question 2: Recurrence Equation**  
Give a recurrence that is the basis of a dynamic programming algorithm to compute the  
HVLCS of strings A and B. You must provide the appropriate base cases, and explain why  
your recurrence is correct.  
OPT(i,j)= max weighted common sequence of A(1, …, i) and B(1, …, j)  
Case 1: Base Case (A and/or B have length 0\)  
	i=0 and j=0, so there is no common sequence and therefore 0  
	OPT(i,j)=0  
Case 2: Match (A\[i\]=B\[j\])  
From here 3 options: accept it and move onto next value, skip to next in A to see if more optimal solution, or skip to next in B to see if more optimal solution (select whichever is maximum value)  
OPT(i, j)= max{ OPT(i-1, j-1)+V(A\[i\]), OPT(i-1, j), OPT(i, j-1)}  
Note that V(B\[j\]) has same value as V(A\[i\]) so you could swap and it wouldn’t make a difference  
Case 3: No Match (A\[i\]\!=B\[j\])  
Skip to the next in the sequence for either A or B (whichever produces higher OPT)  
OPT(i,j)=max{ OPT(i-1,j), OPT(i, j-1)}

Overall recurrence equation:  
\*OPT(i, j)={ 0 if i=0 or if j=0, max{ OPT(i-1, j-1)+V(A\[i\]), OPT(i-1, j), OPT(i, j-1)} if A\[i\]=B\[j\], max{ OPT(i-1,j), OPT(i, j-1)} if A\[i\] \!= B\[j\]}  
\*for better readability the file “recurrance.png” has it written out in standard piece-wise form

**Question 3: Big-Oh**  
Give pseudocode of an algorithm to compute the length of the HVLCS of given strings A  
and B. What is the runtime of your algorithm?  
Submission and Deliverables (GitHub)

Running Instructions:  
Run all tests at once:   
for i in {1..10}   
do  
echo "test$i" time python src/hvlcs.py \< tests/test$i.in \> tests/test$i.out   
done

Single Test:   
time python src/hvlcs.py \< tests/example.in \> tests/example.out

\*note: "python3" might need to replace "python" if working on MacOS.  

