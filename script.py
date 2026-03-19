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

SelectChart()

            
            
