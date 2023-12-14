S=input("Entrez un mot ou une phrase : ")
temp = ""
for i in range(len(S)):
    if S[i].isalpha():
        temp += S[i]
    
test = temp.lower()
leftPos = 0
rightPos = len(test) - 1
palindrome = True
while ((leftPos < rightPos) and palindrome):
    palindorme = (test[leftPos] == test[rightPos])
    leftPos+=1
    rightPos-=1

if palindrome:
    print("C'est un palindrôme")
else:
    print("Non, ce n'est pas un palindrôme.")