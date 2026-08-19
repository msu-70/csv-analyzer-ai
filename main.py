import pandas as pd

data=pd.read_csv('sales.csv')


def main():
    print("1.What is the total sales?\n2.What are the total sales by region?\n3.What are the top 5 products?\n4.What is the average sales per region?\n5.What was the monthly sold trend?\n")
    reply=input("What do you want to check? :")
    if reply=='1':
        Total_Sales()
    elif reply=='2':
        Region_Sales()
    elif reply=='3':
        Top_Products()
    elif reply=='4':
        Avrg_Sale()
    elif reply=='5':
        Sale_Trend()
#
def Total_Sales():
    total=data['Sales'].sum()
    print("Total Sales =",total)

def Region_Sales():
    region=data.groupby('Region' ,as_index=False)['Sales'].sum()
    print(region)

def Top_Products():
    order=data.value_counts('Product')
    print(order)

def Avrg_Sale():
    sale=data.groupby('Region')['Sales'].mean()
    print(sale)

def Sale_Trend():
    data['Date']=pd.to_datetime(data['Date'])
    trend=data.groupby(data['Date'].dt.month)['Product'].value_counts()
    print(trend)

main()