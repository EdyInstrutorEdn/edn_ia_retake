import json

def lambda_handler(event, context):
    try: 

        print(f"Evento: ",event)
        print('Calculando gorgeta')

        request_body = json.loads(event['body'])
        if request_body is None:
            raise Exception("Corpo da requisição inválido")

        total = request_body.get('valor_total')
        percent = request_body.get('percentual')

        if not total or not percent:
            erro = ""
            if not total:
                erro = "paramentro total"
            if not percent:
                erro = erro + " paramento percentual"
            raise Exception(f"{erro} inválido(s)")

        try:
            total = float(total)
        except:
            raise Exception("valor total inválido")

        try:
            percent = float(percent)
        except:
            raise Exception("percentutal total inválido")

        tip = total * (percent/100)
        
        print(f'Total: {total}')
        print(f'Percentual: {percent}')
        print(f'Gorjeta: {tip}')

        # TODO implement
        return {
            'statusCode': 200,
            'body': json.dumps(f"O Valor da gorjeta para uma conta de R${total}, com {percent}% é de R${tip:.2f}")
        }
    except Exception as ex:
        return {
            'statusCode': 500,
            'body': json.dumps(str(ex))
        }
