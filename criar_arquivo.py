# gerar_vendas_csv.py
import csv
import random
from datetime import datetime, timedelta

def generate_sales_data(num_rows=100000, output_filename="vendas.csv"):

    headers = ["id_venda", "data", "produto", "quantidade", "preco_unitario", "total_venda", "regiao", "cliente_id"]
    products = ["TV", "Celular", "Fone", "Geladeira", "Notebook", "Tablet", "Smartwatch", "Monitor"]
    regions = ["Sudeste", "Nordeste", "Sul", "Centro-Oeste", "Norte"]
    
    start_date = datetime(2023, 1, 1)

    print(f"Gerando {num_rows} linhas de dados de vendas para '{output_filename}'...")

    with open(output_filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(headers) 

        for i in range(1, num_rows + 1):
            sale_date = start_date + timedelta(days=random.randint(0, 364)) 
            product = random.choice(products)
            quantity = random.randint(1, 5)
            price_unit = round(random.uniform(50.0, 5000.0), 2)
            total_sale = round(quantity * price_unit, 2)
            region = random.choice(regions)
            client_id = f"C{random.randint(1000, 9999)}"

            row = [
                i,
                sale_date.strftime("%Y-%m-%d"),
                product,
                quantity,
                price_unit,
                total_sale,
                region,
                client_id
            ]
            writer.writerow(row)
            
            if i % (num_rows // 10) == 0: # Imprime progresso a cada 10%
                print(f"{i / num_rows:.0%} concluído...")

    print(f"Arquivo '{output_filename}' gerado com sucesso!")

if __name__ == "__main__":
    generate_sales_data(10000000, "vendas.csv")
