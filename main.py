import requests
import csv
import json
 
headers = {
    'api-key': 'UgjUpN-xUTRXe_47Edmg94MqDb-3a2AJqo1iZPtJu8A',
    'Content-Type': 'application/json',
}
 
# reading the cvs file
with open('products/items.csv', newline='', encoding="utf-8") as f:
  csv_reader = csv.reader(f)
  csv_headings = next(csv_reader)
  first_line = next(csv_reader)
  
  # takes the data from the first line of the file 
  valuesInternaCode = first_line[0].split(";")
  valuesBarCode = first_line[2].split(";")
  valuesName= first_line[1].split(";")
  valuesPrice = first_line[3].split(";")
  
  data =  {
        'products':[{
        'internal_code': valuesInternaCode[0],
        'barcodes': [valuesBarCode[0]],
        'name': valuesName[0],
        'price': valuesPrice[0]
        
       }]}
  f.close()

# generates a json file and prints the return
newFile = open("newfile.json", "w")
newFile.write(json.dumps(data))
newFile.close()
fileConsults = open('newfile.json',encoding="utf-8") 
info = json.load(fileConsults) 
fileConsults.close()
print(info) 
print(" ")
print("'----------------------Products after Update----------------------'")
print(" ")
 
# looping and changing the product name
for products in info.get("products"):
    if products.get('name') == "5L Com Gás":
          if products.get('price') == "99":
              if products.get('barcodes') == ["7196294563771"]:
                products['name'] = "ACQUISSIMA Passion Natural 1,5L Com Gás" # update product name
                products['price'] = "2,99" # updates product price
                products['barcodes'] = ["7196294563771"] # update product barcode
            
    with open ("update.json", "w") as f:
        f.write(json.dumps(info))
        f.close()
 # creates a new file with the change made and prints the return with the update ready
openfile = open('update.json',encoding="utf-8")
info = json.load(openfile) 
openfile.close()
print(info) 
 
response = requests.put('https://api.instabuy.com.br/store/products/', headers=headers, data=json.dumps(info))
# if you update the data, it returns the status of the request
try:
    if response.status_code >= 200 and response.status_code <= 299:
        print(response.content)    
    else:
        print(response.json)
        print(response.content)
        print('Error')
except ValueError:
            print("Resposta Inválida")
 
