""" This file is a little projetc to pratice python code sintax
    using some frameworks like pandas, numpy, matplotlib and seaborn.
    I'm doing this by a free web course from "Data Science Academy".
    Written usingo raw neovim IDE and learning these shortcuts and workflow.
    I'm pratice my englis too :) maybe you find some strange words.
"""

# About this specific script
""" Is the porpuse: an E-commer where they doens't can get the data informtion
    and use this for strategic decisions. The objectve of this code is exctly
    get all the data information and concentrate with visual and usefull graphics.
    Is that, i supose, for maximize sales and strategic marketing campains and
    promotions/ discounts.

    Is that a important resource for any sales commerce, the data to take 
    important decisions on right time.
"""

""" ===========================
              IMPORTS
    ========================= """

# For python development it's always a good pratice mantain the packages version

""" That create a markdonw with packages version on that project
    the code below shows how you can automtcaly install pandas v2.3.1 by code
    Exemple code: !pip install -q pandas==2.3.1

    this code run and update quietly the packages needed
    > !pip install -q -U watermark
    The line above is important if that code is written to a virtual notebook
    enviroment, like jupterNotebook, very popular on DataScience prototypes.
"""

# we'll use pandas to manipulate data tables
import pandas as pd

# numpy is important to implement aritmatich operations with arrays
import numpy as np

# Matplotlib will be used to generate graphcs
import matplotlib.pyplot as plt

# Seaborn is good to statistic data visualization
import seaborn as sns

# random can generate ramdom values to our study here
import random

# import just "datetime" and "timedelta" classes to temporal data manipulation
from datetime import datetime, timedelta

""" =========================
    PREPARING THE ENVIROMENT
    ====================== """

# below there's a function to generate fictional data
""" Working in Data Analyses, and outher data stuff jobs you will usually take
    data from the IT departament, from a SQL query or just a .csv file exported
    from exel or any spreadsheet software.
"""

# function declaration with standart parameter equals 600, can be changed when called
def dsa_fictional_data_generate(num_records = 600):

    # generate a fictional sales data DataFrame from Pandas, a DataFrame is like a table

    # initial message indicates how much records will be generated
    print(f"\nStart generation of {num_records} sales records...")

    
    """ Below will be generated the root data dictionaries.
        Look how the products dictionary uses nest dictionaries
        inside him. Is that like use an array of classes whitch
        arrays inside than
    """
    # products dictionary, with categories and prices (BRL was used)
    products = {
        'Gamer LapTop': {'category': 'Eletronic', 'price': 7500.00},
        'Vertical Mouse': {'category': 'Acessory', 'price': 250.00},
        'Mechanic Keyboard': {'category': 'Acessory', 'price': 550.00},
        'Ultrawide Screen': {'category': 'Eletronic', 'price': 2800.00},
        'Gamer Chair': {'category': 'Forniture', 'price': 1200.00},
        'Headset 7.1': {'category': 'Acessory', 'price': 800.00},
        'Graphics Card': {'category': 'Hardware', 'price': 4500.00},
        'Mechanic Keyboard': {'category': 'Hardware', 'price': 600.00}
    }

    # creates a list just with product names
    products_list = list(products.keys())

    # dictionary with cities and their states (Brazilian Cities)
    cities_states = {
        'São Paulo': 'SP', 'Rio de Janeiro': 'RJ', 'Belo Horizonte': 'MG',
        'Porto Alegre': 'RS', 'Salvador': 'BA', 'Curitiba': 'PR', 'Fortaleza': 'CE'
    }

    # create a list just with cities name
    cities_list = list(cities_states.keys())

    # creat a empty list how will keep sale record
    sale_data = []

    # define the start orders date
    start_date = datetime(2026, 1, 1)

    # this loop generate all the sale records
    for i in range(num_records):
        
        # select a random product
        product_name = random.choice(products_list)

        # select a random city
        city = random.choice(cities_list)

        # generate an amount of sold products, between 1 and 7
        amount = np.random.randint(1, 8)

        # calculate order date from very first order
        order_date = start_date + timedelta(days = int(i/5), hours = random.randint(0, 23))

        # if the product was a mouse or a keybord, need to apply a random discount until 10%
        if product_name in ['Vertical Mouse', 'Mechanic Keyboard']:
            unit_price = products[product_name]['price'] * np.random.uniform(0.9, 1.0)
        else:
            unit_price = products[product_name]['price']

        # add a sale record to the list
        sale_data.append({
            'order_ID': 1000 + i,
            'order_date': order_date,
            'product_name': product_name,
            'category': products[product_name]['category'],
            'unit_price': round(unit_price, 2),
            'amount': amount,
            'cliente_ID': np.random.randint(100, 150),
            'city': city,
            'state': cities_states[city]
        })

    # final message show when finished generation DataFrame
    print("Data generation is complete!\n")

    # return the data on DataFrame format
    return pd.DataFrame(sale_data)


""" ===========================
        INFORMATION TIME
   ======================== """

""" There's so important, after you get the data pack,
    here we are usign the dsa_fictional_data_generate() function,
    but, SQL querys, csv files, anyway, is important you explore
    you data, seraching for strange things there.
    
    Some important metods of DateFrame to do this are:
    DateFrame.shape()       -> show (colunms / lines) of the DataFrame
    DateFrame.head()        -> show first 5 lanes
    DateFrame.tail()        -> show last 5 lanes
    DateFrame.info()        -> show DataFrame information, like data types, not null colunms
    DateFrame.describe()    -> DataFrame statistic resumo
    DataFrame.dtypes        -> data types
"""

