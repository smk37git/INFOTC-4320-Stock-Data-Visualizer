# Scrum Team 6 | INFOTC-4320-Stock-Data-Visualizer


def get_stock_symbol():
    #Ask user for stock symbol and validate input
    #returns a valid, uppercase stock symbol

    while True:
        symbol = input("Enter the stock symbol you are looking for: ").strip().upper()
        if len(symbol) == 0:
            print("Invalid input! Please try again.\n")
        elif not symbol.isalpha():
            print("Invalid input! Stock symbols should only contain letters. Please try again.\n")
        else:
            return symbol
        
def SelectChart():
    while True:
        try:    
            # Ask user for input and validate their choice
            ChartInput = int(input("Please select a chart type:\n 1. Line Graph\n 2. Bar Graph\n\n Selection: "))
            while ChartInput == 1 or ChartInput == 2:
                if ChartInput == 1:
                    LineGraph()
                elif ChartInput == 2:
                    BarChart()
                elif ChartInput != 1 or ChartInput != 2:
                    print("The value must be either 1 or 2")      
                else:
                    return SelectChart
        # Making sure that a person's input is not a string
        except ValueError:
            print("Input must be the integer 1 or 2")
        


if __name__ == "__main__":
    stock_symbol = get_stock_symbol()
    SelectChart()

            

   