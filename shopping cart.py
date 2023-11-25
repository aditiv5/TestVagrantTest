def discount(price,quantity):
    amount = quantity * price
    if price >= 500 :
        discount = 0.05 * amount
        total = amount- discount
        return total
    else:
        return amount
def gst(amount,gst):
    gst = amount * float(gst/100)

    return gst

product = [["Leather wallet",1100,18,1],["Umbrella",900,12,4],["cigarette",200,28,3],["Honey",100,0,2]]
length = len(product)
final_price = []
max_gst = []
final_amount = []
for i in range(length):
    #for j in range(i+1):
    result1 = discount(product[i][1],product[i][3])
    result2 = gst(result1,product[i][2])
    final_price1 = result1 + result2
    final_amount.append(final_price1)
    max_gst.append(result2)
print("Total amount to be paid to shop-keeper:",sum(final_amount))
print("Maximim GST amount: ",max(max_gst),"for the product",product[1][0])