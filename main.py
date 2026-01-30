
from chromedriver_manager import (
    ChromeDriverManager
)


def main() -> str:
    manager = ChromeDriverManager()
    driver_path = manager.get_driver_path()
    return driver_path
    
if __name__ == "__main__":
    main()
