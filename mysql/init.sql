DROP DATABASE IF EXISTS minders;
CREATE DATABASE minders;
USE minders;

ALTER USER 'root'@'%' IDENTIFIED WITH mysql_native_password BY '1234';

SET GLOBAL time_zone='+09:00';
SET time_zone='+09:00';

CREATE TABLE Users (
    username        VARCHAR(30),
    password        VARCHAR(100) NOT NULL,
    name            VARCHAR(30),
    email           VARCHAR(40),
    create_time     TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    update_time     TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY     (username)
);

CREATE TABLE Workspaces (
    workspaceid     INT NOT NULL AUTO_INCREMENT,
    master          VARCHAR(30) NOT NULL,
    title           VARCHAR(50) NOT NULL,
    mindmap         LONGTEXT NOT NULL,
    create_time     TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    update_time     TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY     (workspaceid),
    FOREIGN KEY     (master) REFERENCES Users(username) ON DELETE CASCADE
);

CREATE TABLE Groupings (
    username        VARCHAR(30),
    workspaceid     INT,
    create_time     TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    update_time     TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY     (username, workspaceid),
    FOREIGN KEY     (username)      REFERENCES Users(username) ON DELETE CASCADE,
    FOREIGN KEY     (workspaceid)   REFERENCES Workspaces(workspaceid) ON DELETE CASCADE
);