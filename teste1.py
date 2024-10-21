#
# choseone = 19
#
for num in range(2,100):
  for i in range(2,num):
    if num% i ==0:
      break
  else:
    print(f"{num} é um numero primo ")