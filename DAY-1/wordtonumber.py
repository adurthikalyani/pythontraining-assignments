number=int(input("enter integer:"))

def int_to_string(number):
  d = { 0 : 'zero', 1 : 'one', 2 : 'two', 3 : 'three', 4 : 'four', 5 : 'five', \
          6 : 'six', 7 : 'seven', 8 : 'eight', 9 : 'nine', 10 : 'ten', \
          11 : 'eleven', 12 : 'twelve', 13 : 'thirteen', 14 : 'fourteen', \
          15 : 'fifteen', 16 : 'sixteen', 17 : 'seventeen', 18 : 'eighteen', \
          19 : 'ninteen', 20 : 'twenty', \
          30 : 'thirty', 40 : 'fourty', 50 : 'fifty', 60 : 'sixty', \
          70 : 'seventy', 80 : 'eighty', 90 : 'ninty' }
  k=1000
  m=k*1000
  
  if(number<20):
    return d[number]
  if(number<100):
    if(number % 10 ==0):
      return d[number]
    else:
      return d[number//10 *10]+ ' '+d[number % 10]
  if(number< k):
    if number%100 == 0:
      return d[number// 100]+' '+'hundred'
    else:
      return d[number//100]+' '+'hundred'+' '+'and'+' '+int_to_string(number % 100)
  if(number < m):
    if number % k ==0:
      return int_to_string(number //k)+' '+'thousand'
    else:
      return int_to_string(number//k)+' '+'thousand'+' '+'and'+' '+ int_to_string(number % k)
  
print('%d in words is: %s' %(number,int_to_string(number)))