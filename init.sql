DROP DATABASE IF EXISTS mind_db;
CREATE DATABASE mind_db;
USE mind_db;

CREATE TABLE Users(
    userid      VARCHAR(20) NOT NULL PRIMARY KEY,
    password    VARCHAR(30) NOT NULL,
    name        VARCHAR(20),
    email       VARCHAR(40),
    create_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE Groups(
    g_pk        INTEGER AUTO_INCREMENT PRIMARY KEY,
    userid      VARCHAR(20),
    is_master   TINYINT(1),
    create_time TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (userid) REFERENCES Users(userid)
);

CREATE TABLE Workspaces(
    w_pk        INTEGER AUTO_INCREMENT PRIMARY KEY,
    g_pk        INTEGER,
    map_HTML    LONGTEXT,
    create_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (g_pk) REFERENCES Groups(g_pk)
);

INSERT INTO Users(userid, password, name, email) VALUES('test01', '1234', 'jang', 'test@gmail.com');