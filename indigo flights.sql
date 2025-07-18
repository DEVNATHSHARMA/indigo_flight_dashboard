select *
from flights_cleaned

select source,count(*)
from(select source
from flights_cleaned
union all
select destination
from flights_cleaned) t
group by t.source
order by count(*) desc

select date_of_journey,count(*)
from flights_cleaned
group by date_of_journey
order by date_of_journey


SELECT
    Airline,
    AVG(Duration::INT) AS avg_duration_minutes
FROM
    flights_cleaned
GROUP BY
    Airline
ORDER BY
    avg_duration_minutes ASC;



select airline,avg(duration)
from flights_cleaned
group by airline
order by avg(duration) asc


SELECT
Airline,
ROUND(AVG(Duration::INT)) AS avg_duration_minutes
FROM
flights_cleaned
GROUP BY
Airline
ORDER BY
avg_duration_minutes ASC;



SELECT 
Airline, 
ROUND(AVG(price)) AS avg_price
FROM flights_cleaned
GROUP BY Airline
ORDER BY avg_price ASC;
