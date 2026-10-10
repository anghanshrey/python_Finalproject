import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

class librarymanagementsystem:

    def __init__(self):

        self.data = None

    def load_dataset(self, filename):

        if not os.path.exists(filename):
            print("\n CSV File does not exist.")
            return

        self.data= pd.read_csv(filename)

        print("Dataset loaded Suessfully.")


    def clear_data(self):

        if self.data is None or self.data.empty: 
            print("Dataset is Empty") 
            return 

        while True:
            print("Option")
            print(
                f"\n1. Total missing data"
                f"\n2. fill numeric data"
                f"\n3. fill categority data"
                f"\n4. exit"
            )

            try:
                choice = int(input("Enter your Chocie :"))
            except (ValueError, OSError) as e:
                print("Error :", e)

            match choice:
                case 1: 
                    print("\nTotal Null Values per Column:")
                    print(self.data.isnull().sum())
                case 2: 
                    numeric_cols = self.data.select_dtypes(include=[np.number]).columns
                    self.data[numeric_cols] = self.data[numeric_cols].fillna(self.data[numeric_cols].mean())
                    print("Numeric null values filled with column mean.")
                case 3: 
                    cat_cols = self.data.select_dtypes(include=['object']).columns
                    for col in cat_cols:
                        self.data[col] = self.data[col].fillna(self.data[col].mode()[0] if not self.data[col].mode().empty else "Unknown")
                    print("Categorical null values filled with mode.")
                case 4: 
                    print("Returning to Main Menu") 
                    break 
                case _: 
                    print("Please Enter a Number between 1 and 4!!") 
        


    def calculate_Stat(self):
        if self.data is None or self.data.empty: 
            print("Dataset is Empty") 
            return 
        
        if 'Borrowing Duration (Days)' in self.data.columns:
            borrowing_duration = self.data['Borrowing Duration (Days)'].dropna().to_numpy()
            if len(borrowing_duration) > 0:
                print("\n--- Statistics for Borrowing Duration ---")
                print(f"Mean: {np.mean(borrowing_duration):.2f} days")
                print(f"Median: {np.median(borrowing_duration):.2f} days")
                print(f"Max: {np.max(borrowing_duration)} days")
                print(f"Std : {np.std(borrowing_duration)} days")
                print(f"variance : {np.var(borrowing_duration)} days")
                print(f"Sum : {np.sum(borrowing_duration)} days")
            else:
                print("No data available in Borrowing Duration (Days).")
        else:
            print("Column Borrowing Duration (Days) not found.")



    def filter(self):
        if self.data is None or self.data.empty: 
            print("Dataset is Empty") 
            return 
        
        while True:
            print("Option")
            print(
                    f"\n1. Grouping data by book Genre"
                    f"\n2. Aggregating metric total or average"
                    f"\n3. exit"
                )
        
            try:
                choice = int(input("Enter your Chocie :"))
            except (ValueError, OSError) as e:
                print("Error :", e)
        
            match choice:
                case 1:
                    if 'Genre' in self.data.columns and 'Book Title' in self.data.columns:
                        genre_counts = self.data.groupby('Genre')['Book Title'].count()
                        print("\nNumber of Books per Genre:")
                        print(genre_counts)
                    else:
                        print("Required columns ('Genre' or 'Book Title') missing.")
                case 2:
                    if 'Genre' in self.data.columns and 'Borrowing Duration (Days)' in self.data.columns:
                        agg_data = self.data.groupby('Genre')['Borrowing Duration (Days)'].agg(['sum', 'mean'])

                        agg_data.columns = ['Total Borrowing Days', 'Average Borrowing Days']
                        print("\nBorrowing Duration Aggregation by Genre:")
                        print(agg_data)
                    else:
                        print("Required columns missing for aggregation.")
                        
                case 3:
                    print("Returning to Main Menu")
                    break
                case _:
                    print("Please Enter 1 - 3 Number!!")
        

    def generate_report(self):
        if self.data is None or self.data.empty: 
            print("Dataset is Empty. Cannot generate report.") 
            return 
        
        print("\nGenerating report")
        
        total_records = len(self.data)
        
        most_popular_genre = "N/A"
        if 'Genre' in self.data.columns:
            most_popular_genre = self.data['Genre'].mode().iloc[0] if not self.data['Genre'].mode().empty else "N/A"
            
        avg_duration = 0
        total_duration = 0
        if 'Borrowing Duration (Days)' in self.data.columns:
            avg_duration = self.data['Borrowing Duration (Days)'].mean()
            total_duration = self.data['Borrowing Duration (Days)'].sum()

        # 3. Create the text content for the report
        report_content = (
            f"Total Transactions Processed : {total_records}\n"
            f"Most Popular Book Genre      : {most_popular_genre}\n"
            "--------------------------------------------------\n"
            "BORROWING METRICS:\n"
            f"  - Total Days Borrowed      : {total_duration:.1f} Days\n"
            f"  - Average Borrowing Period  : {avg_duration:.2f} Days\n"
        )
        print(report_content)

    def chart(self):
        print("========== Matplotlib / seaborn Chart ================")

        while True:
            print("Option ")
            print(
                f"\n1. Bar Chart"
                f"\n2. Line Chart"
                f"\n3. pie Chart"
                f"\n4. Heatmap"
                f"\n5. Exit"
            )

            try:
                choice = int(input("Enter your Choice: "))
            except (ValueError, OSError) as e:
                print("Error :", e)
                continue
                
            match choice:
                case 1:
                    if 'Book Title' in self.data.columns:
                        top_books = self.data['Book Title'].value_counts().head(5)
                        
                        plt.figure(figsize=(10, 5))
                        plt.bar(top_books.index, top_books.values , color = 'Green', label = 'Top 5 Books')
                        plt.title('Top 5 Most Borrowed Books')
                        plt.xlabel('Number of Times Borrowed')
                        plt.ylabel('Book Title')
                        plt.legend()
                        plt.tight_layout()
                        plt.show()
                    else:
                        print("Book Title column missing from dataset.")
                        
                case 2:
                    if 'Date' in self.data.columns:
                        dates = pd.to_datetime(self.data['Date'])
                        monthly_trends = self.data.groupby(dates.dt.to_period('M')).size()
                        
                        plt.figure(figsize=(10, 5))
                        plt.plot(monthly_trends.index, monthly_trends.values, marker='o', color='blue', linewidth=2)
                        plt.title('Borrowing Trends Over Months')
                        plt.xlabel('Month')
                        plt.ylabel('Number of Borrowings')
                        plt.grid(True, linestyle='--', alpha=0.6)
                        plt.tight_layout()
                        plt.show()
                    else:
                        print("Date column missing from dataset.")
                        
                case 3:
                    if 'Genre' in self.data.columns:
                        genre_counts = self.data['Genre'].value_counts()
                        
                        plt.figure(figsize=(8, 8))
                        plt.pie(genre_counts.values, labels=genre_counts.index, autopct='%1.1f%%', startangle=90)
                        plt.title('Distribution of Books Borrowed by Genre')
                        plt.tight_layout()
                        plt.show()
                    else:
                        print("Genre column missing from dataset.")
                        
                case 4:
                    if 'Date' in self.data.columns:
                        df_copy = self.data.copy()
                        df_copy['Date'] = pd.to_datetime(df_copy['Date'])
                        df_copy['Day of Week'] = df_copy['Date'].dt.day_name()
                        df_copy['Month'] = df_copy['Date'].dt.strftime('%b')
                        
                        days_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
                        
                        plt.figure(figsize=(10, 6))
                        sns.heatmap(days_order.corr(), annot=True, fmt='%1.1f%%', cmap='inferno')
                        plt.title('Borrowing Activity Heatmap (Day vs Month)')
                        plt.tight_layout()
                        plt.show()
                    else:
                        print("Date column missing from dataset.")
                        
                case 5:
                    print("Returning to Main Menu")
                    break
                case _:
                    print("Please Enter a Number between 1 and 5!!")






    def main(self):
        print("============== Library Management System ===============")

        while True:
            print(
                f"Option"
                f"\n1. Load Dataset"
                f"\n2. clearing Dataset"
                f"\n3. Calculate Statistics"
                f"\n4. filter transactions"
                f"\n5. generate report"
                f"\n6. create chart"
                f"\n7. Exit"
            )

            try:
                choice = int(input("Enter Your Choice :"))
            except (ValueError, OSError) as e:
                print("Error : ", e)
                return

            match choice:
                case 1:
                    filename = input("Enter File name (.csv) : ")
                    self.load_dataset(filename)
                case 2:
                    self.clear_data()
                case 3:
                    self.calculate_Stat()
                case 4:
                    self.filter()
                case 5:
                    self.generate_report()
                case 6:
                    self.chart()
                case 7:
                    print("Thank you Library management System.")
                    break
                case _:
                    print("Please Enter 1 - 7 Number!!")

if __name__ == "__main__":
    system = librarymanagementsystem()

    system.main()
