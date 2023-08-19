-- calfonians cities
SELECT id, names FROM cities
WHERE state_id IN (SELECT id FROM states WHERE name = 'Calfornia')
ORDER BY id ASC;
