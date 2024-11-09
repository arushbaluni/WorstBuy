import pandas as pd
import sys



def sales():
     S_opt = """
         
      **********************************************************

                          ___       _        
                         / __| __ _| |___ ___
                         \__ \/ _` | / -_|_-<
                         |___/\__,_|_\___/__/
                          
 

       [1] Yesterday's Sale               [2] This Year's Sale
       [3] This Month's Sale              [4] Edit Sales Data

      """
     print(S_opt)

     S_inp = int(input("Enter a number between 1-4: "))
     
     

     if S_inp == 1:
          print('')
     
     elif  S_inp == 2:
          print('')

     elif  S_inp == 3:
          print('')

     elif  S_inp == 4:
          print('')

def stock():
     print('stock')

def employee():
     e = """
     ****************************************************
             ___             ___ _         __  __      
      _/\_  / _ \ _  _ _ _  / __| |_ __ _ / _|/ _| _/\_
      >  < | (_) | || | '_| \__ \  _/ _` |  _|  _| >  <
       \/   \___/ \_,_|_|   |___/\__\__,_|_| |_|    \/ 
                                                       
       
      [1] List Staff              [2] Add/Delete/Modify Data
      [3] List Workers only       [4] List Restockers Only
                                                  
     """
     print(e)
     emp = pd.read_csv('employee.csv', names=['Name', 'Job Title'])

     def ret_st():
          print(""" 
                What do you want to do next?

      [1] Go to Main Page              [2] Go Back
      [3] Exit
                
           """)
          gb = int(input('----->>'))
          if gb == 1:
               main()
          elif gb == 2:
               employee()
          elif gb == 3:
               print(""" 

          U _____ u __  __               _____               _   _     ____      
          \| ___"|/ \ \/"/      ___     |_ " _|     ___     | \ |"| U /"___|u    
           |  _|"   /\  /\     |_"_|      | |      |_"_|   <|  \| |>\| |  _ /    
           | |___  U /  \ u     | |      /| |\      | |    U| |\  |u | |_| |     
           |_____|  /_/\_\    U/| |\u   u |_|U    U/| |\u   |_| \_|   \____|     
           <<   >>,-,>> \\_.-,_|___|_,-._// \\_.-,_|___|_,-.||   \\,-._)(|_      
          (__) (__)\_)  (__)\_)-' '-(_/(__) (__)\_)-' '-(_/ (_")  (_/(__)__)  
                     
           @arushbaluni -  https://github.com/arushbaluni/WorstBuy

                    """)
               sys.exit()
                    
     St_inp = int(input("Enter a number between 1-4: "))
     
     if St_inp == 1:
          print(emp)
     
     elif  St_inp == 2:
          print('')

     elif  St_inp == 3:
          workers = emp[emp['Job Title'] == 'Worker']
          print(workers)

     elif  St_inp == 4:
          restockers = emp[emp['Job Title'] == 'Restocker']
          print(restockers)
#employee done     
     

def liab():
     print('lib')

def prod():
     p = """
     -o----o----o----o----o----o----o----o----o----o----o----o----o-
          _     ______              _            _            _    
       /\| |/\  | ___ \            | |          | |        /\| |/\ 
       \ ` ' /  | |_/ / __ ___   __| |_   _  ___| |_ ___   \ ` ' / 
      |_     _| |  __/ '__/ _ \ / _` | | | |/ __| __/ __| |_     _|
       / , . \  | |  | | | (_) | (_| | |_| | (__| |_\__ \  / , . \ 
       \/|_|\/  \_|  |_|  \___/ \__,_|\__,_|\___|\__|___/  \/|_|\/
       
      
      [1] List Product               [2] Add/Remove Product
      [3] Find Specific Product      [4] Change Price
                                                  
     """
     print(p)
     product = pd.read_csv('prod.csv', names = ['Product Name', 'Price'])

          
     Pd_inp = int(input("Enter a number between 1-4: "))
     
     if Pd_inp == 1:
          print(product)
     
     elif  Pd_inp == 2:
          print('')

     elif  Pd_inp == 3:
          fp = input('Enter the product name: ')
          sr = product[product['Product Name'] == fp]
          print('                                                  ')
          print('                      ****                        ')
          print(sr)

     elif  Pd_inp == 4:
          Chp = input("Please enter the name of the product you'd like to change the price of:- ")
          cp = product.loc[product['Product Name'] == Chp, 'Price']
          print('Current price: ' + cp)
          np = input('')
          sr = product[product['Product Name'] == fp]


def help():
    print("Choose the operation you want to perform by entering the corresponding number.")
    print("1 - Sales related operations")
    print("2 - Liabilities management")
    print("3 - Stock management")
    print("4 - Product related operations")
    print("5 - Employee related operations")
    print("6 - Help (Displays this help message)")
#help done

#main def to redirect


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
     inp1= int(input())
     inp1_str = str(inp1)

     if inp1 == 1 :
          sales()

     elif inp1 == 2 :
          liab()

     elif inp1 == 3 :
          stock()

     elif inp1 == 4 :
          prod()

     elif inp1 == 5 :
          employee()

     elif inp1 == 6 :
          help()

     else:
          print("Invalid choice. Please enter a number between 1 and 6. Type 'help' for help.")
          inp2 = str(input())

          if inp2 == 'help':
            print("HELP TEXT")




#def separation **************************************************************************


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
inp1= int(input())
inp1_str = str(inp1)

if inp1 == 1 :
     sales()

elif inp1 == 2 :
     liab()

elif inp1 == 3 :
     stock()

elif inp1 == 4 :
     prod()

elif inp1 == 5 :
     employee()

elif inp1 == 6 :
     help()

else:
     print("Invalid choice. Please enter a number between 1 and 6. Type 'help' for help.")
     inp2 = str(input())

     if inp2 == 'help':
       print("HELP TEXT")



