DROP DATABASE IF EXISTS test;
CREATE DATABASE test;
USE test;

CREATE TABLE Users (
    username    VARCHAR(20) NOT NULL,
    password    VARCHAR(30) NOT NULL,
    name        VARCHAR(20),
    email       VARCHAR(40),
    create_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (username)
);

CREATE TABLE Workspaces (
    workspaceId INT NOT NULL AUTO_INCREMENT,
    username    VARCHAR(20) NOT NULL,
    map_HTML    LONGTEXT NOT NULL,
    create_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (workspaceId),
    FOREIGN KEY (username) REFERENCES Users(username)
);

CREATE TABLE Groupings (
    username    VARCHAR(20),
    workspaceId INT,
    PRIMARY KEY (username, workspaceId),
    FOREIGN KEY (username)      REFERENCES Users(username),
    FOREIGN KEY (workspaceId)   REFERENCES Workspaces(workspaceId)
);

INSERT INTO Users(username, password, name, email) VALUES('test01', '1234', 'jang', 'test@gmail.com');
INSERT INTO Workspaces(username, map_HTML) VALUES('test01', 'Hello World');
INSERT INTO Groupings(username, workspaceId) VALUES('test01', 1)
