def query_by_upc_and_store_number(cur, upc, store_number):
    query = f"""SELECT *
	FROM public.food
	WHERE upc = '{upc}' AND store_number = '{store_number}';"""

    cur.execute(query)

    row = cur.fetchone()

    results = []
    while row is not None:
        results.append(row)
        row = cur.fetchone()

    print(results)
    # return results

    '''data display by upc and store number where in postgres leading 
    zeros are ignore automatically.'''