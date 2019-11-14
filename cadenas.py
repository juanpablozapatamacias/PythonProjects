from collections import OrderedDict

def reverse(s):
    if s == None or len(s)<=1:
         print (s)
    else:
        st = list(s)
        st.reverse()
        print (st)

def lastString(s):
    x=s.split()
    count = len(x[len(x) - 1])
    print(count)

def strStr(haystack,needle):
    if haystack == None or needle == None:
        return 0

    if len(needle) == 0:
        return 0

    i=0

    while i <= len(haystack) - len(needle):
        if haystack[i:i+len(needle)] == needle:
            return i
        
        i+=1

    return -1

def countAndSay(n):
    if n==1:
        return "1"
    if n==2:
        return "11"

    s="11"
    for i in range(3,n+1):
        s+='$'
        l = len (s)

        cnt = 1
        tmp = ""

        for j in range (1,l):
            if s[j] != s[j-1]:
                tmp += str(cnt + 0)
                tmp += s[j-1]
                cnt = 1
            else:
                cnt += 1
        
        s = tmp
    
    return s

def compress(C):
    n = len(C)
    tmp=""

    for i in range (n):
        count = 1
        while i<n-1 and C[i]==C[i+1]:
            count +=1
            i+=1
        
        tmp += str(C[i])
        tmp += str(count)

    print(tmp)
    return len(tmp)

def kangaroo(x1,v1,x2,v2):
    while(x1<=x2):
        if x1 == x2:
            return "YES"

        x1+=v1
        x2+=v2

    return "NO"

reverse("Hellow")
lastString("Hola mundo      ")

print(strStr("Hellow", "ll"))

print(countAndSay(6))

c = list()
c=['w','w','w','a','a','d','e']
print(compress(c))

print (kangaroo(0,3,4,2))