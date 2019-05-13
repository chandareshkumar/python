#*Program to convert a given number to words*_

#Write code to convert a given number into words.
# For example, if “1234” is given as input, output should be 
#“one thousand two hundred and thirty four”.

try:
	number=str(int(input('Enter number between 0-9999')))


	no=int(number)
	num=list(map(int,number))


	ones = ("zero", "one", "two", "three", "four", "five", "six",
	            "seven", "eight", "nine")
	teens = ("ten", "eleven", "twelve", "thirteen", "fourteen",
	             "sixteen", "seventeen", "eighteen", "nineteen")
	tens = ("", "", "twenty", "thirty", "forty", "fifty", "sixty",
	        "seventy", "eighty", "ninety")


	ans = []
	f=0 # included to add "and"
	
	while not len(num) == 0:
	    if len(num) == 4 and no !=0:       # Thousands
	        if (num[0]==0):
	        	pass
	        else:
	        	f=1	
		        ans.append(ones[num[0]])
		        ans.append("thousand")
	        del(num[0])
	    elif len(num) == 3:     # Hundereds

	        if (num[0]==0):
	        	pass
	        else:
	        	f=2    
	        	ans.append(ones[num[0]])
	        	ans.append("hundered")
	        del(num[0])
	    elif len(num) == 2:     # Tens or Teens
	        if f==1 or f==2:
	        	ans.append('and')
	        if num[0] == 1:  # Teens
	            ans.append(teens[num[1]])
	            del(num[:])
	        else:            # Tens
	            ans.append(tens[num[0]])
	            if num[1] != 0:
	                ans.append(ones[num[1]])
	            del(num[:])
	    else:
	               # Ones
	        ans.append(ones[num[0]])
	        del(num[:])             

	print(" ".join(ans))

except:
	print("Enter numbers only between 0-9999")
