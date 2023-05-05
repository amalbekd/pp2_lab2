import psycopg2
import re


hostname = 'localhost'
database = 'suppliers'
username = 'postgres'
pwd = 'Dinmuhamed29.'
port_id = 5432
conn, cur = None, None


conn = psycopg2.connect(
      host = hostname,
      dbname = database,
      user = username,
      password = pwd,
      port = port_id
)
cur = conn.cursor()


cur.execute(
   '''CREATE TABLE IF NOT EXISTS book(name VARCHAR, phone VARCHAR)'''
)

cur.execute(
    '''CREATE OR REPLACE FUNCTION search_from_bk(a VARCHAR, b VARCHAR)
      RETURNS SETOF book 
   AS
   $$
      SELECT * FROM book WHERE name = a AND phone = b;
   $$
   language sql;
   '''
)

cur.execute(
   '''CREATE OR REPLACE PROCEDURE insert_list_of_users(
  IN users TEXT[][]
)

LANGUAGE plpgsql

AS $$

DECLARE
  i TEXT[];

BEGIN 

   Foreach i slice 1 in array users
   LOOP
      INSERT INTO book (name, phone) VALUES (i[1], i[2]);
   END LOOP;
 

END
$$;
'''
)

cur.execute(
   '''CREATE OR REPLACE PROCEDURE insert_to_book(nm VARCHAR, phon VARCHAR)
      LANGUAGE plpgsql
      AS $$
      DECLARE 
         cnt INTEGER;
      BEGIN
         SELECT INTO cnt (SELECT count(*) FROM book WHERE name = nm);
         IF cnt > 0 THEN
            UPDATE book
               SET phone = phon
               WHERE name = nm;
         ELSE
            INSERT INTO book(name, phone) VALUES (nm, phon);
            END IF;
      END;
      $$;''')




cur.execute("""CREATE OR REPLACE PROCEDURE delete_from_book(nm VARCHAR)
LANGUAGE plpgsql
AS $$
DECLARE cnt INTEGER;
BEGIN
    SELECT into cnt (SELECT count(*) FROM book WHERE name = nm);
 IF cnt IS NOT NULL THEN
        DELETE FROM book
  WHERE name=nm;
    END IF;
END;
$$;""")

cur.execute("""CREATE OR REPLACE FUNCTION paginating(a integer, b integer)
RETURNS SETOF book
AS $$
   SELECT * FROM book
 ORDER BY name
 LIMIT a OFFSET b;
$$
language sql;""")


a = input('search\ninsert\ninsertloop\ndelete\npaginating\n')
if a == 'search':
   cur.execute("SELECT search_from_bk('Neymar JR', '87076052769')")
   result = cur.fetchall()
   print(result)
if a == 'insert':
   cur.execute("CALL insert_to_book('Nurtaza Nurasyl','87774545505')")
if a == 'insertloop':
  cur.execute('''CALL insert_list_of_users(ARRAY[
    ARRAY['Dimash', '87780950826'],
    ARRAY['Akhamdi', '87025510432'],
    ARRAY['Rassul', '87086276149']
]);''')  
if a == 'delete':
   cur.execute("CALL delete_from_book('Rassul')")
if a == 'paginating':
   cur.execute(
      '''SELECT * FROM paginating(6, 2);'''
   )
   print(cur.fetchall())
conn.commit()
cur.close()
conn.close()