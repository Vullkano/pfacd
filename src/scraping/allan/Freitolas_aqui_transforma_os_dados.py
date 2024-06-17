import csv


def kmh_to_ms(speed_kmh):
    return speed_kmh / 3.6


def processar_arquivo(origem, destino):
    with open(origem, 'r', newline='') as file:
        reader = csv.reader(file)
        next(reader)  

        dados_processados = []

        for linha in reader:
            
            try:
                temperatura = eval(linha[1]) if isinstance(eval(linha[1]), list) else [float(linha[1])]
            except (SyntaxError, TypeError, NameError):
                temperatura = [float(linha[1])]  

            try:
                humidade = eval(linha[2]) if isinstance(eval(linha[2]), list) else [float(linha[2])]
            except (SyntaxError, TypeError, NameError):
                humidade = [float(linha[2])]

            try:
                intensidade_vento_kmh = eval(linha[3]) if isinstance(eval(linha[3]), list) else [float(linha[3])]
            except (SyntaxError, TypeError, NameError):
                intensidade_vento_kmh = [float(linha[3])]

            try:
                precipitacao = eval(linha[4]) if isinstance(eval(linha[4]), list) else [float(linha[4])]
            except (SyntaxError, TypeError, NameError):
                precipitacao = [float(linha[4])]

            
            temperatura = temperatura[:8]
            humidade = humidade[:8]
            intensidade_vento_kmh = intensidade_vento_kmh[:8]
            precipitacao = precipitacao[:8]

            
            temp_max = max(temperatura)
            temp_min = min(temperatura)

            
            intensidade_vento_ms = [kmh_to_ms(speed) for speed in intensidade_vento_kmh]

           
            linha_processada = [
                linha[0],  
                str(temperatura),  
                str(humidade),  
                str(intensidade_vento_ms),  
                str(precipitacao),  
                str(temp_max),  
                str(temp_min)  
            ]

            dados_processados.append(linha_processada)


    with open(destino, 'w', newline='') as file:
        writer = csv.writer(file)

        writer.writerow(['Distrito', 'Temperatura', 'Humidade', 'Intensidade do Vento', 'Precipitação', 'Temp Max', 'Temp Min'])

        writer.writerows(dados_processados)


processar_arquivo('dados_climaticos_distritos_PT.csv', 'dados_processados1.csv')

print("Processamento concluído. Verifique o arquivo 'dados_processados.csv'.")
