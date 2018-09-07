def nextpower_2 (p):
        value = 1
        while (value <= p):
        	value = value << 1
        return value
p=int(input())
print (nextpower_2(p))
