## SQL Practice

# Give Top 3 authors with most total number of books sold
SELECT a.author_name, SUM(b.sold_copies) AS total_sold
FROM authors AS a
JOIN books AS b ON a.book_name = b.book_name
GROUP BY a.author_name
ORDER BY total_sold DESC
LIMIT 3;



# Count the number of users inserted more than 1000 and less than 2000 images
SELECT COUNT(*) AS num_users # Return the count of users 
FROM (
    SELECT user_id, SUM(num_images) AS total_images
    FROM (
        SELECT user_id, COUNT(*) AS num_images
        FROM event_log
        GROUP BY user_id
    ) AS user_images
    WHERE total_images > 1000 AND total_images < 2000
) AS filtered_users;



# Give all departments with averaged salary lower than 500
SELECT e.department, AVG(s.salary) AS avg_salary
FROM employees AS e
JOIN salaries AS s ON e.id = s.id
GROUP BY e.department
HAVING avg_salary < 500;



# Analyse Social-media links data
# List all following links that were created before September 1st, 1993
SELECT *
FROM follows
WHERE date_created<"1993-09-01";


# List all following links established before September 1st 1993, using users first names
SELECT u.first_name as follower,
u2.first_name as followee,
date_created 
FROM follows
JOIN users as u ON follows.user_id=u.user_id
JOIN users as u2 ON follows.follows=u2.user_id
WHERE date_created<"1993-09-01";


# Count the number of followers for each user before 12-31-1999
SELECT CONCAT(u.first_name, ' ', u.last_name) AS full_name, COUNT(*) AS num_followers
FROM users u
INNER JOIN follows f ON u.user_id = f.user_id # INNER JOIN only takes the matches
WHERE f.date_created < '1999-12-31'
GROUP BY u.user_id
ORDER BY number_of_followers DESC;


# Count the number of users each user follows
SELECT u.user_id, CONCAT(u.first_name, ' ', u.last_name) AS full_name, COUNT(f.follows) AS num_following
FROM users u
LEFT JOIN follows f ON u.user_id = f.user_id # LEFT JOIN ensures all users are included even if they do not follow any other users
GROUP BY u.user_id


# List all rows from follows where someone from one house follows someone from a different house
# Give the result with user names and houses
SELECT u1.first_name AS follower_first_name, u2.first_name AS followee_name,
       u1.house AS follower_house, u2.house AS followee_house
FROM follows f
JOIN users u1 ON f.user_id = u1.user_id
JOIN users u2 ON f.follows = u2.user_id
WHERE u1.house <> u2.house


# List all unrequited followings (i.e. where A follows B but B does not follow A)
SELECT u1.first_name AS follower_first_name, u1.last_name AS follower_last_name,
       u2.first_name AS following_first_name, u2.last_name AS following_last_name
FROM follows f1
JOIN follows f2 ON f1.follows = f2.user_id AND f1.user_id = f2.follows
JOIN users u1 ON f1.user_id = u1.user_id
JOIN users u2 ON f1.follows = u2.user_id
WHERE NOT EXISTS (
  SELECT 1 FROM follows f3 WHERE f3.user_id = f1.follows AND f3.follows = f1.user_id
) # if cannot select a row from the bidirectional links 

# WHERE Concat(follows.follows," ",follows.user_id) NOT IN
      # (SELECT Concat(follows.user_id," ",follows.follows) AS relationship FROM follows);
