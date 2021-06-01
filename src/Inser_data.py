def insert_records(curr):
    _file = "C:/Users/sonip/PycharmProjects/pythonProject4/merged.json"
    with open(_file) as f:
        cleaned_rows = cleanup_data(json.load(f))

        values_arr = []
        for row in cleaned_rows:
            values_arr.append(f'''(
                $cc${row['name']}$cc$, '{row['category']}', '{row['store_number']}',
                '{row['taxable']}', '{row['price']}', $cc${row['description']}$cc$, 
$cc${row['department']}$cc$, '{row['image']}', '{row['upc']}')'''
                )

        insert_Q = f'''INSERT INTO public.food (name, category, store_number, 
                        taxable, price, description, department, image, upc)
                        VALUES {', '.join(values_arr)}
                        ON CONFLICT DO NOTHING;'''

        curr.execute(insert_Q);
            