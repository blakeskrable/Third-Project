import time
from time import sleep as s
import statistics
from statistics import stdev
import pandas as pd
import math 

def sequence():    
    print("What would you like to do with this data set?")
    s(2)
    print("1. Get general statistics for filtering by a ceiling threshold value")
    s(2)
    print("2. Get general statistics for filtering by a floor threshold value")
    s(2)
    print("3. Get general statistics for filtering by a range of values")
    s(2)
    print("4. Get general statistics with no filter")
    s(2)
    print("Where general statistics refer to: n value, max and min values, averages, standard deviations, percentages (where applicable)")
    s(4)
    selection2 = int(input("Please enter the number (1-4) of the function you would like to use: "))
    return selection2

def ceiling():    
    print("You have chosen to get statistics for filtering by a ceiling threshold value")
    s(2)
    print("You will be given:")
    s(2)
    print("1. The number of data points in the old data set")
    s(2)
    print("2. The max and min of the old data set")
    s(2)
    print("3. The average of the old data set")
    s(2)
    print("4. The standard deviation of the old data set")
    s(2)
    print("5. The percentage of data points that fell under the ceiling")
    s(2)
    print("6. The number of data points in the new data set")
    s(2)
    print("7. The max and min of the new data set")
    s(2)
    print("8. The average of the new data set")
    s(2)
    print("9. The standard deviation of the new data set")
    s(2)
                    
def floor():
    print("You have chosen to get statistics for filtering by a floor threshold value")
    s(2)
    print("You will be given:")
    s(2)
    print("1. The number of data points in the old data set")
    s(2)
    print("2. The max and min of the old data set")
    s(2)
    print("3. The average of the old data set")
    s(2)
    print("4. The standard deviation of the old data set")
    s(2)
    print("5. The percentage of data points that are above the floor")
    s(2)
    print("6. The number of data points in the new data set")
    s(2)
    print("7. The max and min of the new data set")
    s(2)
    print("8. The average of the new data set")
    s(2)
    print("9. The standard deviation of the new data set")
    s(2)

def rangex():
    print("You have chosen to get statistics for filtering by a range of values")
    s(2)
    print("You will be given:")
    s(2)
    print("1. The number of data points in the old data set")
    s(2)
    print("2. The max and min of the old data set")
    s(2)
    print("3. The average of the old data set")
    s(2)
    print("4. The standard deviation of the old data set")
    s(2)
    print("5. The percentage of data points that are within the range")
    s(2)
    print("6. The number of data points in the new data set")
    s(2)
    print("7. The max and min of the new data set")
    s(2)
    print("8. The average of the new data set")
    s(2)
    print("9. The standard deviation of the new data set")
    s(2)

def nofilter():
    print("You have chosen to get general statistics.")
    s(2)
    print("You will be given:")
    s(2)
    print("1. The n value of your data set")
    s(2)
    print("2. The max and min of your data set")
    s(2)
    print("3. The average value of your data set")
    s(2)
    print("4. The standard deviation of your data set")
    s(2)

#Intro, Data set selection pt. 1
def step2():
    print("I am going to be filtering and/or analyzing data for you.")
    s(2)
    print("To start, tell me how you would like to input your data:")
    s(2)
    print("1. Manually enter your data")
    s(2)
    print("2. Import your data from Excel")
    s(2)

step2()

#data set selection pt. 2
def step3():
    selection = int(input("Please type the number (1 or 2) of the type of data entry you would like to use: "))
    return selection

selection = int(step3())

#Fork path for small & large set
while selection != 1 and selection != 2:
    print("I'm sorry, I dont understand.")
    s(2)
    selection = int(input("Please enter the value (1 or 2) corresponding to the data set type you want to filter: "))
