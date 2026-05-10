# Python Data Handling

## Project Overview

This project demonstrates practical data extraction, transformation, and loading (ETL) techniques using Python. The assignment focuses on working with JSON data from both GitHub-hosted files and public REST APIs, and exporting the cleaned datasets into CSV files.

---

## Objectives

The main objectives of this assignment were to:

- Extract JSON data from a publicly hosted GitHub repository
- Consume live REST API endpoints using Python
- Transform nested JSON data into structured DataFrames
- Export cleaned and organized datasets into CSV format
- Demonstrate practical ETL workflow concepts using Python

---

## Python Libraries Used
- `requests` : for sending HTTP requests and extracting API data
- `pandas` :for data manipulation and DataFrame operations
- `json` :for parsing and formatting JSON responses
- `datetime` :for generating timestamped output files

## Tools & Platforms
- GitHub : for hosting raw JSON datasets
- Mockaroo : for generating synthetic employee datasets
- DummyJSON API : for accessing sample REST API data

---

# Project Structure

```plaintext
LUXDEV_WEEK9_ASSIGNMENT/
│
├── data/                              # Raw and processed datasets
│   ├── cart_data_*.csv
│   ├── employee_raw_data_mock.json
│   ├── mock_employee_data_*.csv
│   └── products_data_*.csv
│
├── src/                               # Python source files
│   ├── carts_Api_dummy.py             # Cart API extraction pipeline
│   ├── employee_mock_git.py           # GitHub raw JSON extraction
│   └── product_dummy.py               # Product API extraction pipeline
│
├── Assignment_instructions.txt
├── README.md
└── requirements.txt
```

---

## GitHub JSON Data Extraction

### Synthetic Dataset Generation

A synthetic employee dataset was generated using Mockaroo and exported in JSON format.
The generated JSON dataset was uploaded to a public GitHub repository. A raw GitHub URL was then used to access the file programmatically using Python.

---

### Data Transformation Process

The extracted JSON data was:
1. Retrieved using the `requests` library
2. Parsed into Python objects
3. Converted into a Pandas DataFrame
4. Cleaned and structured appropriately
5. Exported into CSV format

---

### DummyJSON API Integration

Data was extracted from the following DummyJSON API endpoints:

### Process
- Sent a GET request to the API
- Extracted the JSON response
- Flattened nested JSON structures
- Normalized nested product data
- Converted the response into a DataFrame
- Exported the final dataset into CSV format

---

## ETL Workflow Demonstrated

The project follows a simplified ETL (Extract, Transform, Load) pipeline:

### Extract
- Retrieved JSON data from GitHub and REST APIs

### Transform
- Cleaned and normalized nested JSON structures
- Structured the data into tabular DataFrames
- Flattened cart-product relationships

### Load
- Exported transformed datasets into CSV files for further analysis

---
### Key Learning Outcomes

Through this assignment, the following concepts were practiced:

- Working with REST APIs using Python
- Consuming and parsing JSON data
- Data normalization and transformation
- Using Pandas for tabular data handling
- Exporting datasets into CSV format
- Building beginner-level ETL pipelines
---
## Conclusion

This assignment successfully demonstrates how Python can be used for real world data extraction and transformation workflows.