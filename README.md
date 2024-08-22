# Product Management System

This Python script provides a basic Product Management System using pandas for handling CSV files. It allows you to manage an inventory of products with functionalities for adding, viewing, updating, deleting, and sorting products.

## Features

- **Add a New Product**: Add products with SKU, Name, Brand, and Quantity.
- **View All Products**: Display all products in a formatted table.
- **Update a Product**: Modify the details of an existing product based on SKU.
- **Delete a Product**: Remove a product from the inventory using its SKU.
- **Sort by Quantity**: Sort products in ascending order by quantity.
- **Sort by Name**: Sort products in alphabetical order by name.

## Dependencies

- **Python 3.x**
- **pandas**: For data handling and CSV file operations. Install it using:

  ```
  pip install pandas
  ```

## Functions Usage

### `add_product()`

Prompts the user to enter details for a new product and adds it to `example.csv`.

### `view_products()`

Displays all products in a tabular format. If the file is empty, it notifies the user.

### `update_product()`

Allows updating the Name, Brand, or Quantity of an existing product identified by SKU.

### `delete_product()`

Deletes a product from `example.csv` based on the SKU provided by the user.

### `sort_products_by_quantity()`

Sorts the products by Quantity in ascending order and updates the CSV file.

### `sort_products_by_name()`

Sorts the products by Name in alphabetical order and updates the CSV file.

## Running the Script

1. **Clone the Repository**

   ```
   git clone https://github.com/yourusername/product-management.git
   cd product-management
   ```

2. **Run the Script**

   ```
   python product_management.py
   ```

3. **Interact with the Menu**

   Choose from the available options to manage the product inventory.
