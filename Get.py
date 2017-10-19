import re

email = 'zhixing.wang@ttu.edu' #raw_input("Type in your email, CVP\n")
regex = re.match(r'^([\w\.]+)\@(\w+)\.(\w+)$',email)

if  regex :
   print email+' is a email'
else:
   print 'None'

if regex :
   Name = regex.group(1).split('.')
   FirstName = Name[0]
   LastName = Name [1]

   print 'FirstName: ' + FirstName
   print 'LastName:  ' + LastName

