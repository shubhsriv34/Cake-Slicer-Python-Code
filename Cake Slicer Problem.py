"""    Point To Be Noted Cake
   Is Considered Circular
  Minimum Angle/Pieces = 1 Degree
  Maximum Pieces Possible = 360   """




"""First Condition  {(1). Cut The Cake Into N equal Pieces} """

N=int(input("Enter The Number Of Cuts You Want 'N': "))   # Entering Number Of Cuts You Want
if N==1 or N==360:
    print("Enter the value of 'N' Such That 1 < N <= 360")
elif (360%N)==0:
    print("First Answer: YES",N,"Equal Pieces Are Possible")
else:
    print("First Answer: NO",N,"Equal Pieces Are Not Possible")



"""Second Condition  {(2). Cut The Cake Into N Pieces Of Any Size} """



sum=0
for i in range(N):
    a=int(input("Enter The Angle Size Total Of 360= "))
    sum=sum+a
if sum==360:
    print("Second Answer YES: Cake Can Be Cutted In ",N,"Pieces")
else:
    print("Second Answer NO: Total Is Not 360, Hence Re-Enter the Values")




""""Third Condition {(3). Cut The Cake Into N Pieces Such That No Any Two Of Them Are Equal} """



"""Considering Minimun Angle Sum For Maximum Output
1+2+3+4+........23+24+25+35=360
i.e N=26
If N>=27 Small Angle Will Be Repeated And HenceForth 
Larger Values Will Also Be Repeated 
"""


if N<=26:
    print("Third Answer YES: Unequal Pieces Are Possible")
else:
    print("Third Answer NO: Unequal Pieces Are Not Possible")