CREATE DATABASE Days4Innovation;
USE Days4Innovation;
CREATE TABLE participant(
    id INT NOT NULL AUTO_INCREMENT,
    nom VARCHAR(255),
    mail VARCHAR(255) NOT NULL,
    remarque VARCHAR(1000),
    evenements VARCHAR(1000),
    PRIMARY KEY (id)
);
