CREATE TABLE employee_t (
    id INT PRIMARY KEY,
    department VARCHAR(50),
    role VARCHAR(50),
    contact_id INT
);

INSERT INTO employee_t
(id, department, role, contact_id)
VALUES
(1, 'Sales', 'Manager', 100),
(2, 'Sales', 'Executive', 101),
(3, 'Sales', 'Executive', 101),
(4, 'HR', 'Manager', 102),
(5, 'HR', 'Executive', 103),
(6, 'HR', 'Executive', 104),
(7, 'HR', 'Executive', 104);