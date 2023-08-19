-- calfonians cities
SELECT * FROM cities
WHERE state_id = (SELECT id FROM states WHERE name = 'Calfornia')
ORDER BY id ASC;
