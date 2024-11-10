
# WorstBuy Project

A command-line application that assists with managing various shop operations, including sales, stock, products, and employees.


## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/arushbaluni/WorstBuy.git
    ```
2. Install the necessary Python dependencies:
    ```bash
    pip install pandas
    ```
3. Ensure you have the following CSV files in your project directory:
    - **sales.csv**: Contains sales data
    - **employee.csv**: Contains employee details (Name, Job Title)
    - **prod.csv**: Contains product information (Product Name, Price)

## Usage

To start the program, execute the `main()` function from the console:

```bash
python main.py
```
or

```bash
py main.py
```

Upon running, the main menu will appear, prompting you to choose an operation based on the options provided. Enter a number (1-6) to access different functionalities, and follow the prompts to view or edit data as needed.

## Features

- **Manage Sales**: View and edit daily, monthly, and yearly sales data.
- **Employee Management**: View, add, delete, and categorize employees.
- **Product Management**: Access and update product lists, including prices.
- **Stock Management**: Currently not implemented.
- **Help Menu**: Provides guidance on using the app and explaining any issues or options.

## Sections

### Sales
The **Sales** section allows you to manage sales records, including tracking daily, monthly, and yearly data. It supports adding and deleting sales entries. You can also view specific sales information by selecting the desired time frame.

### Liabilities
The **Liabilities** section tracks outstanding payments or debts associated with the store. You can add, view, and remove liabilities as necessary.

### Stock
In the **Stock** section, you can manage and update product stock levels. The system will prompt you to enter quantities for products and update stock data.

### Products
The **Products** section contains details about available items for sale, including product name and price. You can view or edit the product information, such as updating prices or adding new products.

### Employees
The **Employees** section allows you to view employee details, such as their name and job title. You can also add new employees or delete existing ones.

### Help
The **Help** section provides assistance with using the program, including an overview of each section and common troubleshooting steps.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
