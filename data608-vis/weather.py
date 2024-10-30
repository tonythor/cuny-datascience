import pandas as pd
import requests
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.ticker import MultipleLocator
import seaborn as sns
import matplotlib.pyplot as plt
import geopandas as gpd
import numpy as np
import cartopy.crs as ccrs
import cartopy.feature as cfeature
from scipy import stats

# URLs for datasets
HURDAT2_URL = "https://www.nhc.noaa.gov/data/hurdat/hurdat2-1851-2023-051124.txt"
GISTEMP_URL = "https://data.giss.nasa.gov/gistemp/graphs/graph_data/Global_Mean_Estimates_based_on_Land_and_Ocean_Data/graph.txt"

# Load the NASA GISTEMP dataset
def load_gistemp_data(url=GISTEMP_URL):
    # Read the data, skipping the header lines
    df = pd.read_csv(url, sep='\s+', skiprows=5)  # Adjusted as per deprecation warning
    df.columns = ['Year', 'No_Smoothing', 'Lowess_5']  # Rename columns
    return df

# Load the HURDAT2 hurricane dataset
def load_hurdat2_data(url=HURDAT2_URL):
    # Fetch and read the dataset
    response = requests.get(url)
    data = response.text.splitlines()
    
    # Parse the data
    rows = []
    current_storm_id = None
    current_storm_name = None
    
    for line in data:
        parts = [p.strip() for p in line.split(',')]
        
        # Header lines start with AL (Atlantic) followed by numbers
        if parts[0].startswith('AL'):
            current_storm_id = parts[0]
            current_storm_name = parts[1].strip()  # The name is in the second part
            # Skip the rest of this iteration as it's just a header
            continue
            
        # If it's not a header line, it's a data line
        if len(parts) > 7:  # Data lines have many columns
            try:
                max_winds = float(parts[6]) if parts[6].strip() != '-999' else None
                min_pressure = float(parts[7]) if parts[7].strip() != '-999' else None
            except ValueError:
                max_winds = None
                min_pressure = None
                
            rows.append({
                "storm_id": current_storm_id,
                "storm_name": current_storm_name,
                "date": parts[0].strip(),
                "time": parts[1].strip(),
                "record_identifier": parts[2].strip(),
                "status": parts[3].strip(),
                "latitude": parts[4].strip(),
                "longitude": parts[5].strip(),
                "max_winds": max_winds,
                "min_pressure": min_pressure
            })
    
    # Load into a DataFrame
    df = pd.DataFrame(rows)
    
    # Convert datetime and create year column
    df['datetime'] = pd.to_datetime(df['date'] + df['time'], format='%Y%m%d%H%M', errors='coerce')
    df = df.dropna(subset=['datetime'])
    df['year'] = df['datetime'].dt.year
    
    # Define category based on max_winds (Saffir-Simpson scale)
    df['category'] = df['max_winds'].apply(lambda x: (
        0 if pd.isna(x) or x < 34 else  # Tropical Depression
        1 if x <= 63 else  # Tropical Storm
        2 if x <= 82 else  # Category 1
        3 if x <= 95 else  # Category 2
        4 if x <= 112 else  # Category 3
        5 if x <= 136 else  # Category 4
        6  # Category 5
    ))
    
    return df

def major_hurricanes() -> pd.DataFrame:
    hurdat2_df = load_hurdat2_data()
    major_hurricanes = hurdat2_df[
        (hurdat2_df['category'].isin([4, 5])) &
        (hurdat2_df['storm_name'].notna()) &
        (hurdat2_df['storm_name'].str.strip() != '')
    ].copy()

    # Group by storm to get unique hurricanes
    unique_major_hurricanes = major_hurricanes.groupby(['storm_name', 'year']).agg({
        'category': 'max',
        'max_winds': 'max',
        'min_pressure': 'min',
        'date': 'first'
    }).reset_index()

    # Sort by year and name
    unique_major_hurricanes = unique_major_hurricanes.sort_values(['year', 'storm_name'])

    # Show results
    # print("Sample of Cat 4-5 hurricanes:")
    # print(unique_major_hurricanes.head(10))
    #print("\nTotal number of Cat 4-5 hurricanes:", len(unique_major_hurricanes))

    # Also show some summary stats
    # print("\nDistribution by category:")
    return unique_major_hurricanes


