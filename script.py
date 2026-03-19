# Scrum Team 6 | INFOTC-4320-Stock-Data-Visualizer

# ======= STOCK SYMBOL (Mia) =======
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
        

# ======= SELECT CHART (Trent) =======
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
        
# ======= TIME SERIES (Ben) =======


# ======= YYYY-MM-DD [Begin & End] (Sebastian) =======
def get_begin_date():

    while True:

        # Gather Input
        begin_date = input("\nPlease enter beginning date (YYYY-MM-DD): ")

        # Validate 
        if is_date_valid(begin_date):
            return begin_date

def get_end_date():
        
        while True:

            # Gather Input
            end_date = input("\nPlease enter ending date (YYYY-MM-DD): ")

            # Validate 
            if is_date_valid(end_date):
                return end_date

def is_date_valid(selected_date):

    # Make sure string isn't empty
    if len(selected_date) == 0:
            print("\nERROR: Beginning Date should not be null")

    # Strip and convert to date-time format
    try:
        import datetime

        datetime.datetime.strptime(selected_date, "%Y-%m-%d")
        return True
    except:
        print("\nERROR: Input is not in correct YYYY-MM-DD format")
        return False
    
def validate_dates(begin_date, end_date):
    try:
        import datetime

        # Restrip and convert to date-time format
        begin = datetime.datetime.strptime(begin_date, "%Y-%m-%d")
        end = datetime.datetime.strptime(end_date, "%Y-%m-%d")

        # If beginning date is less than end date
        if begin < end:
            return True
        else:
            print("\nERROR: Dates are not correctly selected")
            return False

    # Date parsing failed
    except:
        print("\nERROR: Invalid date format")
        return False

# ============== MAIN FUNCTION ==============
def main():

    # == Stock Symbol ==
    stock_symbol = get_stock_symbol()

    # == Chart Select ==
    chart = SelectChart()

    # == Time Series ==

    # == Date Selection ==
    begin_date = get_begin_date()
    end_date = get_end_date()
    validate_dates(begin_date, end_date)

main()