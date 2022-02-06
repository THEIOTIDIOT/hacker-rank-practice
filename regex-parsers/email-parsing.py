test1="""6
shashank <shashank@9mail.com>
shashank <shashank@gmail.9om>
shashank <shashank@gma_il.com>
shashank <shashank@mail.moc>
shashank <shashank@company-mail.com>
shashank <shashank@companymail.c_o>"""

test1="""9
vin <vineet@>
vineet <vineet@gmail.com>
vineet <vineet@gma.il.co.m>
vineet <vineet@gma-il.co-m>
vineet <vineet@gma,il.co@m>
vineet <vineet@gmail,com>
vineet <.vin@gmail.com>
vineet <vin-nii@gmail.com>
vineet <v__i_n-n_ii@gmail.com>"""

# Enter your code here. Read input from STDIN. Print output to STDOUT

import email.utils
import re

# prints all valid emails on newlines
n = int(input())
emaillist = list()
for _ in range(n):
    emailtup = email.utils.parseaddr(input())
    nameemail = email.utils.formataddr(emailtup)
    if re.match(r'^[a-z]{1}[a-z|0-9|\-|\.|_]+@[a-z]+\.[a-z]{1,3}$', emailtup[1], flags=re.I):
        emaillist.append(nameemail)

print('\n'.join(emaillist))