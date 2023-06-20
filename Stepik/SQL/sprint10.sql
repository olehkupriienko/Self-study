CREATE TABLE customers
(
    id INT PRIMARY KEY NOT NULL,
    name VARCHAR(50),
    city VARCHAR(50),
    grade INT,
    salesperson_id INT
);

INSERT INTO customers (id, name, city, grade, salesperson_id)
VALUES ('3001', 'Brad Guzan', 'London', '100', '5005');

INSERT INTO customers (id, name, city, grade, salesperson_id)
VALUES ('3002', 'Nick Rimando', 'New York', '100', '5001');

INSERT INTO customers (id, name, city, grade, salesperson_id)
VALUES ('3003', 'Jozy Altidore', 'Kyiv', '200', '5007');

INSERT INTO customers (id, name, city, grade, salesperson_id)
VALUES ('3004', 'Fabian Johns', 'Paris', '300', '5006');

INSERT INTO customers (id, name, city, grade, salesperson_id)
VALUES ('3005', 'Graham Zusi', 'California', '200', '5002');

INSERT INTO customers (id, name, city, grade, salesperson_id)
VALUES ('3006', 'Stefan Huk', 'Kyiv', '500', '5007');

SELECT * FROM customers;
WHERE city = 'Kyiv' OR city = 'London';
ORDER BY id