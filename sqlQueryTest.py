import sqlite3

# Task 1: Retrieve all columns from the "Customers" table, including their active subscription plan.
def task_1(cursor):
    query = """
    SELECT c."Org ID", c."Organization", c."Full Descr", c."Deleted", c."Business ID", c."Ext Cust ID",
           c."Addr Street1", c."Addr Street2", c."Addr Zipcode", c."Addr City", c."State/Province", c."Country",
           s."Contract ID" AS active_subscription_plan
    FROM "Customers" c
    LEFT JOIN "Subscriptions" s ON c."Org ID" = s."Org ID";
    """
    cursor.execute(query)
    result = cursor.fetchall()
    return result

# Task 2: Calculate the total usage-based charges incurred by each customer in July 2023.
def task_2(cursor):
    query = """
    SELECT c."Org ID", c."Organization", 
           SUM(CASE 
                 WHEN s."Contract ID" = 'Light' THEN CASE 
                                                        WHEN sc."Usage Count" > 20 THEN 0.5 * (sc."Usage Count" - 20) 
                                                        ELSE 0 
                                                        END
                 WHEN s."Contract ID" = 'Basic' THEN CASE 
                                                        WHEN sc."Usage Count" > 50 THEN 1.2 * (sc."Usage Count" - 50) 
                                                        ELSE 0 
                                                        END
                 ELSE 0 
                 END) AS total_charges
    FROM "Customers" c
    LEFT JOIN "Subscriptions" s ON c."Org ID" = s."Org ID"
    LEFT JOIN "ServiceCharges" sc ON c."Org ID" = sc."Org ID"
    WHERE sc."Usage Month" = 'July 2023'
    GROUP BY c."Org ID", c."Organization";
    """
    cursor.execute(query)
    result = cursor.fetchall()
    return result

# Task 3: Calculate the total usage amount for each service in June 2023.
def task_3(cursor):
    query = """
    SELECT p."Product ID", p."Product Code", SUM(sc."Usage Amount") AS total_usage_amount
    FROM "Products" p
    LEFT JOIN "ServiceCharges" sc ON p."Product ID" = sc."Product ID"
    WHERE sc."Usage Date" >= '2023-06-01' AND sc."Usage Date" < '2023-07-01'
    GROUP BY p."Product ID", p."Product Code";
    """
    cursor.execute(query)
    result = cursor.fetchall()
    return result

# Task 4: Update records to remove "X" from records with value X in column "UsageID".
def task_4(cursor):
    query = """
    UPDATE "ServiceUsage"
    SET "UsageID" = REPLACE("UsageID", 'X', '')
    WHERE "UsageID" LIKE '%X%';
    """
    cursor.execute(query)

# Connecting to the SQLite database
conn = sqlite3.connect('test.db')
cursor = conn.cursor()

# Execute the SQL queries
result_1 = task_1(cursor)
result_2 = task_2(cursor)
result_3 = task_3(cursor)
task_4(cursor)

# Close the database connection
conn.commit()
conn.close()


import sqlite3

# Task 1: Retrieve all columns from the "Customers" table, including their active subscription plan.
def task_1(cursor):
    query = """
    SELECT c.*, s.SubscriptionPlan AS active_subscription_plan
    FROM Customers c
    LEFT JOIN Subscriptions s ON c.subscription_id = s.SubscriptionID;
    """
    cursor.execute(query)
    result = cursor.fetchall()
    return result

# Task 2: Calculate the total usage-based charges incurred by each customer in July 2023.
def task_2(cursor):
    query = """
    SELECT c.CustomerID, c.Name, 
           SUM(CASE 
                 WHEN s.SubscriptionID = 'Light' THEN CASE 
                                                        WHEN ch.UsageCount > 20 THEN 0.5 * (ch.UsageCount - 20) 
                                                        ELSE 0 
                                                        END
                 WHEN s.SubscriptionID = 'Basic' THEN CASE 
                                                        WHEN ch.UsageCount > 50 THEN 1.2 * (ch.UsageCount - 50) 
                                                        ELSE 0 
                                                        END
                 ELSE 0 
                 END) AS total_charges
    FROM Customers c
    LEFT JOIN Subscriptions s ON c.subscription_id = s.SubscriptionID
    LEFT JOIN Charges ch ON c.CustomerID = ch.CustomerID
    WHERE ch.UsageMonth = 'July 2023'
    GROUP BY c.CustomerID, c.Name;
    """
    cursor.execute(query)
    result = cursor.fetchall()
    return result

# Task 3: Calculate the total usage amount for each service in June 2023.
def task_3(cursor):
    query = """
    SELECT s.ServiceID, SUM(su.UsageAmount) AS total_usage_amount
    FROM Services s
    LEFT JOIN ServiceUsage su ON s.ServiceID = su.ServiceID
    WHERE su.UsageDate >= '2023-06-01' AND su.UsageDate < '2023-07-01'
    GROUP BY s.ServiceID;
    """
    cursor.execute(query)
    result = cursor.fetchall()
    return result

# Task 4a: Update records to remove "X" from records with value X in column "UsageID".
def task_4a(cursor):
    query = """
    UPDATE ServiceUsage
    SET UsageID = REPLACE(UsageID, 'X', '')
    WHERE UsageID LIKE '%X%';
    """
    cursor.execute(query)

# Task 4b: Update records to remove "X" from records that start with "X" in column "UsageID".
def task_4b(cursor):
    query = """
    UPDATE ServiceUsage
    SET UsageID = REPLACE(UsageID, 'X', '')
    WHERE UsageID LIKE 'X%';
    """
    cursor.execute(query)

# Connecting to the SQLite database
conn = sqlite3.connect('test.db')
cursor = conn.cursor()

# Execute the SQL queries
result_1 = task_1(cursor)
result_2 = task_2(cursor)
result_3 = task_3(cursor)
task_4a(cursor)
task_4b(cursor)

# Close the database connection
conn.commit()
conn.close()