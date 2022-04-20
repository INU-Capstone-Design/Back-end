DROP DATABASE IF EXISTS test;
CREATE DATABASE test;
USE test;

ALTER USER 'root'@'%' IDENTIFIED WITH mysql_native_password BY '1234';

SET GLOBAL time_zone='+09:00';
SET time_zone='+09:00';

CREATE TABLE Users (
    userid      INT NOT NULL AUTO_INCREMENT,
    username    VARCHAR(30) NOT NULL,
    password    VARCHAR(100) NOT NULL,
    name        VARCHAR(30),
    email       VARCHAR(40),
    create_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    update_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (userid)
);

CREATE TABLE Workspaces (
    workspaceid INT NOT NULL AUTO_INCREMENT,
    userid      INT,
    mindmap_info    LONGTEXT NOT NULL,
    create_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    update_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (workspaceId),
    FOREIGN KEY (userid) REFERENCES Users(userid)
);

CREATE TABLE Groupings (
    userid      INT,
    workspaceid INT,
    create_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    update_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (userid, workspaceid),
    FOREIGN KEY (userid)        REFERENCES Users(userid),
    FOREIGN KEY (workspaceid)   REFERENCES Workspaces(workspaceid)
);

INSERT INTO Users(username, password, name, email) VALUES('test01', '1234', 'jang', 'test01@gmail.com');
INSERT INTO Users(username, password, name, email) VALUES('test02', '1234', 'kang', 'test02@gmail.com');
INSERT INTO Users(username, password, name, email) VALUES('test03', '1234', 'gang', 'test03@gmail.com');
INSERT INTO Workspaces(userid, mindmap_info) VALUES(1, 'map html text 1');
INSERT INTO Workspaces(userid, mindmap_info) VALUES(1, 'map html text 2');
INSERT INTO Workspaces(userid, mindmap_info) VALUES(2, 'map html text 3');
INSERT INTO Groupings(userid, workspaceid) VALUES(1, 1);
INSERT INTO Groupings(userid, workspaceid) VALUES(1, 2);
INSERT INTO Groupings(userid, workspaceid) VALUES(2, 3);