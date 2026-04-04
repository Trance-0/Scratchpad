class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        # simulation, just read the characters in the right order
        n=len(encodedText)
        if n==0:
            return ''
        cols=n//rows
        grid=[encodedText[i*cols:(i+1)*cols] for i in range(rows)]
        cn=0
        for r in encodedText:
            if r!=' ':
                cn+=1
        res=''
        s=0
        cr='a'
        c=0
        while c<cn:
            a,b=0,s
            cr=''
            while a<rows and b<cols:
                cr+=grid[a][b]
                if grid[a][b]!=' ':
                    c+=1
                a+=1
                b+=1
            s+=1
            res+=cr
            print(res,cr)
        return res.rstrip()
