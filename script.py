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
            if ChartInput == 1 or ChartInput ==2:
                return time_series_menu
            elif ChartInput != 1 or ChartInput != 2:
                print("Invalid integer, please try again.") 
            else:
                return SelectChart()
        # Making sure that a person's input is not a string
        except ValueError:
            print("Input must be the integer 1 or 2")

# ======= TIME SERIES (Ben) =======
def time_series_menu():
    
    while True:
    
        print("Select the Time Series of the chart you want to Generate\n----------------------------------------------")
        print("1. Intraday")
        print("2. Daily")
        print("3. Weekly")
        print("4. Monthly")

        time_series = input("Enter the time seroes option (1, 2, 3, 4): ")
        if time_series == "1":
            return 1
        elif time_series == "2":
            return 2
        elif time_series == "3":
            return 3
        elif time_series == "4":
            return 4
        else: 
            print("ERROR: input is invalid try again...")
            continue

def get_time_series_label(time_series_type):
    if time_series_type == 1:
        return "Intraday"
    elif time_series_type == 2:
        return "Daily"
    elif time_series_type == 3:
        return "Weekly"
    elif time_series_type == 4:
        return "Monthly"
    
# ======= TIME SERIES QUERY (Mia) =======
def querying_api(time_series_type, stock_symbol, API_KEY):
    try:
        import requests
    except:
        print("\nFailed to import requests")

    while True:
        if time_series_type == 1:
            url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={stock_symbol}&interval=5min&apikey={API_KEY}'
            r = requests.get(url)
            data = r.json()
            return data
        elif time_series_type == 2:
            url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={stock_symbol}&apikey={API_KEY}'
            r = requests.get(url)
            data = r.json()
            return data
        elif time_series_type == 3:
            url = f'https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY&symbol={stock_symbol}&apikey={API_KEY}'
            r = requests.get(url)
            data = r.json()
            return data
        elif time_series_type == 4:
            url = f'https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY&symbol={stock_symbol}&apikey={API_KEY}'
            r = requests.get(url)
            data = r.json()
            return data
        else:
            print("Error!")

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

# GRAPH GENERATION (Trent)

def GraphGeneration(data, ChartInput, start_date, end_date, symbol, time_series_type):
        import pygal
        import json

        # Set the keys to the input according to their json values:
        if time_series_type == 1:
            TimeKey = "Time Series (5min)"
        elif time_series_type == 2:
            TimeKey = "Time Series (Daily)"
        elif time_series_type == 3:
            TimeKey = "Weekly Time Series"
        elif time_series_type == 4:
            TimeKey = "Monthly Time Series"
        else:
            print("Value Error, please try again")
        
        # Get the stock data from the four different points and put it into a dictionary
        # Uses the key value pair "1. open : 323.45", for example from json
       
        with open('r.json') as StockData:
            StockData = json.load(StockData)
            print(StockData)
        
        # Get the date(s)
        
        # Establishing separate lists for the four data points in the json file
        HighPrice = []
        LowPrice = []
        OpenPrice = []
        ClosePrice = []

        # Assigning the prices to their date
        for data in StockData:
            OpenPrice.append(float(StockData[date]["1. open"]))
            HighPrice.append(float(StockData[date]["2. high"]))
            LowPrice.append(float(StockData[date]["3. open"]))
            ClosePrice.append(float(StockData[date]["4. close"]))

            if data not in StockDatas:
                print("There was an error getting stock prices")
        
        # // Create the chart
        try:
            if ChartInput == 1:
                chart = pygal.Line()
            else:
                chart = pygal.Bar()
        except ValueError:
            print("Value Error")    
        
        # print the chart title and labels
        
        chart.title = f"Stock Data for {symbol}: {start_date} to {end_date}"
        
        chart.x_labels = GraphData
        chart.add('Open', OpenPrice)
        chart.add('Close', ClosePrice)
        chart.add('High', HighPrice)
        chart.add('Low', LowPrice)

# ============== MAIN FUNCTION ==============
def main():

    # == API KEY ==:
    API_KEY = "T5LLNYG4DQCQB5QI"

    # == Stock Symbol ==
    stock_symbol = get_stock_symbol()

    # == Chart Select ==
    chart = SelectChart()
    CharInput = SelectChart()
    # == Time Series ==
    time_series_type = time_series_menu()
    querying_api(time_series_type, stock_symbol, API_KEY)
    
    # == Date Selection ==
    begin_date = get_begin_date()
    end_date = get_end_date()
    validate_dates(begin_date, end_date)

    data = querying_api(time_series_type, stock_symbol, API_KEY)
    GraphGeneration(data, begin_date, end_date, stock_symbol, time_series_type)
    
main()
