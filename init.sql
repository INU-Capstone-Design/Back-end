DROP DATABASE IF EXISTS mind_db;
CREATE DATABASE mind_db;
USE mind_db;

CREATE TABLE Users(
    u_pk        INTEGER PRIMARY KEY,
    userid      VARCHAR(20),
    password    VARCHAR(30),
    name        VARCHAR(20),
    email       VARCHAR(40),
    create_time DATETIME
);

CREATE TABLE Groups(
    g_pk     INTEGER PRIMARY KEY,
    u_pk        INTEGER,
    is_master   TINYINT(1),
    create_time DATETIME,
    FOREIGN KEY (u_pk) REFERENCES Users(u_pk)
);

CREATE TABLE Workspaces(
    w_pk        INTEGER PRIMARY KEY,
    g_pk        INTEGER,
    map_HTML    LONGTEXT,
    create_time DATETIME,
    FOREIGN KEY (g_pk) REFERENCES Groups(g_pk)
);