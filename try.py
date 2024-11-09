def show_sales_options():
    print("Sales Operations:")
    print("[1] Record a sale")
    print("[2] View sales report")
    # Add more sales-related options here

def show_liabilities_options():
    print("Liabilities Operations:")
    print("[1] Record a liability")
    print("[2] View liabilities report")
    # Add more liabilities-related options here

def show_stock_options():
    print("Stock Operations:")
    print("[1] Add new stock")
    print("[2] View stock levels")
    # Add more stock-related options here

def show_product_options():
    print("Product Operations:")
    print("[1] Add new product")
    print("[2] View product list")
    # Add more product-related options here

def show_employee_options():
    print("Employee Operations:")
    print("[1] Add new employee")
    print("[2] View employee details")
    # Add more employee-related options here

def show_help():
    print("HELP TEXT: Choose the operation you want to perform by entering the corresponding number.")
    print("1 - Sales related operations")
    print("2 - Liabilities management")
    print("3 - Stock management")
    print("4 - Product related operations")
    print("5 - Employee related operations")
    print("6 - Help (Displays this help message)")

def main():
    x = """
----------------------------------------------------------------------
     __      __                      __    __________                
    /  \    /  \___________  _______/  |_  \______   \__ __ ___.__.
   \   \/\/   /  _ \_  __ \/  ___/\   __\  |    |  _/  |  <   |  |
    \        (  <_> )  | \/\___ \  |  |    |    |   \  |  /\___  |
     \__/\  / \____/|__|  /____  > |__|    |______  /____/ / ____|
          \/                   \/                 \/       \/     
    """
    print(x)
    print('                  Welcome to Worst Buy Shop Manager!' )
    print('                                                    ' )
    print('                Choose the operation you want to perform' )

    Ops = """
           [1] Sales related                [2] Liabilities
           [3] Stock                        [4] Products Related
           [5] Employees related            [6] Help
    """
    print(Ops)

    while True:  # Keep asking for input until user exits
        try:
            inp1 = int(input("Enter your choice (1-6): "))
            if inp1 == 1:
                show_sales_options()
            elif inp1 == 2:
                show_liabilities_options()
            elif inp1 == 3:
                show_stock_options()
            elif inp1 == 4:
                show_product_options()
            elif inp1 == 5:
                show_employee_options()
            elif inp1 == 6:
                show_help()
            else:
                print("Invalid choice. Please enter a number between 1 and 6.")
            
            # Optionally, you can ask if they want to perform another operation or exit
            cont = input("Do you want to perform another operation? (yes/no): ").lower()
            if cont != 'yes':
                print("Goodbye!")
                break
        
        except ValueError:
            print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()
