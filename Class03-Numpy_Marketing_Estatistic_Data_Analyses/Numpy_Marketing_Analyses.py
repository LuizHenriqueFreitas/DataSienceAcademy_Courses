# Is that a implementation of Numpy lib functions to pratice

""" =============
    CONTEXT

    That script implement a moc database content to explore some marketing
    objetctives, simulating a real life situation.

    The specific objectives will be describes below in the code.

    That script also was written using raw neovim on linux.

    There's some "debug messages" around all the code, that's happend because
    its just a study file, so, these messages are just to see the code working, 
    but is not important to generate the final graphs using matplot and seaborn
    or just o manipulate the data with numpy or pandas.
"""

""" ===================
    IMPORT LIBS
  ================== """

# numpy lib import
import numpy as np

# another libs import
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

""" seaborn and matplot will be used just to draw data graphics and 
    make it more visible to understand
"""

# define a seed to make it random but replicable again
np.random.seed(42)


""" ====================
    MOC DATA GENERATION

    Below we'll implement some code to generate a smal data base
    with informations like:
        visits -> that is basicaly how much people access the website
        user_website_time -> that has how much time the user stay on the website
        cart_itens -> that mantain how much itens exists on each user cart
        purchase_value -> that calculate purchases total sum
 ===================== """

# define users number to create moc database
users_num = 500

# generate website visits data (between 1 and 50)
visits = np.random.randint(1, 51, size = users_num)

# generate user time spend inside the website (normal distribution, correlated with visits)
# set 20 minuts of media, 5 of standard deviation, and a bonus by visit
user_website_time = np.random.normal(loc = 20, scale = 5, size = users_num) + (visits * 0.5)
# round to just 2 decimal places
user_website_time = np.round(user_website_time, 2)

