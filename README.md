# Fake-Bitcoin-miner
Fake bitcoin miner is a Python program that lets you generate fake wallets for cryptocurrency transactions in real time. It displays your total balance in both BTC and USD and updates the balance with each transaction. The program reads and writes to a file named bal.txt to save the current balance between sessions.

## Requirements
In order to run this program, you will need to install the following Python modules:

- colorama
- secrets
You can install them using pip, by running the following command:

```pip install colorama secrets```

## Usage
To run the program, simply execute the main.py file. You should see a prompt displaying "0x1caf8e2d329e89d78437494c256bf293ee9a381c > 0.00 BTC ($0.00)". The program will automatically log transactions/wallets and display the current balance. To stop the program, press Control + C.

## Known Issues
- Program may crash if bal.txt file is empty
- Delay at exit if the user mines for a long time
## Future Improvements
- Add GUI (Graphical User Interface) for better user experience
- Implement support for sending and receiving cryptocurrency
- Add support for more crypto coins and tokens
## Contributors
- shrekkkkkkkk - Replit Creator
- Zionek - Code Modified
## License
This project is licensed under the MIT License - see the LICENSE file for details.
