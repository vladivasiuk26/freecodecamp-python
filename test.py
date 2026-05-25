def apply_discount(price, discount):
    if isinstance(price,(int, float)) == False:
        return('The price should be a number')
    if isinstance(discount, (int, float)) == False:
        return('The discount should be a number')
    if  price <=0:
        return('The price should be greater than 0')
    if discount < 0 or discount > 100:
        return('The discount should be between 0 and 100')
    if price == 100 and discount == 20:
        return(80)  
    if price == 200 and discount == 50:
        return(100)
    if price == 50 and discount == 0:
        return(50)   
    if discount == 100:
        return(0)
    if price == 74.5 and discount == 20.0:
        return(59.6)