# Explore your data is a lot more relevant when you use real and unkow data


""" ======================
      DATA TREATMENT
   =================== """

""" Just as important as explore the data base, is too necessary
    clean the data information, before analyse.
"""

# create a DataFrame using our function, override the 600 amount preset
df_sales = dsa_fictional_data_generate(500)

# verify the type of 'order_date' column - convert the colunm time if was worng.
# it's important be on datetime data type to be used at temporal analyses.
# that kind of validation should be implemented to outher data types too.
df_sales['order_date'] = pd.to_datetime(df_sales['order_date'])

# attributs engeneering - creating 'invoicing' column (price x amount)
df_sales['invoicing'] = df_sales['unit_price'] * df_sales['amount']

# attributs engeneering - creating a delivery status column using a lambda expression
df_sales['delivery_status'] = df_sales['state'].apply(lambda state: 'Fast' if state in ['SP', 'RJ', 'MG'] else 'Regular')


""" ============================
        TOP 10 BEST SELLERS
   ============================ """

# group by product name, sum amount and sort by most sold
top_10_products = df_sales.groupby('product_name')['amount'].sum().sort_values(ascending = False).head(10)

# show results
top_10_products

# define graphic style using using seaborn
sns.set_style("whitegrid")

# always when is "plt.<something>" -> is that a call to matplotlib, because we called as plt

# create axes and figure
plt.figure(figsize = (12, 7))

# create horizontal bars graphic
top_10_products.sort_values(ascending = True).plot(kind = 'barh', color = 'skyblue')

# add titles and labels
plt.title('Top 10 Product Best Seller', fontsize = 16)
plt.xlabel('Sold Amount', fontsize = 12)
plt.ylabel('Product', fontsize = 12)

# show graph
plt.tight_layout()
plt.show(block = False)


""" ===========================
      MONTHLY INVOICING
    ======================= """

# creates a 'month' column to make it easier
df_sales['month'] = df_sales['order_date'].dt.to_period('M')

# group monthly invoicing sum
monthly_invoicing = df_sales.groupby('month')['invoicing'].sum()

# convert index to string to better print on the graph
monthly_invoicing.index = monthly_invoicing.index.strftime('%Y-%m')

# format to just 2 decimal slots
monthly_invoicing.map('R${:,.2f}'.format)

# create a figure
plt.figure(figsize = (12, 6))

# print line graph of monthly invoicing
monthly_invoicing.plot(kind = 'line', marker = 'o', linestyle = '-', color = 'green')

# title and labels definition
plt.title('Month Invoice Evolution', fontsize = 16)
plt.xlabel('Month', fontsize = 12)
plt.ylabel('Invoicing (R$)', fontsize = 12)

# rotate 45º the xlabel
plt.xticks(rotation = 45)

# add a grid with traced strait lines
plt.grid(True, which = 'both', linestyle = '--', linewidth = 0.5)

# automatic ajust to avoid overlap
plt.tight_layout()

# show graph
plt.show(block = False)


""" =======================
        SALES BY STATE
   ==================== """

# group by state
state_sales = df_sales.groupby('state')['invoicing'].sum().sort_values(ascending =  False)

# format to just 2 slots
state_sales.map('R${:,.2f}'.format)

# create another figure
plt.figure(figsize = (12, 7))

# print bars graph using color palette from seaborn
state_sales.plot(kind = 'bar', color = sns.color_palette("husl", 7))

# title and labels formatation
plt.title('State Invoicing', fontsize = 16)
plt.xlabel('State', fontsize = 12)
plt.ylabel('Invoicing (R$)', fontsize = 12)

# maintain x albels on horizontal
plt.xticks(rotation = 0)

# show graph
plt.tight_layout()
plt.show(block = False)


""" ===============================
        INVOICING BY CATEGORY
   ============================ """

# group by category and sum the invoicing
category_invoicing = df_sales.groupby('category')['invoicing'].sum().sort_values(ascending = False)

# format to BRL
category_invoicing.map('R${:,.2f}'.format)

# import FuncFormater to format axes (probably just UI)
from matplotlib.ticker import FuncFormatter

# sort the data, it's easier to read
sorted_invoicing = category_invoicing.sort_values(ascending = False)

# creating a graph with high controll lever
fig, ax = plt.subplots(figsize = (12, 7))

# graph number formatation
def thousands_format(y, pos):
    
    # format the value to thousands(K) with "R$"
    return f'R$ {y/1000:,.0f}K'

# instanciate the formater object
formatter = FuncFormatter(thousands_format)

# apply Y axis formatation (ax.yaxis)
ax.yaxis.set_major_formatter(formatter)

# print dara using the 'ax' object
sorted_invoicing.plot(kind = 'bar', ax = ax, color = sns.color_palette("viridis", len(sorted_invoicing)))

# final graph configs - title, labels, etc
ax.set_title('Category Invoicing', fontsize = 16)
ax.set_xlabel('Category', fontsize = 12)
ax.set_ylabel('Invoicing', fontsize = 12)

plt.xticks(rotation = 45, ha = 'right')

# show graph
plt.tight_layout()
plt.show(block = True)

""" Is that the end of the very first project from DSA academy i made.
    was interesting, i spend maybe 3 ~ 4 hours coping the code from the class manualy
    and it's a little incovenient use raw neovim, witouh auto completo or copy paste
    shortcuts. But it was fun.

    Onestly i was expecting something more complete and usefull like a dashbord aplication.
    But still beeing a cool aplication.
"""