def prepare_combined_analysis(hurdat2_df, gistemp_df):
    # Annual hurricane statistics focusing on dangerous storms
    hurricane_stats = hurdat2_df.groupby('year').agg({
        'max_winds': 'mean',
        'category': lambda x: sum(x >= 4)  # Count Category 4-5 hurricanes
    }).reset_index()
    
    # Merge with temperature data
    combined_df = pd.merge(
        hurricane_stats,
        gistemp_df[['Year', 'No_Smoothing']],
        left_on='year',
        right_on='Year',
        how='inner'
    )
    
    return combined_df.rename(columns={
        'No_Smoothing': 'Temperature Anomaly (°C)',
        'category': 'Category 4-5 Hurricanes'
    })

# # Load the data and confirm
# hurdat2_df = load_hurdat2_data()
# print(hurdat2_df.head())  # Check the output to ensure it’s working

def plot_hurricane_categories():
    # Create data for hurricane categories
    categories = pd.DataFrame({
        'Category': [1, 2, 3, 4, 5],
        'Wind Speed (knots)': [74, 96, 111, 130, 157],
        'Damage Level': ['Some Damage', 'Extensive Damage', 
                        'Devastating Damage', 'Devastating Damage',
                        'Catastrophic Damage']
    })
    
    # Create color palette from yellow to red
    colors = ['#FFE5B4', '#FFB347', '#FF8C00', '#FF4500', '#8B0000']
    
    # Create figure
    plt.figure(figsize=(10, 6))
    
    # Create bar plot
    ax = sns.barplot(
        data=categories,
        x='Category',
        y='Wind Speed (knots)',
        palette=colors
    )
    
    # Add damage level annotations
    for i, row in categories.iterrows():
        plt.text(i, row['Wind Speed (knots)'] + 5, 
                row['Damage Level'],
                ha='center', fontsize=9)
    
    # Customize the plot
    plt.title('Hurricane Category and Wind Speed with Damage Potential', 
             pad=20, fontsize=14)
    plt.xlabel('Hurricane Category', fontsize=12)
    plt.ylabel('Wind Speed (knots)', fontsize=12)
    
    # Add gridlines
    plt.grid(True, axis='y', linestyle='--', alpha=0.7)
    
    # Adjust layout
    plt.tight_layout()
    
    return plt, colors

def plot_recent_hurricanes(majors_df, n_hurricanes=10, colors=None):
    # Get the most recent hurricanes
    recent = majors_df.tail(n_hurricanes)
    
    # Create figure
    plt.figure(figsize=(10, 6))
    
    # Create names with years for x-axis
    recent['display_name'] = recent.apply(
        lambda x: f"{x['storm_name']}\n({x['year']})", axis=1)
    
    # Create bar plot
    ax = sns.barplot(
        data=recent,
        x='display_name',
        y='max_winds',
        palette=colors[-2:]  # Use the two most intense colors for Category 5
    )
    
    # Customize the plot
    plt.title('Recent Category 4 and 5 Hurricanes\n(2021-2023)', 
             pad=20, fontsize=14)
    plt.xlabel('Hurricane Name', fontsize=12)
    plt.ylabel('Maximum Wind Speed (mph)', fontsize=12)
    
    # Add wind speed values on top of each bar
    for i, v in enumerate(recent['max_winds']):
        ax.text(i, v + 1, f'{int(v)}', ha='center', fontsize=10)
    
    # Rotate x-axis labels slightly for better readability
    plt.xticks(rotation=0)
    
    # Add gridlines
    plt.grid(True, axis='y', linestyle='--', alpha=0.7)
    
    # Adjust layout
    plt.tight_layout()
    
    return plt

