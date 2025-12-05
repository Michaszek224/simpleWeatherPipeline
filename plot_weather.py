import pandas as pd
import matplotlib.pyplot as plt
from sqlalchemy import create_engine

db_string = "postgresql://user:password@localhost:5432/mydatabase"
engine = create_engine(db_string)

def generate_plot():
    query = """
        SELECT timestamp, temperature 
        FROM air_quality
        WHERE city = 'Warsaw'
        ORDER BY timestamp ASC
    """
    
    df = pd.read_sql(query, engine)
    
    if df.empty:
        print("No data available to plot.")
        return
    
    plt.figure(figsize=(10, 6))
    plt.plot(df['timestamp'], df['temperature'], marker='o', linestyle='-', color='orange', label='Temperature (°C)')
    plt.title('Temperature Over Time in Warsaw')
    plt.xlabel('Timestamp')
    plt.ylabel('Temperature (°C)')
    plt.xticks(rotation=45)
    plt.legend()
    plt.tight_layout()
    
    filename = 'temperature_plot.png'
    plt.savefig(filename)
    plt.close()
    print(f"Plot saved as {filename}")
    
if __name__ == "__main__":
    generate_plot()