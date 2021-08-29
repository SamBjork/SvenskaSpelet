# SvenskaSpelet

A simple game about the Swedish language. 🇸🇪

#Database

ADD Database SvenskaSpelet;

USE SvenskaSpelet;

CREATE TABLE Users (
id INT(6) AUTO_INCREMENT PRIMARY KEY,
username VARCHAR(30) NOT NULL,
password VARCHAR(30) NOT NULL
)

CREATE TABLE Games (
id INT(6) AUTO_INCREMENT PRIMARY KEY,
score int(30) NOT NULL,
username VARCHAR(30) NOT NULL
)

CREATE TABLE Questions (
id INT(6) AUTO_INCREMENT PRIMARY KEY,
text VARCHAR(500) NOT NULL,
correctanswer VARCHAR(130) NOT NULL,
wronganswer1 VARCHAR(130) NOT NULL,
wronganswer2 VARCHAR(130) NOT NULL,
wronganswer3 VARCHAR(130) NOT NULL,
points int(30) NOT NULL
)
