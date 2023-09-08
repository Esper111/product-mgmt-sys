def disc(rate, per):
    return (rate*per/100)

def tot(quantity,t,price):
    quantity=int(quantity)
    t=float(t)
    price=float(price)
    return t+(quantity*price)

def disc1(q,rate, per):
    q=int(q)
    rate=float(rate)
    per=float(per)
    return (q*rate*per/100)

def tx(total):
    total=float(total)
    return (0.14*total)

def amt(totalamt,disamt):
    totalamt=float(totalamt)
    disamt=float(disamt)
    tax=tx(totalamt)
    return (totalamt-disamt+tax)
 
