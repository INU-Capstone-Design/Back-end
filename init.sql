DROP DATABASE IF EXISTS testdb;
CREATE DATABASE testdb;
USE testdb;

CREATE TABLE Users (
    userid      INT NOT NULL AUTO_INCREMENT,
    username    VARCHAR(20) NOT NULL,
    password    VARCHAR(30) NOT NULL,
    name        VARCHAR(20),
    email       VARCHAR(40),
    create_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (userId)
);

CREATE TABLE Workspaces (
    workspaceid INT NOT NULL AUTO_INCREMENT,
    userid      INT,
    map_HTML    LONGTEXT NOT NULL,
    create_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (workspaceId),
    FOREIGN KEY (userId) REFERENCES Users(userId)
);

CREATE TABLE Groupings (
    userid      INT,
    workspaceid INT,
    PRIMARY KEY (userId, workspaceId),
    FOREIGN KEY (userId)        REFERENCES Users(userId),
    FOREIGN KEY (workspaceId)   REFERENCES Workspaces(workspaceId)
);

INSERT INTO Users(username, password, name, email) VALUES('test01', '1234', 'jang', 'test@gmail.com');
INSERT INTO Workspaces(userid, map_HTML) VALUES(1, 'Hello World');
INSERT INTO Groupings(userid, workspaceid) VALUES(1, 1)
