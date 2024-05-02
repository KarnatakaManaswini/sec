from collections import deque
s=input()
arr=list(map(str,s.split()))
map1={"zero":0,
      "one":1,
      "two":2,
      "three":3,
      "four":4,
      "five":5,
      "six":6,
      "seven":7,
      "eight":8,
      "nine":9}
map2={"add","sub","mul","rem","pow"}
flag = 0

for i in arr:
   individual_vals = list(map(str, i.split("c")))
   for j in individual_vals:
       if (j not in map1) and (j not in map2):
           flag = 1
           break
   if flag == 1:
       break
if flag == 1:
   print("expression evaluation stopped invalid words present")
else:
   arr = arr[::-1]
   stack = deque()
   for i in arr:
       if i in map2:
           if not stack:
               flag = 1
               break
           a = stack.pop()
           if not stack:
               flag = 1
               break
           b = stack.pop()
           c = 0
           if i == "add":
               c = a+b
           elif i == "sub":
               c = a-b
           elif i == "mul":
               c = a*b
           elif i == "rem":
               c = a % b
           elif i == "pow":
               c = a**b
           stack.append(c)
       else:
           individual_vals = list(map(str, i.split("c")))
           actual_val = []
           for j in individual_vals:
               actual_val.append(map1[j])
           val = ""
           for i in actual_val:
               val += str(i)
           val = int(val)
           stack.append(val)
   if flag == 1:
       print("expression is not complete or invalid")
   else:
       c = stack.pop()
       if not stack:
           print(c)
       else:
           print("expression is not complete or invalid")