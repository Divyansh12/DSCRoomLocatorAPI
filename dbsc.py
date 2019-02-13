import psycopg2

#conn = psycopg2.connect("host=ec2-23-21-165-188.compute-1.amazonaws.com dbname=de7vfg255ci4al user=vhwrsjmhplmjab password=db579f9f595f62e12355fe9512089fc4a94af6b0a919d46cabccac39910e71ef")

conn = psycopg2.connect("host=localhost dbname=roomlocatordb user=postgres password=12.divyansh")

cur = conn.cursor()

with open('days_export.csv', 'r') as f:
    # Notice that we don't need the `csv` module.
    next(f)  # Skip the header row.
    cur.copy_from(f,'"roomlocator_day"' , sep=',')

with open('period_export.csv', 'r') as f:
    # Notice that we don't need the `csv` module.
    next(f)  # Skip the header row.
    cur.copy_from(f,'"roomlocator_period"' , sep=',')

with open('block_export.csv', 'r') as f:
    # Notice that we don't need the `csv` module.
    next(f)  # Skip the header row.
    cur.copy_from(f,'"roomlocator_block"' , sep=',')

with open('roomnumber_export.csv', 'r') as f:
    # Notice that we don't need the `csv` module.
    next(f)  # Skip the header row.
    cur.copy_from(f,'"roomlocator_roomnumber"' , sep=',')
with open('room_export.csv', 'r') as f:
    # Notice that we don't need the `csv` module.
    next(f)  # Skip the header row.
    cur.copy_from(f,'"roomlocator_room"' , sep=',')

# \COPY "roomlocator_room" TO 'C:\Users\Azomicrate\Documents\Desktop2\VsCode\Django\dsccoolroomlocator\room_export.csv' WITH (FORMAT csv, DELIMITER ',',  HEADER true);

with open('availability_export.csv', 'r') as f:
    # Notice that we don't need the `csv` module.
    next(f)  # Skip the header row.
    cur.copy_from(f,'"roomlocator_availability"' , sep=',')
    

# with open('avial_export.csv', 'r') as f:
#     # Notice that we don't need the `csv` module.
#     next(f)  # Skip the header row.
#     cur.copy_from(f,'"roomlocator_availability"' , sep=',')
    
conn.commit()