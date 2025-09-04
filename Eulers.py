import math
#A simple code to implement Euler totient function
P=int(input("Enter your prime P "))
Q=int(input("Enter your prime Q "))
print("Your N will be P*Q i.e.",P*Q)
N=P*Q
print("Now, the number of numbers below",N," which are coprime to",N," will be",(P-1)*(Q-1))
eulers=(P-1)*(Q-1)
print("i.e. your euler's totient for these values will be", eulers)

spacer=input("Press enter to see all the values")
print("These values are as follows, will be useful for you later")
counter=0
numbers=[]
for i in range(1,N):
    if(math.gcd(i,N)==1):
        counter+=1
        # print(i)
        numbers.append(i)
print(*numbers)
print("TOTAL No. of numbers:")
print(counter)
a=input("Press enter to calculate E")
Enumbers=[]
for i in range(3,N):
    if(math.gcd(i,eulers)==1):
        Enumbers.append(i)
print(*Enumbers)
print("we will use",Enumbers[0]," in our case")
E=Enumbers[0]
a=input("Press enter to calculate D")
print("Now calculating D")
i=0
while(True):
    i+=1
    print(E,"*",i,"=",E*i," %",eulers,"=",(E*i)%eulers)
    if((E*i)%eulers==1):
        D=i
        break
print("We finally found the smallest value of D for our example i.e.,",D)
print()
print("LESSGO FOUND PUBLIC KEY",N,",",E,"AND THE PRIVATE KEY",N,",",D)

print("Enter to finally encrypt and decrypt somehting")

data = int(input("\nEnter a number message to encrypt (must be < N): "))

# Encryption: C = M^E mod N
C = pow(data, E, N)
print("Encrypted message is:", C)

# Decryption: M = C^D mod N
M = pow(C, D, N)
print("Decrypted message is:", M)
