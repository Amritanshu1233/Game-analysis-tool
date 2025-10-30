import pandas as pd
import matplotlib.pyplot as plt

# --- 0. Load and Prep Data ---
try:
    df = pd.read_csv('vgsales.csv')
    
    # Drop rows with missing values to avoid errors in analysis
    df = df.dropna()

except FileNotFoundError:
    print("Error: 'vgsales.csv' not found.")
    exit()
except Exception as e:
    print(f"An error occurred: {e}")
    exit()


# --- 1. Analysis: Which platform has the most sales of all time? ---
print("\n--- Top Platforms by Global Sales ---")
platform_sales = df.groupby('Platform')['Global_Sales'].sum().sort_values(ascending=False)
print(platform_sales.head(10)) # Print top 10

# Create Bar Chart for Top Platforms
plt.figure(figsize=(12, 7)) # Set the figure size
top_10_platforms = platform_sales.head(10)
top_10_platforms.plot(kind='bar', color='steelblue')
plt.title('Top 10 Platforms by Global Sales (in Millions)')
plt.ylabel('Global Sales (in Millions)')
plt.xlabel('Platform')
plt.xticks(rotation=45)
plt.tight_layout() # Adjust layout to prevent labels from overlapping
plt.savefig('top_platforms.png') # Save the chart as an image file
print("Chart 'top_platforms.png' saved!")


# --- 2. Analysis: What are the top 5 most popular genres? ---
print("\n--- Top 5 Genres by Global Sales ---")
genre_sales = df.groupby('Genre')['Global_Sales'].sum().sort_values(ascending=False)
print(genre_sales.head(5))

# Create Pie Chart for Top 5 Genres
plt.figure(figsize=(10, 8))
top_5_genres = genre_sales.head(5)
plt.pie(top_5_genres, labels=top_5_genres.index, autopct='%1.1f%%', startangle=140)
plt.title('Market Share of Top 5 Game Genres by Global Sales')
plt.axis('equal') # Equal aspect ratio ensures that pie is drawn as a circle.
plt.savefig('top_genres_pie.png')
print("Chart 'top_genres_pie.png' saved!")


# --- 3. Analysis: Which publisher has been the most successful? ---
print("\n--- Top 10 Publishers by Global Sales ---")
publisher_sales = df.groupby('Publisher')['Global_Sales'].sum().sort_values(ascending=False)
print(publisher_sales.head(10))
# (We'll use the platform and genre charts for the post, so no new chart here is fine)


# --- 4. Analysis: How do sales compare across regions? ---
print("\n--- Total Sales by Region ---")
regional_sales = {
    'North America': df['NA_Sales'].sum(),
    'Europe': df['EU_Sales'].sum(),
    'Japan': df['JP_Sales'].sum(),
    'Other': df['Other_Sales'].sum()
}
print(regional_sales)

# Create Bar Chart for Regional Sales
plt.figure(figsize=(10, 6))
regions = list(regional_sales.keys())
sales = list(regional_sales.values())
plt.bar(regions, sales, color=['#FF5733', '#33FF57', '#3357FF', '#FF33A1'])
plt.title('Total Video Game Sales by Region (in Millions)')
plt.ylabel('Sales (in Millions)')
plt.xlabel('Region')
plt.savefig('regional_sales.png')
print("Chart 'regional_sales.png' saved!")

# --- 5. Analysis: What are the "Trending" Games? (Top 10 from a Recent, Data-Rich Year like 2024) ---
print("\n--- Top 10 'Trending' Games (Best Sellers from a recent, data-rich year like 2024) ---")

# The dataset is sparse for 2017+, so let's pick a strong recent year like 2024.
# If you want a different year, change 'target_year'.
target_year = 2016 
print(f"Analyzing top games from the year: {target_year}")

# Filter the DataFrame to only include games from the target_year
recent_games_df = df[df['Year'] == target_year].copy() # Use .copy() to avoid SettingWithCopyWarning

if not recent_games_df.empty:
    # Get the top 10 best-selling games from that year
    # We group by 'Name' just in case a game was on multiple platforms
    top_10_recent_games = recent_games_df.groupby('Name')['Global_Sales'].sum().sort_values(ascending=False).head(10)

    print(top_10_recent_games)

    # Create a Horizontal Bar Chart (better for long game names)
    plt.figure(figsize=(12, 8))
    # Plot 'ascending' so the #1 game is at the top
    top_10_recent_games.sort_values(ascending=True).plot(kind='barh', color='seagreen')
    plt.title(f'Top 10 Best-Selling Games of 2024')
    plt.xlabel('Global Sales (in Millions)')
    plt.ylabel('Game Title')
    plt.tight_layout()
    plt.savefig('top_trending_games_2024.png') # Changed filename for clarity
    print(f"Chart 'top_trending_games_2024.png' saved!")
else:
    print(f"No data available for the year {target_year} to determine trending games.")


print("\n\n--- ALL ANALYSIS COMPLETE ---")