import pymongo
import pandas as pd

# Configuração da conexão com o MongoDB
mongo_uri = "mongodb+srv://admDB:eOX5boI6o8gcF90j@cluster0.ozsm1jh.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
database_name = "vulnerability_db"
collection_name = "scan_results"
output_csv = "dados_mongodb.csv"

# Conectar ao MongoDB
client = pymongo.MongoClient(mongo_uri)
db = client[database_name]
collection = db[collection_name]

# Consultar dados da coleção
data = list(collection.find())

# Converter os dados para um DataFrame do pandas
df = pd.DataFrame(data)

# Remover o campo '_id' do MongoDB, se necessário (Power BI pode não lidar bem com ele)
if '_id' in df.columns:
    df = df.drop('_id', axis=1)

# Salvar o DataFrame em um arquivo CSV
df.to_csv(output_csv, index=False, encoding='utf-8')

# Exibir o DataFrame (será usado diretamente pelo Power BI)
print(df)

# Fechar a conexão com o MongoDB
client.close()