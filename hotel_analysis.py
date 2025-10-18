import mysql.connector
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="sahanak",  
    database="hotel_analytics"
)


query = "SELECT * FROM hotel_bookings1;"
df = pd.read_sql(query, conn)


print(df.head())
print(df.info())


revenue_data = df.groupby('hotel_name')['revenue'].sum().reset_index()

sns.barplot(x='hotel_name', y='revenue', data=revenue_data)
plt.title("Total Revenue per Hotel")
plt.xlabel("Hotel")
plt.ylabel("Revenue")
plt.show()


satisfaction_data = df.groupby('hotel_name')['satisfaction_score'].mean().reset_index()

sns.barplot(x='hotel_name', y='satisfaction_score', data=satisfaction_data)
plt.title("Average Satisfaction by Hotel")
plt.xlabel("Hotel")
plt.ylabel("Average Satisfaction")
plt.show()


conn.close()

