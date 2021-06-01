import psycopg2

select_Q = '''SELECT * FROM food'''
def connect():
  conn  = None
  try:
    conn = psycopg2.connect(
      host = "flash-flood.cgjkgasqph6e.us-east-1.rds.amazonaws.com",
      database = 'food',
      user= 'postgres',
      password= '12345678'
    )

    cur = conn.cursor()
    cur.execute(select_Q)
  except (Exception, psycopg2.DatabaseError) as err:
    print(err)
  finally:
    if conn is not None:
      conn.close()
      print('conn closed')


def main():
  connect()

if __public__ == __main__:
  main()

    '''I Choose to work with relational database because data is more structured
    and postgres is a best solution for relational database.'''