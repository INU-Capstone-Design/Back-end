DROP DATABASE IF EXISTS test;
CREATE DATABASE test;
USE test;

CREATE TABLE Users (
    userid      VARCHAR(20) NOT NULL PRIMARY KEY,
    password    VARCHAR(30) NOT NULL,
    name        VARCHAR(20),
    email       VARCHAR(40),
    create_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE Working_groups (
    g_pk        INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    userid      VARCHAR(20) NOT NULL,
    is_master   TINYINT,
    create_time TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (userid) REFERENCES Users(userid)
);

CREATE TABLE Workspaces (
    w_pk        INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    g_pk        INT,
    map_HTML    LONGTEXT NOT NULL,
    create_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (g_pk) REFERENCES Working_groups(g_pk)
);

INSERT INTO Users(userid, password, name, email) VALUES('test01', '1234', 'jang', 'test@gmail.com');
INSERT INTO Working_groups(userid, is_master) VALUES('test01', 1);
INSERT INTO Workspaces(g_pk, map_HTML) VALUES(1, "Hello World");