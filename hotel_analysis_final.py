import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ✅ Connect to MySQL Database
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="sahanak",  # 🔹 Replace with your actual MySQL password
    database="hotel_analytics"
)

# ✅ Load all data from MySQL
query = "SELECT * FROM hotel_bookings1;"
df = pd.read_sql(query, conn)

print(df.head())
print(df.info())

# ✅ Close DB connection
conn.close()

# =========================
# 📊 DATA ANALYSIS SECTION
# =========================

# --- 1️⃣ Total Revenue by Hotel
revenue_df = df.groupby("hotel_name")["revenue"].sum().reset_index()
plt.figure(figsize=(7, 5))
sns.barplot(x="hotel_name", y="revenue", data=revenue_df, palette="viridis")
plt.title("Total Revenue by Hotel")
plt.xlabel("Hotel Name")
plt.ylabel("Total Revenue ($)")
plt.tight_layout()
plt.show()

# --- 2️⃣ Total Bookings vs. Cancellations by Hotel
cancel_df = df.groupby("hotel_name")["is_canceled"].agg(['count', 'sum']).reset_index()
cancel_df.columns = ["hotel_name", "total_bookings", "total_cancellations"]
plt.figure(figsize=(7, 5))
sns.barplot(x="hotel_name", y="total_bookings", data=cancel_df, color="skyblue", label="Bookings")
sns.barplot(x="hotel_name", y="total_cancellations", data=cancel_df, color="salmon", label="Cancellations")
plt.title("Bookings vs. Cancellations by Hotel")
plt.legend()
plt.tight_layout()
plt.show()

# --- 3️⃣ Average Satisfaction Score per Hotel
satisfaction_df = df.groupby("hotel_name")["satisfaction_score"].mean().reset_index()
plt.figure(figsize=(7, 5))
sns.barplot(x="hotel_name", y="satisfaction_score", data=satisfaction_df, palette="coolwarm")
plt.title("Average Satisfaction Score by Hotel")
plt.xlabel("Hotel Name")
plt.ylabel("Avg Satisfaction Score")
plt.tight_layout()
plt.show()

# --- 4️⃣ Average ADR (Room Price) per Hotel 💰
adr_df = df.groupby("hotel_name")["adr"].mean().reset_index()
plt.figure(figsize=(7, 5))
sns.barplot(x="hotel_name", y="adr", data=adr_df, palette="crest")
plt.title("Average ADR (Room Price) by Hotel")
plt.xlabel("Hotel Name")
plt.ylabel("Average Daily Rate (ADR)")
plt.tight_layout()
plt.show()

# --- 5️⃣ Relationship Between ADR (Price) and Satisfaction
plt.figure(figsize=(7, 5))
sns.scatterplot(x="adr", y="satisfaction_score", hue="hotel_name", data=df, palette="tab10")
plt.title("ADR vs Satisfaction Score by Hotel")
plt.xlabel("Average Daily Rate (ADR)")
plt.ylabel("Satisfaction Score")
plt.tight_layout()
plt.show()

print("\n✅ Analysis complete! All 5 visualizations displayed successfully.")