# Example usage:
# majors = major_hurricanes()
# plt1, colors = plot_hurricane_categories()
# plt1.show()
# plt2 = plot_recent_hurricanes(majors, colors=colors)
# plt2.show()

def plot_temp_hurricane_trends(gistemp_df, major_hurricanes_df, start_year=1980):
    # Set style
    plt.style.use('seaborn-v0_8-whitegrid')
    
    # Prepare temperature data
    temp_data = gistemp_df[gistemp_df['Year'] >= start_year].copy()
    
    # Prepare hurricane data
    hurricane_counts = major_hurricanes_df[
        major_hurricanes_df['year'] >= start_year
    ]['year'].value_counts().sort_index()
    
    # Calculate 5-year moving average of hurricane counts
    hurricane_ma = hurricane_counts.rolling(window=5, center=True).mean()
    
    # Create figure with dual axes
    fig, ax1 = plt.subplots(figsize=(15, 7))
    
    # Customize grid
    ax1.grid(True, color='#E6E6E6', linestyle='-', linewidth=0.5)
    ax1.set_axisbelow(True)
    
    # Plot temperature anomaly
    ax1.set_xlabel('Year', fontsize=10, labelpad=10)
    ax1.set_ylabel('Temperature Anomaly (°C)', color='#FF7F50', fontsize=10)
    line1 = ax1.plot(temp_data['Year'], temp_data['No_Smoothing'], 
                     color='#FF7F50', linewidth=1.5, label='Temperature Anomaly')
    ax1.tick_params(axis='y', labelcolor='#FF7F50')
    
    # Create second y-axis for hurricane frequency
    ax2 = ax1.twinx()
    ax2.set_ylabel('Number of Category 4-5 Hurricanes', color='#4169E1', fontsize=10)
    
    # Scale the hurricane data to match the right axis range
    scale_factor = 100/8  # Assuming max of about 8 hurricanes
    scaled_ma = hurricane_ma * scale_factor
    scaled_counts = hurricane_counts * scale_factor
    
    # Plot hurricane moving average
    line2 = ax2.plot(hurricane_ma.index, scaled_ma.values, 
                     color='#4169E1', linewidth=1.5, 
                     label='5-year Moving Average of Cat 4-5 Hurricanes')
    
    # Plot individual year hurricane counts as scatter
    scatter = ax2.scatter(hurricane_counts.index, scaled_counts.values, 
                         color='#4169E1', alpha=0.3, s=20)
    
    # Customize y-axis ticks for hurricanes
    ax2.yaxis.set_major_locator(MultipleLocator(20))
    ax2.set_ylim(0, 100)
    
    # Make right y-axis labels show actual hurricane counts (not scaled)
    ax2.set_yticklabels([f'{int(x/scale_factor)}' for x in ax2.get_yticks()])
    ax2.tick_params(axis='y', labelcolor='#4169E1')
    
    # Set title
    plt.title('Global Temperature Anomaly and Major Hurricane Frequency\n1980-2023', 
              pad=20, fontsize=12)
    
    # Combine legends with custom style
    lines = line1 + line2
    labels = [l.get_label() for l in lines]
    ax1.legend(lines, labels, loc='upper left', frameon=True, 
              facecolor='white', edgecolor='none')
    
    # Set axis limits
    ax1.set_ylim(0, 1.2)
    ax1.set_xlim(1980, 2023)
    
    # Set x-axis ticks every 10 years
    ax1.xaxis.set_major_locator(MultipleLocator(10))
    
    # Remove top spines
    ax1.spines['top'].set_visible(False)
    ax2.spines['top'].set_visible(False)
    
    # Adjust layout
    plt.tight_layout()
    
    return plt

