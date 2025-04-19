# Store Management System

A Python-based application for managing store operations, including inventory tracking, product management, and order processing.

## Features

- **Product Management**: Create and display product information including ID, name, price, and description
- **Inventory Management**: Track product quantities, add and remove products from inventory
- **Order Processing**: Create orders, add products to orders, and calculate order totals
- **User Authentication**: Basic user management with username and password

## Project Structure

```
store-management/
│
├── src/
│   ├── inventory.py - Inventory management functionality
│   ├── main.py - Main application entry point
│   ├── order.py - Order creation and management
│   ├── product.py - Product class definition
│   ├── user.py - User authentication and management
│   └── utils.py - Utility functions
│
├── LICENSE
└── README.md
```

### Main Menu Options

1. **View Products**: Display all available products
2. **View Inventory**: Check current inventory levels
3. **Create Order**: Create a new order by adding products
4. **Exit**: Quit the application

## How It Works

The system follows an object-oriented design with the following key components:

- **Product**: Represents a product with ID, name, price, and description
- **Inventory**: Manages product quantities and stock levels
- **Order**: Handles order creation and calculates totals
- **User**: Basic user management functionality

## Example Workflow

1. Launch the application
2. View available products
3. Check inventory levels
4. Create an order by selecting products and specifying quantities
5. View order details and total cost

## Future Improvements

- Database integration for persistent data storage
- Enhanced user authentication and authorization
- Web-based interface
- Order history and reporting features
- Payment processing integration

## License

[MIT](./LICENSE)