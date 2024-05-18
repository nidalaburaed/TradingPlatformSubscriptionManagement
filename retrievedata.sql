-- Task 1: Retrieve all columns from the "Customers" table, including their active subscription plan.
SELECT c.*, s.plan_name AS active_subscription_plan
FROM Customers c
LEFT JOIN Subscriptions s ON c.subscription_id = s.subscription_id;

-- Task 2: Calculate the total usage-based charges incurred by each customer in July 2023.
SELECT c.customer_id, c.name, SUM(CASE 
                                    WHEN s.subscription_id = 'Light' THEN CASE 
                                                                        WHEN sc.usage_count > 20 THEN 0.5 * (sc.usage_count - 20) 
                                                                        ELSE 0 
                                                                        END
                                    WHEN s.subscription_id = 'Basic' THEN CASE 
                                                                        WHEN sc.usage_count > 50 THEN 1.2 * (sc.usage_count - 50) 
                                                                        ELSE 0 
                                                                        END
                                    ELSE 0 
                                    END) AS total_charges
FROM Customers c
LEFT JOIN Subscriptions s ON c.subscription_id = s.subscription_id
LEFT JOIN ServiceCharges sc ON c.customer_id = sc.customer_id
WHERE sc.usage_month = 'July 2023'
GROUP BY c.customer_id, c.name;

-- Task 3: Calculate the total usage amount for each service in June 2023.
SELECT s.service_id, SUM(su.usage_amount) AS total_usage_amount
FROM Services s
LEFT JOIN ServiceUsage su ON s.service_id = su.service_id
WHERE su.usage_date >= '2023-06-01' AND su.usage_date < '2023-07-01'
GROUP BY s.service_id;

-- Task 4a: Update records to remove "X" from records with value X in column "UsageID".
UPDATE ServiceUsage
SET UsageID = REPLACE(UsageID, 'X', '')
WHERE UsageID LIKE '%X%';

-- Task 4b: Update records to remove "X" from records that start with "X" in column "UsageID".
UPDATE ServiceUsage
SET UsageID = REPLACE(UsageID, 'X', '')
WHERE UsageID LIKE 'X%';