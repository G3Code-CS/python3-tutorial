   # Write your logic here
   if year % 4 == 0 and (year % 400 == 0 or year % 100 != 0):
        leap = True

    return leap
