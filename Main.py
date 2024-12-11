import pandas as pd
import sys

def exit():
          print(""" 

                                                                                                        
     ______                    ____  _________________  ____  _____   ______         _____    
 ___|\     \  _____      _____|    |/                 \|    ||\    \ |\     \    ___|\    \   
|     \     \ \    \    /    /|    |\______     ______/|    | \\    \| \     \  /    /\    \  
|     ,_____/| \    \  /    / |    |   \( /    /  )/   |    |  \|    \  \     ||    |  |____| 
|     \--'\_|/  \____\/____/  |    |    ' |   |   '    |    |   |     \  |    ||    |    ____ 
|     /___/|    /    /\    \  |    |      |   |        |    |   |      \ |    ||    |   |    |
|     \____|\  /    /  \    \ |    |     /   //        |    |   |    |\ \|    ||    |   |_,  |
|____ '     /|/____/ /\ \____\|____|    /___//         |____|   |____||\_____/||\ ___\___/  /|
|    /_____/ ||    |/  \|    ||    |   |`   |          |    |   |    |/ \|   ||| |   /____ / |
|____|     | /|____|    |____||____|   |____|          |____|   |____|   |___|/ \|___|    | / 
  \( |_____|/   \(        )/    \(       \(              \(       \(       )/     \( |____|/  
   '    )/       '        '      '        '               '        '       '       '   )/     
        '                                                                              '      
           @arushbaluni -  https://github.com/arushbaluni/EasyBuy

                    """)
          sys.exit()

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
     sl = pd.read_csv('sales.csv')
     
     def ret_sl():
          print(""" 
                What do you want to do next?

      [1] Go to Main Page              [2] Go Back
      [3] Exit
                
           """)
          gb = int(input('----->>'))
          if gb == 1:
               main()
          elif gb == 2:
               sales()
          elif gb == 3:
               exit()

     if S_inp == 1:
          print("$",sl.iloc[0])
          ret_sl()
     
     elif  S_inp == 2:
          print("$",sl.iloc[1])
          ret_sl()

     elif  S_inp == 3:
          print("$",sl.iloc[2])
          ret_sl()

     elif  S_inp == 4:
          print(""" 
       [1] Edit Yesterday's Sale               [2] EditThis Year's Sale
       [3] Edit This Month's Sale              
           """)
          einp = int(input())

          if einp == 1:
               x = int(input("What would you like to change it to? -: "))
               sl.iloc[0] = x
               sl.to_csv('sales.csv', index=False, mode= 'w')
               print('Changed')
               ret_sl()
          elif einp == 2:
               x = int(input("What would you like to change it to? -: "))
               sl.iloc[1] = x
               sl.to_csv('sales.csv', index=False, mode= 'w')
               print('Changed')
               ret_sl()
          elif einp == 3:
               x = int(input("What would you like to change it to? -: "))
               sl.iloc[0] = x
               sl.to_csv('sales.csv', index=False, mode= 'w')
               print('Changed')
               ret_sl()





def stock():

     p = """
     -o----o----o----o----o----o----o----o----o----o----o----o----o-
         ______     ______   ______     ______     __  __    
        /\  ___\   /\__  _\ /\  __ \   /\  ___\   /\ \/ /    
        \ \___  \  \/_/\ \/ \ \ \/\ \  \ \ \____  \ \  _"-.  
         \/\_____\    \ \_\  \ \_____\  \ \_____\  \ \_\ \_\ 
          \/_____/     \/_/   \/_____/   \/_____/   \/_/\/_/ 
                                                     
       
      
      [1] List Product               [2] Find Specific Product
                                                  
     """
     print(p)
     stockk = pd.read_csv('stock.csv', names = ['Product Name', 'Stock'])
     
     def ret_pd():
          print(""" 
                What do you want to do next?

      [1] Go to Main Page              [2] Go Back
      [3] Exit
                
           """)
          gb = int(input('----->>'))
          if gb == 1:
               main()
          elif gb == 2:
               stock()
          elif gb == 3:
               exit()
          
     Pd_inp = int(input("Enter a number between 1-4: "))
     
     if Pd_inp == 1:
          print(stockk)
          ret_pd()
     

     elif  Pd_inp == 2:
          fp = input('Enter the product name: ')
          sr = stockk[stockk['Product Name'] == fp]
          print('                                                  ')
          print('                      ****                        ')
          print(sr)
          ret_pd()



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
               exit()
                    
     St_inp = int(input("Enter a number between 1-4: "))
     
     if St_inp == 1:
          print(emp)
          ret_st()
     
     elif  St_inp == 2:
          print('')
          ret_st()
     elif  St_inp == 3:
          workers = emp[emp['Job Title'] == 'Worker']
          print(workers)
          ret_st()

     elif  St_inp == 4:
          restockers = emp[emp['Job Title'] == 'Restocker']
          print(restockers)
          ret_st()
