DROP DATABASE IF EXISTS sky;
CREATE DATABASE sky;
USE sky;

SET NAMES utf8mb4;
SET character_set_client = utf8mb4;

CREATE TABLE reviews(
	user_id VARCHAR(128) NOT NULL,
    review TEXT,
    rating TINYINT UNSIGNED,
    version VARCHAR(32),
    datetime_created DATETIME
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
