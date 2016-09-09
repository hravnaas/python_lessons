USE friendsdb;
INSERT INTO friends (first_name, last_name, occupation, created_at, updated_at)
SELECT "Hans", "Ravnaas", "Student", NOW(), NOW() UNION ALL
SELECT "Doyle", "Ravnaas", "Dev", NOW(), NOW() UNION ALL
SELECT "Malcom", "Ravnaas", "Cat", NOW(), NOW() UNION ALL
SELECT "Angus", "Ravnaas", "ex-cat", NOW(), NOW();

SELECT * FROM friends
-- DELETE FROM friends

