-- lists all cities contained in the database

select
cities.id, cities.name, states.name
from cities, states
where cities.state_id = states.id
order by cities.id asc;

