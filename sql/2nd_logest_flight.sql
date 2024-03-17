-- Given a table of flights, extract the 2nd flight with the most duration between each pair of cities. Order the flights by the flight id ascending.

-- Note: For any cities X and Y, (source_location=X, destination_location=Y) and (source_location=Y, destination_location=X) are counted as the same pair of cities.

-- Note: If there are fewer than two flights between two cities, there is no 2nd longest flight.
  
with id as (  
select id from
( 
select 
*,
rank() over (partition by least(source_location,destination_location),greatest(source_location,destination_location) order by TIMESTAMPDIFF(SECOND,flight_start,flight_end) desc) as rnk
from flights) c
where rnk=2)

select 
destination_location,	flight_end,	flight_start,	id,	source_location
from flights where id in( select * from id) order by id;
