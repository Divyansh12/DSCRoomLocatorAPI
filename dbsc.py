import psycopg2

conn = psycopg2.connect("host=localhost dbname=roomlocatordb user=postgres password=12.divyansh")

cur = conn.cursor()

# \COPY "roomlocator_room" TO 'C:\Users\Azomicrate\Documents\Desktop2\VsCode\Django\dsccoolroomlocator\room_export.csv' WITH (FORMAT csv, DELIMITER ',',  HEADER true);

with open('avail_export.csv', 'r') as f:
    # Notice that we don't need the `csv` module.
    next(f)  # Skip the header row.
    cur.copy_from(f,'"roomlocator_availability"' , sep=',',columns=('created_at','updated_at','archived','"isAvailable"','period_id','room_id'))
    
conn.commit()