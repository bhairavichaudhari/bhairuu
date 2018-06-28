def word_count(str):
        count=dict()
        w=str.split()
        print(w)
        for a in w:
                if a in count:
                    count[a]+=1
                else:
                    count[a]=1
        return count
c=word_count('we we are are in sql lab lab')
print(c)
