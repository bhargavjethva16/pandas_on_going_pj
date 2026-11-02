import pandas as pd
import matplotlib.pyplot as plt


class DataAnalysis :

    def __init__(self):

        self.data = None
        self.graph = None

    def load_data(self):
        try :
            print()
            path = input("Enter the pata of the dataset (CSV File) :   ")
            self.data = pd.read_csv(path)
            print()
            print("Dataset loaded successfully")
            print()
            return self.data
        except : 
            print("something went wrong")
        

    def explore_data(self):

        try:

            print()
            print("--- Explore Data ---")
            print("1. Display the first 5 Rows")
            print("2. Display the last 5 Rows")
            print("3. Display column names")
            print("4. Display Datatypes")
            print("5. Display basic info")
            print()

            opt = int(input("Enter your No. :   "))

            if opt == 1 : 

                print()
                print(self.data.head(5))
                print()

            elif opt == 2 :

                print()
                print(self.data.tail(5))
                print()

            elif opt == 3 :

                print()
                print(self.data.columns)
                print()

            elif opt == 4 :

                print()
                print(self.data.dtypes)
                print()

            elif opt == 5 : 

                print()
                print(self.data.info()) 
                print()

        except:
            print("Something went wrong")

    def clean_data(self):

        print()
        
        if self.data is None:
            print("Load data first ")
            return
        print()
        
        try:

            print()
            print("--- Handle Missing Data --- ")
            print("1. Display Rows with Missing values")
            print("2. Fill missing values with mean")
            print("3. Drop rows with missing values")
            print("4. Replace missing values with specific values")
            print()

            ch = int(input("Enter your No. :-   "))
            print()

            if ch == 1 :
                
                if self.data.isnull().empty :
                    
                    print()
                    print("No missing values found in the Dataset")
                    print()
                
                else:

                    print()
                    null = self.data.isnull().sum()
                    print(null)
                    print()

            elif ch == 2 :

                print()
                self.data = self.data.fillna(self.data.mean())
                print(self.data.head())
                print()

            elif ch == 3 :

                print()
                print("- - - Before Cleaning - - -")
                print()
                self.data = self.data.isnull().sum()
                print()
                print(self.data.isnull().sum())
                print()
                self.data = self.data.dropna()
                print()
                print("- - - After Cleaning - - - ")
                print()
                print(self.data.isnull().sum())
                print()

            elif ch == 4 : 

                print()
                replace = input("Enter a value to replace it with missing value :-  ")
                self.data = self.data.fillna(replace)
                print(f"Missing values replaced with {replace} successfully !")
                print()

            else :

                print(" Invalid choice ! !")
                print()

        except:
            
            print()
            print("Something went wrong, check the values in the dataset first")
            print()


    def data_frame_op():
        pass









    

    while True:

        print()
        print("="*75)
        print("================= Data Analysis and Visualisation Program =================")
        print("="*75)
        print("\n")

        print("Select an option-")
        print()
        print("1. Load Dataset")
        print("2. Explore Data")
        print("3. Perform DataFrame Operations")
        print("4. Handle Missing Data")
        print("5. Generate Descriptive Statistics")
        print("6. Data visualisation")
        print("7. Save Visualisaton")
        print("8. Exit")
        print()
        print("-"*75,"|")
        print()

        choice = int(input("Enter your choice:-  "))
        print()

        if choice == 1 : 
            
            pass
        
        elif choice == 2 :

            pass

        elif choice == 3 :

            pass

        elif choice == 4 :

            pass

        elif choice == 5 :

            pass

        elif choice == 6 :

            pass

        elif choice == 7 :

            pass

        elif choice == 8 :

            print()
            print("Thanks for using the Data Analysis and Visualisation Program !!! ")
            print()
            print("Exiting the Program...")
            print("\n")
            print("+"*197)
            print("="*197)
            print("-"*197)
            print()
            break



            


       




















