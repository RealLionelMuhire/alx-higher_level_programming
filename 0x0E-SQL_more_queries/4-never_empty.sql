-- Id_null table has to be created and no empty id, just 1

CREATE TABLE IF NOT EXISTS id_not_null(
id INT DEFAULT 1,
name VARCHAR(256)
);
