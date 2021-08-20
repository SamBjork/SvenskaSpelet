CREATE DATABASE IF NOT EXISTS users;
USE users;

CREATE TABLE IF NOT EXISTS `user` (
	`id` int(11) NOT NULL AUTO_INCREMENT,
  	`username` varchar(50) NOT NULL,
  	`password` varchar(255) NOT NULL,
    PRIMARY KEY (`id`)
);

INSERT INTO `user` (`id`, `name`, `password`, `email`) VALUES (1, 'Admin', 'goodOne');
INSERT INTO `user` (`id`, `name`, `password`, `email`) VALUES (2, 'John', 'badOne');

INSERT INTO users(
	username, password
) VALUES ("sam1021", "test");

CREATE TABLE users(
    id int NOT NULL AUTO_INCREMENT,
    username varchar(255) NOT NULL,
    password varchar(255) NOT NULL,
    PRIMARY KEY (id)
);

