import os
from scraping_utils import get_url, parse
from dotenv import load_dotenv
import matplotlib.pyplot as plt

def plot_data(data):
    years = [int(item["Report_Year"]) for item in data]
    emissions = [item["Total_GHG_emissions"] for item in data]

    plt.figure(figsize=(10, 5))
    plt.plot(years, emissions, marker='o', color='#fe2c55')  # 修改颜色为#fe2c55
    plt.title('Total GHG Emissions Over Years')
    plt.xlabel('Year')
    plt.ylabel('Total GHG Emissions')
    plt.grid(True)
    plt.show()

def main():
    load_dotenv()
    url = os.getenv('URL')
    page = get_url(url, 'data.json')
    tree = parse(page, 'json')
    print(tree)
    plot_data(tree)

if __name__ == "__main__":
    main()