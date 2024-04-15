# IBM Data Engineering Capstone Project
In this project, I was assigned the role of Junior Data Engineer who has recently joined SoftCart, an e-commerce organization. The project offered numerous hands-on labs with a real-world use case that required building an industry standard data analytics platform.
## Objectives
- Create and query data repositories using relational and NoSQL databases such as MySQL and MongoDB.
- Design and populate a data warehouse using PostgreSQL and IBM Db2 and write queries to perform Cube and Rollup operations.
- Analyze data and create a dashboard using Cognos Analytics.
- Extract, Transform, and Load (ETL) processes by creating data pipelines for moving data from relational and NoSQL databases into the data warehouse.
- Perform big data analytics using Apache Spark to make predictions with the help of a machine learning model.
## Project Summary
In this Capstone project, I have:
- designed a data platform using MySQL as an OLTP database and MongoDB as a NoSQL database,
- designed a data warehouse and generated reports from the data,
- designed a reporting dashboard that reflects the key metrics of the business,
- extracted data from OLTP and NoSQL databases, transformed it and loaded it into the data warehouse, and then create an ETL pipeline, and finally,
- created a Spark connection to the data warehouse and then deployed a machine learning model.
## Tools and Technologies
- OLTP database - MySQL
- NoSql database - MongoDB
- Staging Data warehouse – PostgreSQL
- Production Data warehouse – DB2 on Cloud
- Big data platform - Hadoop
- Big data analytics platform – Spark
- Business Intelligence Dashboard - IBM Cognos Analytics
- Data Pipelines - Apache Airflow
## Process
- SoftCart has its website accessible to its customers through various devices like laptops, mobiles and tablets.
- All the transactional data like inventory and sales are stored in the MySQL database server.
- All the catalog data of the products is stored in the MongoDB NoSQL server.
- SoftCart's web server is driven entirely by these two databases.
- Data is periodically extracted from these two databases and put into the staging data warehouse running on PostgreSQL.
- The production data warehouse is on the cloud instance of IBM DB2 server.
- BI teams connect to the IBM DB2 for operational dashboard creation. IBM Cognos Analytics is used to create dashboards.
- SoftCart uses Hadoop cluster as its big data platform where all the data is collected for analytics purposes.
- Spark is used to analyze the data on the Hadoop cluster.
- To move data between OLTP, NoSQL and the data warehouse, ETL pipelines are used and these run on Apache Airflow.
## Assignment Overview
### 01 MySQL OLTP Database

1. Using the given sample data, I designed the schema for the OLTP database by storing data like product ID, customer ID, price, quantity, and timestamp of sales in a sales database.
2. Loaded this data into the OLTP database by importing the data from the downloaded CSV file into the data table using phpMyAdmin.
3. Created an index on the timestamp field and prepared an administrative bash script to export sales data into an SQL file.

### 02 NoSQL Database

1. SoftCart had to store all its e-commerce catalog data in a NoSQL database server. For that, I designed a data platform using MongoDB as the NoSQL database.
2. I created a database ```catalog``` and imported the electronics products data from ```catalog.json``` file into a collection named ```electronics```.
3. Run the test queries on the data and finally exported the required fields (```id```, ```type```, and ```model```) from the ```electronics``` collection into a file names ```electronics.csv```.

### 03 Data Warehousing
#### PostgreSQL Staging Data Warehouse
The company's data is periodically extracted from both the databases, MySQL and MongoDB, and put into staging data warehouse running on PostgreSQL. This data warehouse is used by the company to create business reports like total sales per year per country or total sales per month per category, etc.

1. Designed and created a staging data warehouse environment using PgAdmin and PostgreSQL.
2. Designed a Star Schema for the warehouse by identifying the columns for the various dimension and fact tables in the schema. Prepared this design using pgAdmin ERD design tool and ensured that the table can generate yearly, monthly, daily, and weekly reports.
3. Exported the schema SQL and create the schema in a database named ```staging```.

#### IBM DB2 Production Data Warehouse

1. Created an instance of IBM DB2 and loaded the data provided by the company into the tables in CSV format.
2. Wrote aggregation queries on the loaded data by creating a grouping sets query, rollup query, and cube query.
3. Created a Materialized Query Table (MQT) named ```total_sales_per_country``` for future reports.

### 04 Data Analytics

1. Created an instance of IBM Watson Studio and added a Cognos Dashboard Embedded (CDE) service to my project.
2. Uploaded the dataset from ```ecommerce.csv``` file and created a dashboard by performing tasks such as creating a bar chart of quarterly sales of mobile phones, a pie chart of category-wise sales of electronic goods, and a line chart of month-wise total sales for a given year.

### 05 ETL & Data Pipelines
SoftCart required its data to be synchronized among all the databases and data warehouses. The sync up of staging and production data warehouse was a routine task. For that, I had written a Python script to automate the process of regularly updating DB2 with new records from MySQL database.
#### Python Scripts and Automation

1. Extracted data from MySQL into a CSV file.
2. Transformed the OLTP data to suit the data warehouse schema and then saved the transformed data into a new CSV file.
3. Loaded the transformed data into the data warehouse.
4. Wrote a Python script that automatically loads yesterday's data from the operational database into the data warehouse.

#### ETL & Data Pipelines using Apache Airflow

1. Wrote an Airflow Directed Acyclic Graph (DAG) pipeline that analyzes the log files, extracts the required lines and fields, transforms the data and saved the output to a CSV file.
2. Loaded the data by archiving the transformed CSV file into a TAR file.
3. Made the DAG operational by submitting the DAG, unpausing it and then finally monitored that the DAG runs for Airflow console.

### 06 Big Data Analytics with Spark
For this assignment, I worked on IBM Watson Studio within a Jupyter notebook.

SoftCart had prepared a dataset containing search terms on their e-commerce platform. I used this data to run analytical queries using ```Pyspark``` and ```JupyterLab```.

1. Loaded the data from a CSV file into Spark dataframe.
2. Loaded a pre-trained sales forecasting model and used this to predict sales for next year.

## About this Project
The IBM Data Engineering Capstone Project is offered by IBM Skills Network hosted on Coursera. [Read more](https://www.coursera.org/learn/data-enginering-capstone-project)
