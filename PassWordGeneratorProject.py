import string
import random
s=[]
s1=list(string.ascii_lowercase)
s2=list(string.ascii_uppercase)
s3=list(string.digits)
s4=list(string.punctuation)
s.extend(s1)
s.extend(s2)
s.extend(s3)
s.extend(s4)
l=int(input("Enter the length of your password:\n"))
random.shuffle(s)
print("Your PassWord is :")
print("".join(s[0:l]))