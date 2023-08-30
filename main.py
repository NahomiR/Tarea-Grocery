
import csv

def write_list_of_dicts_to_csv(filename, data):
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        fieldnames = data[0].keys()
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

def read_csv_to_dict(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        return list(reader)

def main():
    # Cargar los datos existentes en la fuente de datos (sample_grocery.csv)
    source_data = read_csv_to_dict('sample_grocery.csv')

    # Cargar los datos del archivo de lote (grocery_batch_1.csv)
    batch_data = read_csv_to_dict('grocery_batch_1.csv')

    # Crear un diccionario para mantener el seguimiento de los artículos y sus cantidades
    grocery_dict = {}

    # Agregar los datos existentes a grocery_dict
    for item in source_data:
        SKU = item['SKU']
        Name = item['Name']
        Description = item['Description']
        Price = item['Price']
        Quantity = int(item['Quantity'])
        Expiration_Date = item['Expiration Date']
        
        if Name in grocery_dict:
            grocery_dict[Name]['Quantity'] += Quantity
        else:
            grocery_dict[Name] = {
                'SKU': SKU,
                'Name': Name,
                'Description': Description,
                'Price': Price,
                'Quantity': Quantity,
                'Expiration Date': Expiration_Date
            }

    # Combinar los datos del archivo de lote
    for item in batch_data:
        SKU = item['SKU']
        Name = item['Name']
        Description = item['Description']
        Price = item['Price']
        Quantity = int(item['Quantity'])
        Expiration_Date = item['Expiration Date']
        
        if Name in grocery_dict:
            grocery_dict[Name]['Quantity'] += Quantity
        else:
            grocery_dict[Name] = {
                'SKU': SKU,
                'Name': Name,
                'Description': Description,
                'Price': Price,
                'Quantity': Quantity,
                'Expiration Date': Expiration_Date
            }

    # Convertir el diccionario a una lista de diccionarios para escribir en el archivo
    final_data = list(grocery_dict.values())

    # Guardar los datos finales en grocery_db.csv
    write_list_of_dicts_to_csv('grocery_db.csv', final_data)

if __name__ == '__main__':
    main()




  
    




