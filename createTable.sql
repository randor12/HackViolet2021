create database hack_violet_2021;

use hack_violet_2021;

/**
 * Accounts Table
 */
CREATE TABLE accounts (
  id int PRIMARY KEY,
  email varchar(255),
  username varchar(255),
  passwd varchar(255),
  salt varchar(255),
  fname varchar(255),
  lname varchar(255)
);

/**
 * Database storing who follows certain "subscribed" accounts
 */
CREATE TABLE subscribe(
  sId int,
  fllwID int,
  fllwdID int
);

/**
 * Message that was posted by an account
 */
CREATE TABLE msgs(
  mID int,
  aID int,
  title varchar(255),
  message varchar(255),
  feed int,
  sentID int
);
