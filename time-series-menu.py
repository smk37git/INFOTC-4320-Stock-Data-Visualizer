def time_series_menu():
    
    while True:
    
        print("Select the Time Series of the chart you want to Generate\n----------------------------------------------")
        print("1. Intraday")
        print("2. Daily")
        print("3. Weekly")
        print("4. Monthly")

        time_series = input("Enter the time seroes option (1, 2, 3, 4): ")
        if time_series == "1":
            Intraday()
        elif time_series == "2":
            Daily()
        elif time_series == "3":
            Weekly()
        elif time_series == "4":
            Monthly()
        else: 
            print("ERROR: input is invalid try again...")
            continue
        return