def plot_temperature_anomaly(gistemp_df):
    # Create figure and axis with specific size ratio
    fig, ax = plt.subplots(figsize=(12, 8))
    
    # Set style
    plt.style.use('seaborn-v0_8-whitegrid')
    
    # Plot both lines
    ax.plot(gistemp_df['Year'], gistemp_df['No_Smoothing'], 
            color='#4169E1', label='Actual Temperature Readings', linewidth=1)
    ax.plot(gistemp_df['Year'], gistemp_df['Lowess_5'], 
            color='#FF0000', label='Smoothed Trend Line', linewidth=1.5)
    
    # Customize grid
    ax.grid(True, color='#E6E6E6', linestyle='-', linewidth=0.5)
    ax.set_axisbelow(True)
    
    # Add horizontal line at y=0
    ax.axhline(y=0, color='gray', linestyle='--', linewidth=0.5, alpha=0.5)
    
    # Set title and labels
    plt.title("Earth's Temperature Change Over Time\n(Difference from Historical Average)", 
              pad=20, fontsize=12)
    plt.xlabel('Year', fontsize=10, labelpad=10)
    plt.ylabel('Temperature Difference (°C)\nPositive = Warmer, Negative = Cooler', fontsize=10)
    
    # Customize y-axis
    ax.set_ylim(-0.5, 1.25)
    ax.yaxis.set_major_locator(MultipleLocator(0.25))
    
    # Customize x-axis
    ax.set_xlim(1880, 2023)
    ax.xaxis.set_major_locator(MultipleLocator(20))
    
    # Customize legend
    plt.legend(loc='upper left',
              frameon=True,
              facecolor='white',
              edgecolor='none')
    
    # Remove top and right spines
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    
    # Make left and bottom spines gray
    ax.spines['left'].set_color('#666666')
    ax.spines['bottom'].set_color('#666666')
    
    # Adjust tick colors
    ax.tick_params(axis='both', colors='#666666')
    
    # Tight layout
    plt.tight_layout()
    
    return plt

# Example usage:
# from weather import load_gistemp_data
# gistemp_df = load_gistemp_data()
# plt = plot_temperature_anomaly(gistemp_df)
# plt.show()



