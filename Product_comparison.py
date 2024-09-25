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

def create_device_from_data(name, specs):
    """Creates a MobileDevice instance from provided specifications."""
    return MobileDevice(
        name=name,
        release_date=specs.get("Release Date", "N/A"),
        price=specs.get("Price", "N/A"),
        market_positioning="Flagship",  # Assuming both are flagship devices
        display_size=specs.get("Display Size", "N/A"),
        display_resolution=specs.get("Display Resolution", "N/A"),
        refresh_rate=specs.get("Refresh Rate", "N/A"),
        processor=specs.get("Processor", "N/A"),
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
    # Specifications extracted from search results
    samsung_s24_specs = {
        "Release Date": "January 17, 2024",
        "Price": "$799",
        "Display Size": "6.2 inches",
        "Display Resolution": "2340 x 1080 pixels",
        "Refresh Rate": "1-120Hz",
        "Processor": "Snapdragon 8 Gen 3 / Exynos 2400",
        "RAM": "8 GB",
        "Storage": "128GB / 256GB",
        "Battery": "4000 mAh"
    }

    iphone_15_specs = {
        "Release Date": "September 12, 2023",
        "Price": "$799",
        "Display Size": "6.1 inches",
        "Display Resolution": "2556 x 1179 pixels",
        "Refresh Rate": "60Hz",
        "Processor": "A16 Bionic",
        "RAM": "6 GB",
        "Storage": "128GB / 256GB / 512GB",
        "Battery": "3349 mAh"
    }

    # Create device instances
    samsung_s24_device = create_device_from_data("Samsung Galaxy S24", samsung_s24_specs)
    iphone_15_device = create_device_from_data("iPhone 15", iphone_15_specs)

    # Compare the two devices
    compare_devices(samsung_s24_device, iphone_15_device)
