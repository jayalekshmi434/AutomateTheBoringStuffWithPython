    
import pyperclip , re 
phoneRegex= re.compile(r'''(
    (\d{3}|\(\d{3}\))?  #area code
    (\s|-|\.)?          #separator
    (\d{3})            #first 3 digits
    (\s|-|\.)           #separator
    (\d{4})            #last 4 digits
    (\s*(ext|x|ext.)\s*)?
    (\d{2,5})? #extension
    ) ''',re.VERBOSE)
            
       
emailRegex=re.compile(r'''(
    [A-Za-z0-9._+-]+      #username
    @                       # at the rate of
    [A-Za-z0-9.-]+          #domain name
    (\.[A-Za-z]{2,4})       #dot-com
    )''',re.VERBOSE)

#get the text from clipboard

text=str(pyperclip.paste())
matches=[]

for groups in phoneRegex.findall(text):
    phoneNum='-'.join([groups[1],groups[3],groups[5]])
    if groups[8] != '':
        phoneNum+= ' x'+groups[8]
    matches.append(phoneNum)

for groups in emailRegex.findall(text):
    matches.append(groups[0])
    
# copy results to the clipboard
if len(matches)>0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clip board)')
    print('\n'.join(matches))
else:
    print('No phone numbers or emails to match')
        