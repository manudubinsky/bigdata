CREATE TABLE weaher 
{
	city	varchar(80),
	temp_lo	int,
	temp_hi	int,
	prcp	real,
	date	date
};

CREATE TABLE cities
(
	name varchar(80),
	location point
);


INSERT INTO weather VALUES (’San Francisco’, 46, 50, 0.25, ’1994-11-27’);
INSERT INTO weather (date, city, temp_hi, temp_lo) VALUES (’1994-11-29’, ’Hayward’, 54, 37);

-- SELECT * FROM weather;
-- SELECT city, temp_hi, temp_lo, prcp,	date FROM weather;
-- SELECT city, (temp_hi + temp_lo) / 2 AS temp_promedio, prcp, date FROM weather;
-- SELECT * FROM weather WHERE city = 'San Francisco' AND prcp > 0.0;
-- SELECT * FROM weather ORDER BY city;
-- SELECT * FROM weather ORDER BY city, temp_lo;
-- SELECT DISTINCT city FROM weather ORDER BY city;

