import pandas as pd
import os

file_path = 'example.csv'
class product:
    def __init__(self,SKU,Name,Brand,Quantity):
        self.SKU=SKU
        self.Name=Name
        self.Brand=Brand
        self.Quantity=Quantity

def create_new_prod():
    print("Enter the sku,name,brand,quantity")
    s,q,n,b=input().split(" ")
    x= product(s,q,n,b)
    dict={
        'SKU':[x.SKU],
        'Name':[x.Name],
        'Brand':[x.Brand],
        'Quantity':[int(x.Quantity)]

    }
    return dict
# Display the DataFrame
# print(df)
def add_product():
    data=create_new_prod()
    new_df = pd.DataFrame(data)

    if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
        existing_df = pd.read_csv('example.csv')
        updated_df = pd.concat([existing_df, new_df], ignore_index=True)
    
    else:
        updated_df = new_df
    updated_df.to_csv('example.csv', index=False)


def load_products(file_path):
    """Load products from the CSV file."""
    if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
        return pd.read_csv(file_path)
    else:
        # If the file is empty or does not exist, return an empty DataFrame with expected columns
        return pd.DataFrame(columns=['SKU', 'Name', 'Price', 'Quantity'])

def save_products(df, file_path):
    """Save the DataFrame to the CSV file."""
    df.to_csv(file_path, index=False)


def view_products():
    df = load_products(file_path)
    
    if df.empty:
        print("No products available.")
        return
    
    # Calculate column widths
    col_widths = {col: max(df[col].astype(str).map(len).max(), len(col)) for col in df.columns}
    
    # Print header
    header = '| ' + ' | '.join(f'{col:{col_widths[col]}}' for col in df.columns) + ' |'
    separator = '+-' + '-+-'.join('-' * col_widths[col] for col in df.columns) + '-+'
    
    print(separator)
    print(header)
    print(separator)
    
    # Print rows
    for _, row in df.iterrows():
        print('| ' + ' | '.join(f'{str(row[col]):{col_widths[col]}}' for col in df.columns) + ' |')
    
    print(separator)


def update_product():
    l=[]
    if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
        df=pd.read_csv('example.csv')
        
        sku=input("enter the sku id of the product")
        for i in df['SKU']:
            l.append(i)
        

        if sku in l:
            print("1) update Name")
            print("2) update Brand")
            print("3) update Quantity")
            choice = input("Select an option: ")
        
            if choice == '1':
                n=input("Enter new product Name: ")
                df.loc[df['SKU']==sku,'Name']=n
            elif choice == '2':
                b=input("Enter new product Brand: ")
                df.loc[df['SKU']==sku,'Brand']=b
            elif choice == '3':
                q=int(input("Enter new product Quantity: "))
                df.loc[df['SKU']==sku,'Quantity']=int(q)
            else:
                print("Invalid option, please try again.")
            #save
            df.to_csv('example.csv', index=False)
        else:
            print("sku not found")
    else:
        print("file empty")
    return

def delete_product():
    """Delete a row with the given SKU from the DataFrame."""
    sku=input("enter the sku =>")
    # Load the products from the CSV file
    df = load_products(file_path)

    # Check if the DataFrame is empty
    if df.empty:
        print("The file is empty or does not exist.")
        return
    

    if sku not in df['SKU'].values:
        print(f"SKU {sku} not found.")
        return
    # Delete the row where SKU matches
    df = df[df['SKU'] != sku]
    save_products(df,file_path)

def sort_products_by_quantity():
    """Sort the products by 'Quantity' in ascending order."""
    df = load_products(file_path)
    
    if df.empty:
        print("No products available to sort.")
        return
    # Convert 'Quantity' column to numeric (if necessary) and sort
    df['Quantity'] = pd.to_numeric(df['Quantity'], errors='coerce')
    df_sorted = df.sort_values(by='Quantity', ascending=True)

    # Save the sorted DataFrame back to the CSV file
    save_products(df_sorted, file_path)

    # Display the sorted products
    print("Products sorted by quantity in ascending order:")
    view_products()
    save_products(df,file_path)

def sort_products_by_name():
    """Sort the products by 'Quantity' in ascending order."""
    df = load_products(file_path)
    
    if df.empty:
        print("No products available to sort.")
        return
    
    df_sorted = df.sort_values(by='Name', ascending=True)

    # Save the sorted DataFrame back to the CSV file
    save_products(df_sorted, file_path)

    # Display the sorted products
    print("Products sorted by quantity in ascending order:")
    view_products()
    save_products(df,file_path)

def main_menu():
    # load=load_product()
    
    while True:
        print()
        print("Menu:")
        print("1) Add a New Product")
        print("2) View All Products")
        print("3) Update a Product")
        print("4) Delete a Product")
        print("5) Sort by Quantity")
        print("6) Sort by Name")
        print("7) Exit")
        
        choice = input("Select an option: ")
        
        if choice == '1':
            add_product()
        elif choice == '2':
            view_products()
        elif choice == '3':
            update_product()
        elif choice == '4':
            delete_product()
        elif choice == '5':
            sort_products_by_quantity()
        elif choice == '6':
            sort_products_by_name()
        elif choice=='7':
            break
        else:
            print("Invalid option, please try again.")
        


    print("Exiting the menu.")

# Run the main menu
if __name__ == "__main__":
    main_menu()



