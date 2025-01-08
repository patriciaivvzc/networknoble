# NetworkNoble

NetworkNoble is a Python program designed to optimize network settings for enhanced performance and security on Windows devices.

## Features

- **Optimize Performance**: Adjusts TCP parameters to enhance network performance.
- **Enhance Security**: Enables firewall settings and disables legacy protocols (e.g., SMBv1) to improve security.
- **Reset to Default**: Resets network settings to their default state.

## Requirements

- Windows operating system
- Python 3.x
- Administrative privileges to execute network commands

## Installation

1. Ensure you have Python installed on your Windows device.
2. Clone the repository or download the `network_noble.py` file.

## Usage

1. Open a command prompt with administrative privileges.
2. Navigate to the directory containing `network_noble.py`.
3. Run the script using Python:

   ```shell
   python network_noble.py
   ```

4. Follow the on-screen instructions to select the desired operation:
   - Enter `1` to optimize network performance.
   - Enter `2` to enhance network security.
   - Enter `3` to reset network settings to default.

## Important Notes

- Some actions, such as disabling SMBv1, may impact compatibility with older devices or services. Ensure you understand these changes before applying them.
- The program requires administrative privileges to run certain network commands. Make sure to run the command prompt as an administrator.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

## Disclaimer

The author is not responsible for any issues that arise from the use of this program. Use at your own risk and ensure you have backups of your system and data.