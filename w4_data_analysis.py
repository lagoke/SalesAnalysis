import csv

import pandas as pd
import numpy as np

import matplotlib.pyplot as matplot


try:

    with open('autosales.csv') as file:
        record_counter= 0  # Set counter to 0
        readEachLine= csv.reader(file)
        heading= next(readEachLine) # skip the heading of the dataset
        for record in readEachLine:
            OrderNumber = int(record[0])
            QuantityOrdered= int(record[1])
            PriceEach= float(record[2])
            OrderLineNumber= int(record[3])
            Sales= float(record[4])

            print(OrderNumber, QuantityOrdered, PriceEach, OrderLineNumber, Sales)

            record_counter = record_counter + 1
        print(f"Total number of records = {record_counter}")
        file.close()    

except:
    print("file not found")



# Reading the Autosales dataset with Numpy and Pandas libraries

datafile= np.loadtxt('autosales.csv',delimiter=',',skiprows=1) # Use NumPy library to read the autosales dataset

df= pd.read_csv('autosales.csv') # Use Pandas library to read the autosales dataset



#  non-trivial data transformation (using log function and scaling) 

def transform_with_natural_log():
    # Calculate the natural logarithm
    # on the 'sales' column
    df['Natural_logarithm_of_Sales_Column'] = np.log(df['SALES'])
    print(df)

    df['Natural_logarithm_of_Sales_Column'].hist()
    matplot.show()


def transform_with_scaling():
    scaling = df.copy()
    min_sold= np.min(scaling['SALES'])
    max_sold = np.max(scaling['SALES'])
    scaling['transformed_sales'] = (scaling['SALES'] - min_sold) / (max_sold - min_sold)
    print(scaling)

    scaling['transformed_sales'].hist()
    matplot.show()



#  non-trivial operation of data reduction (minimum and maximum, then mean)

def min_max():
    min_value_from_columnn= np.min(datafile,axis=0) # Minimum value, column-wise, full array)
  

    max_value_from_columnn= np.max(datafile,axis=0) # Minimum value, column-wise, full array)
  
    
 
    print(f"Minimum value column wise = {min_value_from_columnn}")

    print(f"Maximum value column wise = {max_value_from_columnn}")



# non-trivial operation of data reduction (mean)

def reduction_with_mean():
    meanvalue = df['SALES'].mean() # full column
    print(meanvalue)


#transform_with_natural_log()
transform_with_scaling()
min_max()
reduction_with_mean()
