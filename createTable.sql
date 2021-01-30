create database hack_violet_2021;

use hack_violet_2021;

CREATE TABLE accounts (
  id int PRIMARY KEY,
  email varchar(255),
  username varchar(255),
  passwd varchar(255),
  salt varchar(255),
  fname varchar(255),
  lname varchar(255)
);
