import psycopg2


def cleanup_data(rows):
    clean_records = []
    for row in rows:
        is_valid = True
#         print(row.keys())
        for key in row.keys():
            if key == 'upc':
#                 print(key, type(key))
                break
                if type(key) != str:
                    is_valid = False
                    break
            elif type(key) == 'price':
                if type(key) != float:
                    is_valid = False
                    break
            elif type(key) == 'store_number':
                if type(key) != str:
                    is_valid = False
                    break
                    
        if is_valid:
            clean_row = {
                'upc': row['upc'],
                'name': row['name'],
                'category': row['category'],
                'store_number': row['store_number'],
                'price': row['price'],
                'description': row['description'],
                'taxable': row['taxable'],
                'department': row['department'],
                'image': row['image']
            }
            clean_records.append(clean_row)
            
    return clean_records
    
_file = "C:/Users/sonip/PycharmProjects/pythonProject4/merged.json"
with open(_file) as f:
    cleaned_rows = cleanup_data(json.load(f))
    print(cleaned_rows[:5])
    write_to_csv(cleaned_rows)


    '''clean up data with duplicate and invalid records.'''