# generate cart itens (depends visits and time on website)
# users who visit more and spend more time usualy buy more itens
cart_itens = np.random.randint(0, 8, size = users_num) + (visits // 10)

# make time spend on website positive influence to cart_itens count
cart_itens = (cart_itens + (user_website_time // 15)).astype(int)

# generate purchase value (correlated to cart itens)
# median iten price is R$ 35, with some random variation
purchase_value = (cart_itens * 35) + np.random.normal(loc = 0, scale = 10, size = users_num)

# if there's no itens on the cart, the value should be R$ 0
purchase_value[cart_itens == 0] = 0
# correct negative value which could spawn
purchase_value[purchase_value < 0 ] = 0
purchase_value = np.round(purchase_value, 2)

# unifield every in just one matrix (ndarray)
# each line represents one unique user, each colunm one metric
ecommerce_data = np.column_stack((visits, user_website_time, cart_itens, purchase_value))

# debug message about database creation
"""
print("\nOur data base shape:", ecommerce_data.shape)
print("\nExemple of 5 first users (lines):")
print("\nColunas: [Visits, Time on website(min), Cart Itens, Purchase Value (R$)]\n")
print(ecommerce_data[:5])
"""


""" ==============================
    ESTATISTC DESCRITIVE ANALYSES
  =============================== """

""" =============================
    DATA GRAPPER LOGIC

    Look, on that workflow, with python and numpy,
    maybe you want to get just a column from a table,
    or just a line an isolate that information to make
    some analyses with just that data.

    To separete that could you just do this:
         <create a new variable> = <you data base variable>[<line index>, <column index>]
        > remeber, python index starts on "0".
    if you want to get a entire column, with all lines, you cloud write like that:
        <new variable> = <raw data>[:, <column index>]
        > yes, ":" means you want to select all the lines, or colunms. 
        > you could use that if you try to get an entier line, with all columns.
  ============================= """

# separete columns to make code read easier
visits_col = ecommerce_data[:, 0]
time_col   = ecommerce_data[:, 1]
itens_col  = ecommerce_data[:, 2]
value_col  = ecommerce_data[:, 3]

# debug message
# print ("--- GENERAL ESTATISTC ANALYSE ---")

# media calculation
visits_madeia = np.mean(visits_col)
media_time    = np.mean(time_col)
media_itens   = np.mean(itens_col)
media_value   = np.mean(value_col)

# below has some debug messages to check data info - learning debugs
"""
print(f"Visits Media: {visits_media:.2f}")
print(f"Time on website Media: {time_media:.2f}")
print(f"Cart Itens Media: {media_itens:.2f}")
print(f"Purchase Value Media (Median Ticket): R$ {media_value:.2f}")
"""

# medium (central value, less sensive to outliers)
medium_value = np.median(value_col)
"""
print(f"\nPurchase Value Medium: R$ {medium_value:.2f}")
"""

# standard deviation (measures data spread)
std_value = np.std(value_col)
"""
print(f"Purchase Value standard davanetion: R$ {std_value:.2f}")
"""

# Max & Min Values
max_value = np.max(value_col)
# minumum just between who bouth
min_value_positive = np.min(value_col[value_col > 0])
"""
print(f"Bigger purchase value: R$ {max_value:.2f}")
print(f"Smaller purchase value (from who bouth): R$ {min_value_positive:.2f}")
"""

# ---- Graph ----
plt.figure(figsize = (12, 5))
plt.hist(value_col, bins = 30, color = 'skyblue', edgecolor = 'black', alpha = 0.7)
plt.axvline(media_value, color = 'red', linestyle = '--', linewidth = 2, label = f'Media = R$ {media_value:.2f}')
plt.axvline(medium_value, color = 'orange', linestyle = '--', linewidth = 2, label = f'Median= R$ {medium_value:.2f}')
plt.axvline(media_value + std_value, color = 'green', linestyle = ':', linewidth = 2, label = f'+1 SD = R$ {media_value + std_value:.2f}')
plt.axvline(media_value - std_value, color = 'green', linestyle = ':', linewidth = 2, label = f'-1 SD = R$ {media_value - std_value:.2f}')
plt.title('Distribution of Purchase Values')
plt.xlabel('Purchase Value (R$)')
plt.ylabel('Frequence')
plt.legend()
plt.grid(alpha = 0.3)
plt.show(block = False)


""" ===========================
  CLIENT SEGMENTATION ANALYSE
  ========================== """

# Question: "High Value" clients, what they has in common?

# boolean filter to clients how bouth > R$ 250
high_value_clients = ecommerce_data[ecommerce_data[:, 3] > 250]

""" debug messages
print("\n--- ANALYSES: HIGH VALUE CLIENT (Purchase > R$ 250) ---\n")
print("High value clients count: {high_value_clients.shape[0]}")
"""

# that scope statistcs
media_high_value_visits = np.mean(high_value_clients[:, 0])
media_high_value_time = np.mean(high_value_clients[:, 1])

""" debug messages
print(f"Those clients visit media: {media_high_value_visits:.2f}")
print(f"Thoso clients time on website media: {media_high_value_time:.2f} min")
"""

# Question: What who doesn't buy anything do on the website, how made then buy something

# filter to visiters who don't buy nothing
no_buy_visiters = ecommerce_data[ecommerce_data[:, 3] == 0]

""" debug messages
print("\n--- ANALYSE: VISITERS WHO DON'T BUY ---\n")
print(f"Number of isiters who don't buy: {no_buy_visiters.shape[0]}")
"""

# that scope statistcs
media_no_buy_visits = np.mean(no_buy_visiters[:, 0])
media_no_buy_time = np.mean(no_buy_visiters[:, 1])

""" debug messages
print(f"Those clients visits media: {media_no_buy_visits:.2f}")
print(f"Despite not buying, they stay for like: {media_no_buy_time:.2f} on the website.")
"""

# Question: Exists some correlation between time on the website and the cart itens amount?

# the np.corrcoef calculate the correlation matrix
# rowvar=false indicate columns to variables
correlation_matrix = np.corrcoef(ecommerce_data, rowvar = False)

""" debug messages
print("\n--- CORRELATION MATRIX ---\n")
print("[Visitas, Tempo, Itens, Valor]\n")
print(np.round(correlation_matrix, 2))
"""

# define variable names
var_names = ["Visits", "Time on Website", "Cart Itens", "Purchase Value"]

# convert to DataFrame to show with labels
df_correlation = pd.DataFrame(correlation_matrix, index = var_names, columns = var_names)

# Correlation Matrix (Heat Map)
plt.figure(figsize=(7 ,5))
sns.heatmap(df_correlation, annot = True, cmap = "Blues", fmt = ".2f")
plt.title("Correlation Matrix")
plt.show(block = True)
