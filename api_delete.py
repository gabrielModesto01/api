import pymongo
from pymongo.errors import ConnectionFailure, ConfigurationError

# Configuração da conexão com o MongoDB
mongo_uri = "mongodb+srv://login:password@cluster0.ozsm1jh.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0&connectTimeoutMS=30000&serverSelectionTimeoutMS=30000"
database_name = "vulnerability_db"
collection_name = "scan_results"

try:
    # Conectar ao MongoDB
    client = pymongo.MongoClient(mongo_uri)
    db = client[database_name]
    collection = db[collection_name]

    # Testar a conexão
    client.admin.command('ping')
    print("Conexão com o MongoDB estabelecida com sucesso.")

    # Confirmar a exclusão de todos os dados
    print(f"ATENÇÃO: Esta operação excluirá TODOS os documentos da coleção '{collection_name}' no banco '{database_name}'.")
    confirmation = input("Digite 'CONFIRMAR' para prosseguir com a exclusão: ")

    if confirmation == "CONFIRMAR":
        # Excluir todos os documentos da coleção
        result = collection.delete_many({})
        print(f"Exclusão concluída. {result.deleted_count} documentos foram removidos.")
    else:
        print("Operação cancelada. Nenhum dado foi excluído.")

except ConnectionFailure:
    print("Erro: Não foi possível conectar ao MongoDB. Verifique a URI ou a conexão de rede.")
except ConfigurationError as e:
    print(f"Erro de configuração: {e}")
except Exception as e:
    print(f"Erro inesperado: {e}")
finally:
    # Fechar a conexão com o MongoDB
    try:
        client.close()
    except:
        pass