def create_hurricane_typhoon_map(
    figsize=(15, 8),
    line_color='red',
    text_color='darkred',
    text_size=12,
    title_size=16
):
    """
    Creates a visualization showing hurricane/typhoon regions with a map background.
    
    Parameters:
    -----------
    figsize : tuple, default (15, 8)
        Size of the figure in inches
    line_color : str, default 'red'
        Color of the dividing line
    text_color : str, default 'darkred'
        Color of the text labels
    text_size : int, default 12
        Size of the main labels
    title_size : int, default 16
        Size of the title
    
    Returns:
    --------
    tuple
        (figure, axis) matplotlib objects
    """
    # Create figure with cartopy projection
    plt.figure(figsize=figsize)
    ax = plt.axes(projection=ccrs.PlateCarree())
    
    # Add map features
    ax.add_feature(cfeature.LAND, facecolor='lightgray')
    ax.add_feature(cfeature.OCEAN, facecolor='lightblue')
    ax.add_feature(cfeature.COASTLINE, linewidth=0.5)
    
    # Create sample data points
    np.random.seed(42)  # for reproducibility
    n_points = 50
    
    # Western Pacific (Typhoon) points
    west_x = np.random.uniform(20, 150, n_points)
    west_y = np.random.uniform(-20, 40, n_points)
    
    # Eastern Pacific (Hurricane) points
    east_x = np.random.uniform(-150, -20, n_points)
    east_y = np.random.uniform(-20, 40, n_points)
    
    # Create DataFrame
    data = pd.DataFrame({
        'longitude': np.concatenate([west_x, east_x]),
        'latitude': np.concatenate([west_y, east_y]),
        'storm_type': ['Typhoon']*n_points + ['Hurricane']*n_points
    })
    
    # Plot storm locations
    for storm_type, color, marker in [('Hurricane', 'navy', 'x'), ('Typhoon', 'darkred', 'o')]:
        mask = data['storm_type'] == storm_type
        ax.scatter(data[mask]['longitude'], 
                  data[mask]['latitude'],
                  c=color, 
                  marker=marker,
                  s=100,
                  alpha=0.5,
                  label=storm_type,
                  transform=ccrs.PlateCarree())
    
    # Add the dividing line
    x = np.linspace(-180, 180, 200)
    y = 15 * np.sin((x + 30) / 100)
    ax.plot(x, y, color=line_color, linestyle='--', linewidth=2, transform=ccrs.PlateCarree())
    
    # Set the map extent
    ax.set_extent([-180, 180, -60, 60], crs=ccrs.PlateCarree())
    
    # Add gridlines
    ax.gridlines(draw_labels=True, alpha=0.3)
    
    # Add labels
    ax.text(-120, 50, 'Hurricanes', fontsize=text_size+4, color='navy', 
            fontweight='bold', transform=ccrs.PlateCarree())
    ax.text(80, 50, 'Typhoons', fontsize=text_size+4, color='darkred', 
            fontweight='bold', transform=ccrs.PlateCarree())
    
    # Add title
    plt.title('Same Storm, Different Names', fontsize=title_size, pad=20)
    
    # Add explanation
    ax.text(0, -50, 
            'The same type of tropical cyclone is called a "hurricane" in the Eastern Pacific\n'
            'and Atlantic, but a "typhoon" in the Western Pacific',
            ha='center', fontsize=text_size-2, transform=ccrs.PlateCarree())
    
    plt.tight_layout()
    
    return plt.gcf(), ax

# Example usage:
# fig, ax = create_hurricane_typhoon_map()
# plt.show()


def plot_correlation(gistemp_df, major_hurricanes_df):
    # Calculate annual stats
    annual_stats = pd.DataFrame()
    
    # Get annual temperature averages
    annual_stats['avg_temp'] = gistemp_df.groupby('Year')['No_Smoothing'].mean()
    
    # Count major hurricanes per year
    hurricane_counts = major_hurricanes_df[
        major_hurricanes_df['category'].isin([4, 5])
    ]['year'].value_counts().sort_index()
    annual_stats['major_hurricanes'] = hurricane_counts
    
    # Fill missing values with 0
    annual_stats['major_hurricanes'] = annual_stats['major_hurricanes'].fillna(0)
    
    # Calculate correlation
    correlation = stats.pearsonr(annual_stats['avg_temp'], 
                               annual_stats['major_hurricanes'])[0]
    
    # Create scatter plot
    plt.figure(figsize=(10, 6))
    
    # Plot points with jitter to show overlapping points
    sns.regplot(data=annual_stats,
                x='avg_temp',
                y='major_hurricanes',
                scatter_kws={'alpha':0.5, 'color':'darkblue'},
                line_kws={'color': 'red'})
    
    # Add correlation info in student-friendly terms
    if correlation >= 0.5:
        strength = "strong"
    elif correlation >= 0.3:
        strength = "moderate"
    else:
        strength = "weak"
        
    plt.title("Warmer Years Have More Strong Hurricanes\n" +
             f"({strength} positive relationship)", 
             pad=20, fontsize=12)
    
    plt.xlabel('Temperature Difference from Normal (°C)', fontsize=10)
    plt.ylabel('Number of Category 4-5 Hurricanes per Year', fontsize=10)
    
    # Add simple explanation
    plt.text(0.05, 0.95, 
            "Each dot represents one year.\n" +
            "Upward slope shows that as temperature increases,\n" +
            "we tend to see more powerful hurricanes.",
            transform=plt.gca().transAxes,
            verticalalignment='top',
            fontsize=9)
    
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    
    return plt
