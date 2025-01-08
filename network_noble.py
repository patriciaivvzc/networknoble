import subprocess
import os

class NetworkNoble:
    def __init__(self):
        self.settings_applied = False

    def optimize_performance(self):
        try:
            print("Optimizing network performance settings...")
            # Adjust TCP parameters for better performance
            subprocess.run(["netsh", "int", "tcp", "set", "global", "rss=enabled"], check=True)
            subprocess.run(["netsh", "int", "tcp", "set", "global", "autotuninglevel=normal"], check=True)
            subprocess.run(["netsh", "int", "tcp", "set", "heuristics", "disabled"], check=True)
            self.settings_applied = True
            print("Performance settings optimized successfully.")
        except subprocess.CalledProcessError as e:
            print(f"Failed to optimize performance settings: {e}")

    def enhance_security(self):
        try:
            print("Enhancing network security settings...")
            # Enable firewall
            subprocess.run(["netsh", "advfirewall", "set", "allprofiles", "state", "on"], check=True)
            # Disable SMBv1
            subprocess.run(["dism", "/online", "/norestart", "/disable-feature", "/featurename:SMB1Protocol"], check=True)
            self.settings_applied = True
            print("Security settings enhanced successfully.")
        except subprocess.CalledProcessError as e:
            print(f"Failed to enhance security settings: {e}")

    def reset_settings(self):
        try:
            print("Resetting network settings to default...")
            subprocess.run(["netsh", "int", "ip", "reset"], check=True)
            subprocess.run(["netsh", "winsock", "reset"], check=True)
            self.settings_applied = False
            print("Network settings reset to default successfully.")
        except subprocess.CalledProcessError as e:
            print(f"Failed to reset network settings: {e}")

if __name__ == "__main__":
    network_noble = NetworkNoble()
    print("Welcome to NetworkNoble! Choose an option:")
    print("1. Optimize Performance")
    print("2. Enhance Security")
    print("3. Reset to Default")
    
    option = input("Enter the number of your choice: ")

    if option == "1":
        network_noble.optimize_performance()
    elif option == "2":
        network_noble.enhance_security()
    elif option == "3":
        network_noble.reset_settings()
    else:
        print("Invalid option. Please choose 1, 2, or 3.")