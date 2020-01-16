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

        df2.reset_index(drop=True, inplace=True)    #Reset the index to 0

        position = 0                                #Since indexes are reset, the element we are looking for is at the 0th position

        result = df2.at[position,output]            #Get the result

        return result                               #Return the result


    #This method returns a dataframe of all available beverages with the desired criteria
    #Usage: if you want to see all beverages with a ABV of max 4.5, call:
    #showAvailableBeverages(4.5, 'ABV'):
    @staticmethod
    def showAvailableBeverages(output, search_term):

        temp_DF = dataHandler.productDataframe()                        #Create a new DataFrame, productDataframe() returns a DataFrame

        #locates and returns the rows that satisfies the conditions
        if search_term == 'ABV' :
            beverage_DF = temp_DF.loc[temp_DF['ABV'] <= output]
        elif search_term == 'Volume' :
            beverage_DF = temp_DF.loc[temp_DF['Volume'] <= output]
        else :
            beverage_DF = temp_DF.loc[temp_DF[search_term] == output]

        beverage_DF.reset_index(inplace=True, drop=True)                #reset the index

        return beverage_DF                                              #return the result

    #This method returns a beverage as a list of all availiable attributes, by
    #calling the index position from showAvailableBeverages()
    @staticmethod
    def getBeverageList(output, search_term, position):

        temp_DF = dataHandler.showAvailableBeverages(output, search_term)   #Create a new DataFrame, showAvailableBeverages() returns a DataFrame

        beverage_list = temp_DF.iloc[position].tolist()                     #Chooses a beverage from the dataframe and adds it to a list

        return beverage_list                                                #returns the list


dataHandler.getBeverageList('Cider', 'Category', 0)
