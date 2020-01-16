#Reads and handles the csv dataset 
import pandas as p

class dataHandler:

    @staticmethod
    def productDataframe():
        #The Dataset
        Dataset = "open_units.csv"

        #Read the file
        data=p.read_csv("../BallmerPeak/Dataset/Data/" + Dataset, index_col=False)
        
        #Create a dataframe with desired columns and set index column to Product 
        df1 = p.DataFrame(data, columns=['Product','Brand', 'Category', 'Style', 'Volume','ABV'])
        
        return df1


    #This method returns a cell value based on product name as input value, 
    #and desired value Brand, Category, Style, Volume, ABV.
    #Usage -> dataHandler.getValue('Carlsberg Export', Category)
    #TODO:      1) Try to apply Pandas.DataFrame.loc instead.
    #           2) Apply Tolower to Dataframe 
    #           3) Figure out how to do a contains method instead    
    @staticmethod
    def getValue(product, output):
    
        temp_DF = dataHandler.productDataframe()    #Create a new DataFrame, productDataframe() returns a DataFrame
        temp_DF.drop_duplicates(keep='first')       #Drop duplicates
        temp_DF.dropna()                            #Drop NaN
        

        #Find match in dataframe based in input value
        if output == 'ABV' :
            temp = temp_DF['ABV'].where(temp_DF['Product'] == product)
        elif output == 'Brand' :
            temp = temp_DF['Brand'].where(temp_DF['Product'] == product)
        elif output == 'Category' : 
            temp = temp_DF['Category'].where(temp_DF['Product'] == product)
        elif output == 'Style' : 
            temp = temp_DF['Style'].where(temp_DF['Product'] == product)
        elif output == 'Volume' : 
            temp = temp_DF['Volume'].where(temp_DF['Product'] == product)
        
        #make new dataframe with new data
        df2 = p.DataFrame(temp)                     #Create a DataFrame from temp data
        df2.dropna(inplace=True)                    #Drop NaN
        df2.drop_duplicates(keep='first')           #Drop all duplicates
        df2.reset_index(drop=True, inplace=True)    #Reset the index to 0
  
        position = 0                                #Since indexes are reset, the element we are looking for is at the 0th position

        result = df2.at[position,output]            #Get the result

        print(result)
        #return result                               #Return the result

