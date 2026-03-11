def total_revenue(data):
   
    total_revenue=0
    for order in data:
        if order["status"]=='Delivered':
            total_revenue+=order['price']*order['quantity']
    print(total_revenue)

def most_sold_product(data):
    print('most sold product')
    products={}
    for order in data:
        if order['status']=='Delivered':
            if order['product'] in products:
                products[order['product']]+=order['quantity']
            else:
                products[order['product']]=order['quantity']
    print(products)
    most_sold=max(products,key=products.get) 
    print(most_sold)


def top_customer(data):
    print('top customer')
def Cancelled_orders(data):
    print('cancelled orders')
def product_revenue(data):
    print('product revenue')