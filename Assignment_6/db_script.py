import mysql.connector
from pymongo import MongoClient
 
# MySQL configuration
mysql_config = {
    'user': 'root',
    'password': 'root',
    'host': 'localhost',
    'database': 'ecommerce_db'  # Ensure this database exists
}

# MongoDB configuration
mongo_config = {
    'host': 'localhost',  # Adjust the host if MongoDB is running elsewhere
    'port': 27017,         # Default port for MongoDB
    'database': 'ecommerce_mdb'  # Name of the MongoDB database
}

# Establish MySQL connection
mysql_conn = mysql.connector.connect(**mysql_config)
mysql_cursor = mysql_conn.cursor(dictionary=True)

# Establish MongoDB connection
mongo_client = MongoClient(mongo_config['host'], mongo_config['port'])
mongo_db = mongo_client[mongo_config['database']]

# Fetch categories and their associated products
mysql_cursor.execute("SELECT cat_id, cat_name FROM category")
categories = mysql_cursor.fetchall()

for category in categories:
    cat_id = category['cat_id']
    # Fetch associated products for the current category
    mysql_cursor.execute("SELECT prod_id, prod_name, c_id FROM product WHERE c_id = %s", (cat_id,))
    products = mysql_cursor.fetchall()
    # Embed products into the category document
    category['product'] = products

# Insert data into MongoDB category collection with embedded products
mongo_db.category.insert_many(categories)

# Close MySQL and MongoDB connections
mysql_cursor.close()
mysql_conn.close()
mongo_client.close()

print("Data transfer to MongoDB complete!")