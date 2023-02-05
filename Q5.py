x=input("enter the string:")
def case_count(s):
  upper=0
  lower=0
  for j in s:
    if j.isupper():
      upper=upper+1
    elif j.islower():
      lower=lower+1
    else:
      pass
  print("No of upper case charecters:",upper)
  print("No of lower case charecters:",lower)
case_count(x)
