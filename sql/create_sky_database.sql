DROP DATABASE IF EXISTS sky;
CREATE DATABASE sky;
USE sky;

SET NAMES utf8mb4;
SET character_set_client = utf8mb4;

CREATE TABLE review (
    review_id VARCHAR(128) PRIMARY KEY,
    user_name VARCHAR(64),
    content BLOB,
    rating TINYINT,
    thumbs_up_count MEDIUMINT UNSIGNED,
    created_for_version VARCHAR(64),
    created_on DATETIME
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;
