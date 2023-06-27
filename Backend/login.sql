-- Create a table to store login information
CREATE TABLE users (
  id INT PRIMARY KEY AUTO_INCREMENT,
  username VARCHAR(255) NOT NULL,
  password VARCHAR(255) NOT NULL
);

-- Insert sample login information
INSERT INTO users (username, password)
VALUES ('john', 'password123'),
       ('jane', 'pass456'),
       ('alex', 'abc123');

-- Perform login verification
SELECT COUNT(*) AS count
FROM users
WHERE username = 'john' AND password = 'password123';
