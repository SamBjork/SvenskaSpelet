# SvenskaSpelet

A simple game about the Swedish language. 🇸🇪

#Database

ADD Database SvenskaSpelet;

USE SvenskaSpelet;

CREATE TABLE Users (
userid INT(6) AUTO_INCREMENT PRIMARY KEY,
username VARCHAR(30) NOT NULL,
password VARCHAR(30) NOT NULL
)

CREATE TABLE Games (
gameid INT(6) AUTO_INCREMENT PRIMARY KEY,
score VARCHAR(30) NOT NULL,
userid VARCHAR(30) NOT NULL
)

CREATE TABLE Question (
id INT(6) AUTO_INCREMENT PRIMARY KEY,
text VARCHAR(30) NOT NULL,
correct VARCHAR(30) NOT NULL,
firstwrong VARCHAR(30) NOT NULL,
secondwrong VARCHAR(30) NOT NULL,
thirdwrong VARCHAR(30) NOT NULL,
points VARCHAR(30) NOT NULL
)
