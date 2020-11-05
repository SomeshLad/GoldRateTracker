create database stock;
use stock;

CREATE TABLE gold(Date DATE , price INT);
DESC gold;

INSERT INTO gold VALUES('2020-10-25', 49450),
    ('2020-10-26', 49500),
    ('2020-10-27', 49540),
    ('2020-10-28', 49550),
    ('2020-10-29', 49820),
    ('2020-10-30', 49540),
    ('2020-10-31', 49600),
    ('2020-11-1', 49550),
    ('2020-11-2', 49530),
    ('2020-11-3', 49500);

SELECT * FROM gold;
