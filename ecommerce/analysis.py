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
    customers={}
    for order in data:
        if order['status']=='Delivered':
            if order['customer'] in customers:
                customers[order['customer']]+=order['price']*order['quantity']
            else:
                customers[order['customer']]=order['price']*order['quantity']
    # print(customers)
    top_custmr=max(customers,key=customers.get)
    print(top_custmr)

def Cancelled_orders(data):
    print('cancelled orders')
    cancelled_orders=[]
    for order in data:
        if order['status']=='Cancelled':
            cancelled_orders.append(order)
    print(cancelled_orders)

def product_revenue(data):
    print('product revenue')