else: 
    if selection == 1:
        print("You have chosen to manually enter your data set.")
        s(2)
        n = int(input("The number of data points in your data set is: "))
        small_lst = []


        #small list input
        def small_set():
            print("Please enter each value one at a time and press enter after each: ")
            for numbers in range(0,n):
                add = float(input())
                small_lst.append(add)

        small_set()
        
        #small list filter option
        def listvisible():
            print("Your data set is: ")
            print(small_lst)
            s(3)

        listvisible()
   
        selection2 = int(sequence())
        

        #small list filter option fork
        while selection2 != 1 and selection2 != 2 and selection2 != 3 and selection2 != 4:
            print("I'm sorry, I dont understand.")
            s(2)
            selection2 = int(input("Please enter the value (1-4) corresponding to the data set type you want to filter: "))
        else:
            if selection2 == 1:
                ceiling()
                n2 = float(input("Please input the value of the ceiling: "))

                #ceiling threshold function
                def filter1():
                    New_small_lst_str = filter(lambda x: x<n2, small_lst)
                    New_small_list = list(New_small_lst_str)
                    Newtotal = len(New_small_list)
                    Oldtotal = len(small_lst)
                    old_small_list_stdev = stdev(small_lst)
                    new_small_list_stdev = stdev(New_small_list)
                    old_average1 = (sum(small_lst)/n)
                    new_average1 = (sum(New_small_list)/Newtotal)
                    maxold = max(small_lst)
                    maxnew1= max(New_small_list)
                    minold= min(small_lst)
                    minnew1 = min(New_small_list)
                    
                    print("For the old data set (with no filter applied):")
                    s(3)
                    print(small_lst)
                    s(3)
                    print("The total number of data points is:", Oldtotal)
                    s(3)
                    print("The max of the old data set is:", maxold)
                    s(3)
                    print("The min of the old data set is:", minold)
                    s(3)
                    print("The average of the data set is:", old_average1)
                    s(3)
                    print("The standard deviation is:", old_small_list_stdev)
                    s(3)
                    print("For the new data set (with the ceiling filter applied):")
                    s(3)
                    print(New_small_list)
                    s(3)
                    print("The percentage of data points that fell under the ceiling is:", ((Newtotal/n)*100), "%")
                    s(3)
                    print("The total number of data points (that fell under the ceiling) is:", Newtotal)
                    s(3)
                    print("The max of the new data set is:", maxnew1)
                    s(3)
                    print("The min of the new data set is:", minnew1)
                    s(3)
                    print("The average of the new data set is:", new_average1)
                    s(3)
                    print("The standard deviation of the new data set is:", new_small_list_stdev)
                    s(3)

                filter1()

            elif selection2 == 2:
                floor()
                n3 = float(input("Please input the value of the floor: "))
                

                #floor threshold function
                def filter2():
                    New_small_lst_str2 = filter(lambda x: x>n3, small_lst)
                    New_small_list2 = list(New_small_lst_str2)
                    Newtotal2 = len(New_small_list2)
                    Oldtotal = len(small_lst)
                    old_small_list_stdev = stdev(small_lst)
                    new_small_list_stdev2 = stdev(New_small_list2)
                    old_average2 = (sum(small_lst)/n)
                    new_average2 = (sum(New_small_list2)/Newtotal2)
                    maxold = max(small_lst)
                    maxnew2= max(New_small_list2)
                    minold= min(small_lst)
                    minnew2 = min(New_small_list2)
                    print("For the old data set (with no filter applied):")
                    s(3)
                    print(small_lst)
                    s(3)
                    print("The total number of data points is:", Oldtotal)
                    s(3)
                    print("The max of the old data set is:", maxold)
                    s(3)
                    print("The min of the old data set is:", minold)
                    s(3)
                    print("The average of the data set is:", old_average2)
                    s(3)
                    print("The standard deviation is:", old_small_list_stdev)
                    s(3)
                    print("For the new data set (with the floor filter applied):")
                    s(3)
                    print(New_small_list2)
                    s(3)
                    print("The percentage of data points that are above the floor is:", ((Newtotal2/n)*100), "%")
                    s(3)
                    print("The total number of data points (that are above the floor) is:", Newtotal2)
                    s(3)
                    print("The max of the new data set is:", maxnew2)
                    s(3)
                    print("The min of the new data set is:", minnew2)
                    s(3)
                    print("The average of the new data set is:", new_average2)
                    s(3)
                    print("The standard deviation of the new data set is:", new_small_list_stdev2)
                    s(3)

                filter2()

            elif selection2 == 3:
                rangex()
                n4 = float(input("Please input the value of the lower bound: "))
                n5 = float(input("Please input the value of the upper bound: "))
                

                #range threshold function
                def filter3():
                    New_small_lst_str3 = filter(lambda x: n4<x<n5, small_lst)
                    New_small_list3 = list(New_small_lst_str3)
                    Newtotal3 = len(New_small_list3)
                    Oldtotal = len(small_lst)
                    old_small_list_stdev = stdev(small_lst)
                    new_small_list_stdev3 = stdev(New_small_list3)
                    old_average3 = (sum(small_lst)/n)
                    new_average3 = (sum(New_small_list3)/Newtotal3)
                    maxold = max(small_lst)
                    maxnew3= max(New_small_list3)
                    minold= min(small_lst)
                    minnew3 = min(New_small_list3)
                    print("For the old data set (with no filter applied):")
                    s(3)
                    print(small_lst)
                    s(3)
                    print("The total number of data points is:", Oldtotal)
                    s(3)
                    print("The max of the old data set is:", maxold)
                    s(3)
                    print("The min of the old data set is:", minold)
                    s(3)
                    print("The average of the data set is:", old_average3)
                    s(3)
                    print("The standard deviation is:", old_small_list_stdev)
                    s(3)
                    print("For the new data set (with the range filter applied):")
                    s(3)
                    print(New_small_list3)
                    s(3)
                    print("The percentage of data points that fall between the range is:", ((Newtotal3/n)*100), "%")
                    s(3)
                    print("The total number of data points (within the range) is:", Newtotal3)
                    s(3)
                    print("The max of the new data set is:", maxnew3)
                    s(3)
                    print("The min of the new data set is:", minnew3)
                    s(3)
                    print("The average of the new data set is:", new_average3)
                    s(3)
                    print("The standard deviation of the new data set is:", new_small_list_stdev3)
                    s(3)

                filter3()
            
            #general statistics function
            else:
                nofilter()

                def filter4():
                    average4 = (sum(small_lst)/n)
                    old_small_list_stdev = stdev(small_lst)
                    maxold = max(small_lst)
                    minold= min(small_lst)
                    print("The n value is:", n)
                    s(3)
                    print("The max is:", maxold)
                    s(3)
                    print("The min is:", minold)
                    s(3)
                    print("The average value is:", average4)
                    s(3)
                    print("The standard deviation is:", old_small_list_stdev)
                    s(3)

                filter4()
                    
    elif selection == 2:
        print("You have chosen to import your data set from Excel.")
        s(2)
        print("This will require you to import your data set from a file.")
        s(2)
        print("To start, download this program into an unused folder in your directory.")
        s(2)
        
        
        def checkpoint1():
            checkpoint= str(input("Type 'Ready' when you have completed this task: "))
            while checkpoint != "ready" and checkpoint != "Ready":
                print("I'm sorry, I dont understand.")
                s(2)
                checkpoint= str(input("Please type 'Ready' when you have completed this task: "))
        
        checkpoint1()

        print("Fantastic! Now I am going to have you click 'Save a copy' of the file with you downloaded data.")
        s(2)
        print("Download this file containing your data as an 'xlsx' file into the same folder.")")
        s(2)
        
        checkpoint1()

        print("Fantastic! Now I am going to have you copy the path address of your file in the folder.")
        s(2)
        print("To do this, first select the file.")
        s(2)
        print("Then, hold shift and right click on the file, and then click the 'Copy as Path' option")
        s(2)

        checkpoint1()

        print("Paste the path of the file in the space below.")
        s(2)
        print("Before hitting enter, please remove the quotation marks surrounding the file path: ")
        s(2)
        filename = input()
        df2 = pd.read_excel(filename)
                
        def excelfileimport():
            print("Your data is: ")
            s(1)
            print(df2)
                
        excelfileimport()
        s(2)

        def roworcolumn():
            print("Are you going to be analyzing a specific row or column?")
            s(2)
            row_or_column = str(input("Please type 'row' or 'column' to indicate which you would like to work with: "))
            return row_or_column
                
        row_or_column = str(roworcolumn())
                

        while row_or_column != "row" and row_or_column != "Row" and row_or_column != "column" and row_or_column != "Column":
            print("I'm sorry, I dont understand.")
            s(2)
            row_or_column = str(input("Please enter either 'row' or 'column' into the space below: "))
        else:
            if row_or_column == "row" or row_or_column == "Row":
                def rowselection():
                    print("You have chosen to analyze a specific row within your file.")
                    s(2)
                    rowx = int(input("Please type the number of the row in your data set that you would like to analyze, according to the program's numbers: "))
                    return rowx

                rowx = int(rowselection())

                row_list= list(df2.loc[rowx])
                row_list_filtered_nan = list(filter(lambda x: isinstance(x, (int, float)), row_list))
                row_list_filtered = list(x for x in row_list_filtered_nan if math.isnan(x) == False)

                def rowlistfilter():
                    print("All the numeric values in this column are: ")
                    s(1)
                    print(row_list_filtered)
                    s(2)

                rowlistfilter()

                selection2 = int(sequence())

                while selection2 != 1 and selection2 != 2 and selection2 != 3 and selection2 != 4:
                    print("I'm sorry, I dont understand.")
                    s(2)
                    selection2 = int(input("Please enter the value (1-4) corresponding to the data set type you want to filter: "))
                else:
                    if selection2 == 1:
                        ceiling()     
                        n6 = float(input("Please input the value of the ceiling: "))
                            
                        def filter5():
                            New_row_list_str = filter(lambda x: x<n6, row_list_filtered)
                            New_row_list = list(New_row_list_str)
                            Newtotal7 = len(New_row_list)
                            Oldtotal3 = len(row_list_filtered)
                            old_row_list_stdev = stdev(row_list_filtered)
                            New_row_list_stdev = stdev(New_row_list)
                            old_average7 = (sum(row_list_filtered)/Oldtotal3)
                            new_average7 = (sum(New_row_list)/Newtotal7)
                            maxold3 = max(row_list_filtered)
                            maxnew7= max(New_row_list)
                            minold3= min(row_list_filtered)
                            minnew7 = min(New_row_list)
                    
                            print("For the old data set (with no filter applied, numerical values only):")
                            s(3)
                            print(row_list_filtered)
                            s(3)
                            print("The total number of data points is:", Oldtotal3)
                            s(3)
                            print("The min of the old data set is:", minold3)
                            s(3)
                            print("The max of the old data set is:", maxold3)
                            s(3)
                            print("The average of the data set is:", old_average7)
                            s(3)
                            print("The standard deviation is:", old_row_list_stdev)
                            s(3)
                            print("For the new data set (with the ceiling filter applied):")
                            s(3)
                            print(New_row_list)
                            s(3)
                            print("The percentage of data points that fell under the ceiling is:", ((Newtotal7/Oldtotal3)*100), "%")
                            s(3)
                            print("The total number of data points (that fell under the ceiling) is:", Newtotal7)
                            s(3)
                            print("The min of the new data set is:", minnew7)
                            s(3)
                            print("The max of the new data set is:", maxnew7)
                            s(3)
                            print("The average of the new data set is:", new_average7)
                            s(3)
                            print("The standard deviation of the new data set is:", New_row_list_stdev)
                            s(3)

                        filter5()

                    elif selection2 == 2:
                        floor()
                        n7 = float(input("Please input the value of the floor: "))
                

                        #floor threshold function
                        def filter6():
                            New_row_list_str2 = filter(lambda x: x>n7, row_list_filtered)
                            New_row_list2 = list(New_row_list_str2)
                            Newtotal8 = len(New_row_list2)
                            Oldtotal3 = len(row_list_filtered)
                            old_row_list_stdev = stdev(row_list_filtered)
                            new_row_list_stdev2 = stdev(New_row_list2)
                            old_average8 = (sum(row_list_filtered)/Oldtotal3)
                            new_average8 = (sum(New_row_list2)/Newtotal8)
                            maxold3 = max(row_list_filtered)
                            maxnew8= max(New_row_list2)
                            minold3= min(row_list_filtered)
                            minnew8 = min(New_row_list2)
                            print("For the old data set (with no filter applied, numerical values only):")
                            s(3)
                            print(row_list_filtered)
                            s(3)
                            print("The total number of data points is:", Oldtotal3)
                            s(3)
                            print("The min of the old data set is:", minold3)
                            s(3)
                            print("The max of the old data set is:", maxold3)
                            s(3)
                            print("The average of the data set is:", old_average8)
                            s(3)
                            print("The standard deviation is:", old_row_list_stdev)
                            s(3)
                            print("For the new data set (with the floor filter applied):")
                            s(3)
                            print(New_row_list2)
                            s(3)
                            print("The percentage of data points that are above the floor is:", ((Newtotal8/Oldtotal3)*100), "%")
                            s(3)
                            print("The total number of data points (that are above the floor) is:", Newtotal8)
                            s(3)
                            print("The min of the new data set is:", minnew8)
                            s(3)
                            print("The max of the new data set is:", maxnew8)
                            s(3)
                            print("The average of the new data set is:", new_average8)
                            s(3)
                            print("The standard deviation of the new data set is:", new_row_list_stdev2)
                            s(3)

                        filter6()

                    elif selection2 == 3:                       
                        rangex()   
                        n8 = float(input("Please input the value of the lower bound: "))
                        n9 = float(input("Please input the value of the upper bound: "))
                

                        #range threshold function
                        def filter7():
                            New_row_list_str3 = filter(lambda x: n8<x<n9, row_list_filtered)
                            New_row_list3 = list(New_row_list_str3)
                            Newtotal9 = len(New_row_list3)
                            Oldtotal3 = len(row_list_filtered)
                            old_row_list_stdev = stdev(row_list_filtered)
                            new_row_list_stdev3 = stdev(New_row_list3)
                            old_average9 = (sum(row_list_filtered)/Oldtotal3)
                            new_average9 = (sum(New_row_list3)/Newtotal9)
                            maxold3 = max(row_list_filtered)
                            maxnew9= max(New_row_list3)
                            minold3= min(row_list_filtered)
                            minnew9 = min(New_row_list3)
                            print("For the old data set (with no filter applied, numerical values only):")
                            s(3)
                            print(row_list_filtered)
                            s(3)
                            print("The total number of data points is:", Oldtotal3)
                            s(3)
                            print("The min of the old data set is:", minold3)
                            s(3)
                            print("The max of the old data set is:", maxold3)
                            s(3)
                            print("The average of the data set is:", old_average9)
                            s(3)
                            print("The standard deviation is:", old_row_list_stdev)
                            s(3)
                            print("For the new data set (with the range filter applied):")
                            s(3)
                            print(New_row_list3)
                            s(3)
                            print("The percentage of data points that fall between the range is:", ((Newtotal9/Oldtotal3)*100), "%")
                            s(3)
                            print("The total number of data points (within the range) is:", Newtotal9)
                            s(3)
                            print("The max of the new data set is:", maxnew9)
                            s(3)
                            print("The min of the new data set is:", minnew9)
                            s(3)
                            print("The average of the new data set is:", new_average9)
                            s(3)
                            print("The standard deviation of the new data set is:", new_row_list_stdev3)
                            s(3)

                        filter7()
            
                        #general statistics function
                    else:
                        nofilter()

                        def filter8():
                            Oldtotal3 = len(row_list_filtered)
                            average10 = (sum(row_list_filtered)/Oldtotal3)
                            old_row_list_stdev = stdev(row_list_filtered)
                            maxold3 = max(row_list_filtered)
                            minold3= min(row_list_filtered)
                            print("The n value is:", Oldtotal3)
                            s(3)
                            print("The max is:", maxold3)
                            s(3)
                            print("The min is:", minold3)
                            s(3)
                            print("The average value is:", average10)
                            s(3)
                            print("The standard deviation is:", old_row_list_stdev)
                            s(3)

                        filter8()

            else:
                print("You have chosen to analyze a specific column within your file.")
                s(2)
                print("I am going to have you type out the exact name of the column header you are going to analyze.")
                s(2)
                column1 = str(input("If there is no column name, type the exact header given by the program: "))

                column_list = list(df2[column1])
                column_list_filtered_nan = list(filter(lambda x: isinstance(x, (int, float)), column_list))
                column_list_filtered = list(x for x in column_list_filtered_nan if math.isnan(x) == False)
                        
                def columnlistfilter():
                    print("All the numeric values in this column are: ")
                    s(2)
                    print(column_list_filtered)
                    s(2)

                columnlistfilter()

                selection2 = int(sequence())

                while selection2 != 1 and selection2 != 2 and selection2 != 3 and selection2 != 4:
                    print("I'm sorry, I dont understand.")
                    s(2)
                    selection2 = int(input("Please enter the value (1-4) corresponding to the data set type you want to filter: "))
                else:
                    if selection2 == 1:
                        ceiling()
                        n10 = float(input("Please input the value of the ceiling: "))
                            
                        def filter9():
                            New_column_list_str = filter(lambda x: x<n10, column_list_filtered)
                            New_column_list = list(New_column_list_str)
                            Newtotal4 = len(New_column_list)
                            Oldtotal2 = len(column_list_filtered)
                            old_column_list_stdev = stdev(column_list_filtered)
                            new_column_list_stdev = stdev(New_column_list)
                            old_average4 = (sum(column_list_filtered)/Oldtotal2)
                            new_average4 = (sum(New_column_list)/Newtotal4)
                            maxold2 = max(column_list_filtered)
                            maxnew4= max(New_column_list)
                            minold2= min(column_list_filtered)
                            minnew4 = min(New_column_list)
                    
                            print("For the old data set (with no filter applied, numerical values only):")
                            s(3)
                            print(column_list_filtered)
                            s(3)
                            print("The total number of data points is:", Oldtotal2)
                            s(3)
                            print("The min of the old data set is:", minold2)
                            s(3)
                            print("The max of the old data set is:", maxold2)
                            s(3)
                            print("The average of the data set is:", old_average4)
                            s(3)
                            print("The standard deviation is:", old_column_list_stdev)
                            s(3)
                            print("For the new data set (with the ceiling filter applied):")
                            s(3)
                            print(New_column_list)
                            s(3)
                            print("The percentage of data points that fell under the ceiling is:", ((Newtotal4/Oldtotal2)*100), "%")
                            s(3)
                            print("The total number of data points (that fell under the ceiling) is:", Newtotal4)
                            s(3)
                            print("The min of the new data set is:", minnew4)
                            s(3)
                            print("The max of the new data set is:", maxnew4)
                            s(3)
                            print("The average of the new data set is:", new_average4)
                            s(3)
                            print("The standard deviation of the new data set is:", new_column_list_stdev)
                            s(3)

                        filter9()

                    elif selection2 == 2:
                        floor()
                        n11 = float(input("Please input the value of the floor: "))
                
                        #floor threshold function
                        def filter10():
                            New_column_list_str2 = filter(lambda x: x>n11, column_list_filtered)
                            New_column_list2 = list(New_column_list_str2)
                            Newtotal5 = len(New_column_list2)
                            Oldtotal2 = len(column_list_filtered)
                            old_column_list_stdev = stdev(column_list_filtered)
                            new_column_list_stdev2 = stdev(New_column_list2)
                            old_average5 = (sum(column_list_filtered)/Oldtotal2)
                            new_average5 = (sum(New_column_list2)/Newtotal5)
                            maxold2 = max(column_list_filtered)
                            maxnew5= max(New_column_list2)
                            minold2= min(column_list_filtered)
                            minnew5 = min(New_column_list2)
                            print("For the old data set (with no filter applied, numerical values only):")
                            s(3)
                            print(column_list_filtered)
                            s(3)
                            print("The total number of data points is:", Oldtotal2)
                            s(3)
                            print("The min of the old data set is:", minold2)
                            s(3)
                            print("The max of the old data set is:", maxold2)
                            s(3)
                            print("The average of the data set is:", old_average5)
                            s(3)
                            print("The standard deviation is:", old_column_list_stdev)
                            s(3)
                            print("For the new data set (with the floor filter applied):")
                            s(3)
                            print(New_column_list2)
                            s(3)
                            print("The percentage of data points that are above the floor is:", ((Newtotal5/Oldtotal2)*100), "%")
                            s(3)
                            print("The total number of data points (that are above the floor) is:", Newtotal5)
                            s(3)
                            print("The min of the new data set is:", minnew5)
                            s(3)
                            print("The max of the new data set is:", maxnew5)
                            s(3)
                            print("The average of the new data set is:", new_average5)
                            s(3)
                            print("The standard deviation of the new data set is:", new_column_list_stdev2)
                            s(3)

                        filter10()

                    elif selection2 == 3:
                        rangex()
                        n12 = float(input("Please input the value of the lower bound: "))
                        n13 = float(input("Please input the value of the upper bound: "))
                

                        #range threshold function
                        def filter11():
                            New_column_list_str3 = filter(lambda x: n12<x<n13, column_list_filtered)
                            New_column_list3 = list(New_column_list_str3)
                            Newtotal6 = len(New_column_list3)
                            Oldtotal2 = len(column_list_filtered)
                            old_column_list_stdev = stdev(column_list_filtered)
                            new_column_list_stdev3 = stdev(New_column_list3)
                            old_average6 = (sum(column_list_filtered)/Oldtotal2)
                            new_average6 = (sum(New_column_list3)/Newtotal6)
                            maxold2 = max(column_list_filtered)
                            maxnew6= max(New_column_list3)
                            minold2= min(column_list_filtered)
                            minnew6 = min(New_column_list3)
                            print("For the old data set (with no filter applied, numerical values only):")
                            s(3)
                            print(column_list_filtered)
                            s(3)
                            print("The total number of data points is:", Oldtotal2)
                            s(3)
                            print("The min of the old data set is:", minold2)
                            s(3)
                            print("The max of the old data set is:", maxold2)
                            s(3)
                            print("The average of the data set is:", old_average6)
                            s(3)
                            print("The standard deviation is:", old_column_list_stdev)
                            s(3)
                            print("For the new data set (with the range filter applied):")
                            s(3)
                            print(New_column_list3)
                            s(3)
                            print("The percentage of data points that fall between the range is:", ((Newtotal6/Oldtotal2)*100), "%")
                            s(3)
                            print("The total number of data points (within the range) is:", Newtotal6)
                            s(3)
                            print("The max of the new data set is:", maxnew6)
                            s(3)
                            print("The min of the new data set is:", minnew6)
                            s(3)
                            print("The average of the new data set is:", new_average6)
                            s(3)
                            print("The standard deviation of the new data set is:", new_column_list_stdev3)
                            s(3)

                        filter11()
            
                        #general statistics function
                    else:
                        nofilter()
                
                        def filter12():
                            Oldtotal2 = len(column_list_filtered)
                            average5 = (sum(column_list_filtered)/Oldtotal2)
                            old_column_list_stdev = stdev(column_list_filtered)
                            maxold2 = max(column_list_filtered)
                            minold2= min(column_list_filtered)
                            print("The n value is:", Oldtotal2)
                            s(3)
                            print("The max is:", maxold2)
                            s(3)
                            print("The min is:", minold2)
                            s(3)
                            print("The average value is:", average5)
                            s(3)
                            print("The standard deviation is:", old_column_list_stdev)
                            s(3)

                        filter12()

