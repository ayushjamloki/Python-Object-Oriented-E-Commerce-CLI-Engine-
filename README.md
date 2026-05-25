# 🛒 Python Object-Oriented E-Commerce CLI Engine

A robust, terminal-based e-commerce application built entirely from scratch using **Core Python**. This project focuses on clean software architecture, scalable backend logic, and data persistence without relying on any external web frameworks (like Django or Flask).

It demonstrates a strong foundation in Object-Oriented Programming (OOP) and includes entry-level AI logic integrations like a rule-based chatbot and a product recommendation system.

## 🚀 Key Features

* **Object-Oriented Architecture:** Heavy utilization of Inheritance and Polymorphism to manage different product categories (e.g., Electronics vs. Accessories).
* **Role-Based Access Control:** Built custom Python decorators (like `@admin_only`) to ensure only authorized admin accounts can modify store inventory.
* **Secure Data Persistence:** Utilizes JSON file handling (`users.json`, `cart.json`) to safely store user credentials, cart data, and generate physical `.txt` receipts. *(Note: Sensitive data files are secured via `.gitignore`)*.
* **Intelligent Recommendation Engine:** A dictionary-mapped logic system that suggests related products to users based on their current cart selections.
* **Rule-Based NLP Chatbot:** An integrated help assistant that processes user queries using string manipulation and keyword extraction to provide instant customer support.
* **Advanced Python Concepts:** Implemented Lambda functions for dynamic data sorting and robust `try-except` blocks to prevent system crashes.

## 💻 Tech Stack
* **Language:** Python 3.x
* **Core Concepts:** OOP, Custom Decorators, Lambda Functions, Exception Handling, File I/O
* **Data Storage:** JSON Format

## ⚙️ How to Run Locally

1. Clone the repository to your local machine:
   ```bash
   git clone [https://github.com/ayushjamloki/Python-Object-Oriented-E-Commerce-CLI-Engine.git](https://github.com/ayushjamloki/Python-Object-Oriented-E-Commerce-CLI-Engine.git)