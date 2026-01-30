
from chromedriver_manager import (
    get_driver_path
)


def main() -> str:
    driver_path = get_driver_path()
    return driver_path
    
if __name__ == "__main__":
    main()
