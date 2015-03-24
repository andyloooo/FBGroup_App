-- create out database to store facebook data
CREATE DATABASE facebook_data;

-- create our table to store the data
USE facebook_data;
CREATE TABLE page_info(-- each is a column of table
	id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    fb_id BIGINT UNSIGNED,
    likes BIGINT UNSIGNED,
    talking_about BIGINT UNSIGNED,
    usename VARCHAR(40),
    time_collected datetime NOT NULL DEFAULT NOW()
);