#employee done     
     

def liab():
     print(""" 
     -o----o----o----o----o----o----o----o----o----o----o----o----o-
                __   _      __   _   __  _ __  _       
               / /  (_)__ _/ /  (_) / / (_) /_(_)__ ___
              / /__/ / _ `/ _ \/ / / / / / __/ / -_|_-<
             /____/_/\_,_/_.__/_/ /_/ /_/\__/_/\__/___/
                                          
           [1] List Liabilities             [2] Go bcak to Main

          """)
     x= int(input())

     def ret_lb():
          print(""" 
                What do you want to do next?

           [1] Go to Main Page              [2] Exit
                
           """)
          gb = int(input('----->>'))
          if gb == 1:
               main()
          elif gb == 2:
               exit()

     if x == 1:
          liabi = pd.read_csv('Liab.csv', names= ['Liability Name', 'Amount', 'Due Date'])
          print(liabi)
          ret_lb()
     elif x==2:
          exit()

     

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
     
     def ret_pd():
          print(""" 
                What do you want to do next?

      [1] Go to Main Page              [2] Go Back
      [3] Exit
                
           """)
          gb = int(input('----->>'))
          if gb == 1:
               main()
          elif gb == 2:
               prod()
          elif gb == 3:
               exit()
          
     Pd_inp = int(input("Enter a number between 1-4: "))
     
     if Pd_inp == 1:
          print(product)
          ret_pd()
     
     elif  Pd_inp == 2:
          print('')
          ret_pd()

     elif  Pd_inp == 3:
          fp = input('Enter the product name: ')
          sr = product[product['Product Name'] == fp]
          print('                                                  ')
          print('                      ****                        ')
          print(sr)
          ret_pd()

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
    print("------------------------------------------------------------------------------------------------")
    print("")
    print("")
    main()
#help done

#main def to redirect


def main():
     x = """
----------------------------------------------------------------------
     ___________                         __________                
     \_   _____/_____     ______ ___.__. \______   \ __ __  ___.__.
      |    __)_ \__  \   /  ___/<   |  |  |    |  _/|  |  \<   |  |
      |        \ / __ \_ \___ \  \___  |  |    |   \|  |  / \___  |
     /_______  /(____  //____  > / ____|  |______  /|____/  / ____|
             \/      \/      \/  \/              \/         \/          
          
"""
     print(x)
     print('                  Welcome to Easy Buy Shop Manager!' )
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
          main()
          




#def separation **************************************************************************


x = """
----------------------------------------------------------------------
     ___________                         __________                
     \_   _____/_____     ______ ___.__. \______   \ __ __  ___.__.
      |    __)_ \__  \   /  ___/<   |  |  |    |  _/|  |  \<   |  |
      |        \ / __ \_ \___ \  \___  |  |    |   \|  |  / \___  |
     /_______  /(____  //____  > / ____|  |______  /|____/  / ____|
             \/      \/      \/  \/              \/         \/          
          
"""
print(x)
print('                  Welcome to Easy Buy Shop Manager!' )
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
     main()
