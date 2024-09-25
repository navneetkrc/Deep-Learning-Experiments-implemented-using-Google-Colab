import requests
from bs4 import BeautifulSoup

class MobileDevice:
    def __init__(self, name, release_date, price, market_positioning,
                 display_size, display_resolution, refresh_rate,
                 processor, ram, storage, battery_capacity):
        self.name = name
        self.release_date = release_date
        self.price = price
        self.market_positioning = market_positioning
        self.display_size = display_size
        self.display_resolution = display_resolution
        self.refresh_rate = refresh_rate
        self.processor = processor
        self.ram = ram
        self.storage = storage
        self.battery_capacity = battery_capacity

    def display_info(self):
        return f"{self.name}:\n" \
               f"  Release Date: {self.release_date}\n" \
               f"  Price: ${self.price}\n" \
               f"  Market Positioning: {self.market_positioning}\n" \
               f"  Display: {self.display_size}, {self.display_resolution}, {self.refresh_rate}Hz\n" \
               f"  Processor: {self.processor}\n" \
               f"  RAM: {self.ram}GB\n" \
               f"  Storage Options: {self.storage}\n" \
               f"  Battery Capacity: {self.battery_capacity} mAh\n"

def fetch_phone_data(phone_name):
    """Fetches mobile phone specifications from GSMArena."""
    url = f"https://www.gsmarena.com/{phone_name.replace(' ', '_').lower()}-10100.php"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36"
    }
    
    response = requests.get(url, headers=headers)
    
    if response.status_code != 200:
        print(f"Failed to retrieve data for {phone_name}")
        return None

    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Extract specifications from the page
    specs_table = soup.find("table", {"class": "specs-table"})
    specs = {}
    
    if specs_table:
        rows = specs_table.find_all("tr")
        for row in rows:
            header = row.find("td", {"class": "ttl"})
            value = row.find("td", {"class": "nfo"})
            if header and value:
                specs[header.get_text(strip=True)] = value.get_text(strip=True)

    return specs

def create_device_from_specs(name, specs):
    """Creates a MobileDevice instance from fetched specifications."""
    return MobileDevice(
        name=name,
        release_date=specs.get("Announced", "N/A"),
        price=specs.get("Price", "N/A"),
        market_positioning="Flagship",  # Assuming both are flagship devices
        display_size=specs.get("Display", "N/A"),
        display_resolution=specs.get("Resolution", "N/A"),
        refresh_rate=specs.get("Refresh Rate", "N/A"),
        processor=specs.get("Chipset", "N/A"),
        ram=specs.get("RAM", "N/A").replace(' GB', ''),
        storage=specs.get("Storage", "N/A"),
        battery_capacity=specs.get("Battery", "N/A").replace(' mAh', '')
    )

def compare_devices(device1, device2):
    print(device1.display_info())
    print(device2.display_info())

    print("Comparison Results:")
    attributes = ['release_date', 'price', 'market_positioning', 
                  'display_size', 'display_resolution', 
                  'refresh_rate', 'processor', 'ram', 
                  'storage', 'battery_capacity']
    
    for attr in attributes:
        value1 = getattr(device1, attr)
        value2 = getattr(device2, attr)
        
        if value1 != value2:
            print(f"{attr.replace('_', ' ').capitalize()}:")
            print(f"  {device1.name}: {value1}")
            print(f"  {device2.name}: {value2}")
            print()

if __name__ == "__main__":
    # Fetch data for Samsung Galaxy S24 and iPhone 15
    samsung_s24_specs = fetch_phone_data("Samsung Galaxy S24")
    iphone_15_specs = fetch_phone_data("iPhone 15")

    if samsung_s24_specs and iphone_15_specs:
        samsung_s24_device = create_device_from_specs("Samsung Galaxy S24", samsung_s24_specs)
        iphone_15_device = create_device_from_specs("iPhone 15", iphone_15_specs)

        # Compare the two devices
        compare_devices(samsung_s24_device, iphone_15_device)
