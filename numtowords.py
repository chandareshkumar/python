#*Program to convert a given number to words*_

#Write code to convert a given number into words.
# For example, if “1234” is given as input, output should be 
#“one thousand two hundred thirty four”.


num=str(input('Enter number between 0-9999'))

assert len(num) > 0 and len(num) < 5, "Invalid number entered"

num=list(map(int,num))


ones = ("zero", "one", "two", "three", "four", "five", "six",
            "seven", "eight", "nine")
teens = ("ten", "eleven", "twelve", "thirteen", "fourteen",
             "sixteen", "seventeen", "eighteen", "nineteen")
tens = ("", "", "twenty", "thirty", "forty", "fifty", "sixty",
        "seventy", "eighty", "ninety")



ans = []

while not len(num) == 0:
    if len(num) == 4:       # Thousands
        ans.append(ones[num[0]])
        ans.append("thousand")
        del(num[0])
    elif len(num) == 3:     # Hundereds
        ans.append(ones[num[0]])
        ans.append("hundered")
        del(num[0])
    elif len(num) == 2:     # Tens or Teens
        if num[0] == 1:  # Teens
            ans.append(teens[num[1]])
            del(num[:])
        else:            # Tens
            ans.append(tens[num[0]])
            if num[1] != 0:
                ans.append(ones[num[1]])
            del(num[:])
    else:                # Ones
        ans.append(ones[num[0]])
        del(num[:])             # Ones

print(" ".join(ans))
