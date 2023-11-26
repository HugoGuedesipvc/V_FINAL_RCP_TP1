import xmlrpc.client

def send_csv_to_server(server, csv_path, file_name):
    try:
        with open(csv_path, 'rb') as csv_file:
            csv_data = xmlrpc.client.Binary(csv_file.read())
            server.save_csv_file(file_name, csv_data)
            print(f"Arquivo CSV '{file_name}' enviado com sucesso.")
    except Exception as e:
        print(f"Erro ao enviar o arquivo CSV: {e}")

def list_xml_bd(server):
    try:
        result = server.list_xml()
        if result:
            print("Lista de arquivos XML:")
            for item in result:
                print(item)
        else:
            print("Nenhum arquivo XML encontrado.")
    except Exception as e:
        print(f"Erro ao listar arquivos XML: {e}")

if __name__ == "__main__":
    try:
        print("Conectando ao servidor...")
        server = xmlrpc.client.ServerProxy('http://is-rpc-server:9000')
        print("Conexão ao servidor estabelecida com sucesso.")

        csv_path = 'cars.csv'
        #send_csv_to_server(server, csv_path, "cars_csv")
        list_xml_bd(server)
        server.routinas_query(int(1))

        while True:
            print("\nMenu:")
            print("1. Enviar arquivo CSV")
            print("2. Eliminar arquivo XML")
            print("3. Filtrar por país")
            print("4. Filtrar por ano")
            print("5. Pesquisar carros")
            print("6. Listar pessoas ordenadas por nome")
            print("7. Filtrar carros por marca")
            print("8. Sair")

            choice = input("Escolha uma opção (1-8): ")

            if choice == '1':
                csv_name = input("Digite o nome do arquivo CSV: ")
                print("Ficheiro scv a ser processado...")
                send_csv_to_server(server, "cars.csv", csv_name)
                print("Ficheiro scv finalizado")

            elif choice == '2':
                list_xml_bd(server)
                id_to_remove = input("Digite o ID do arquivo XML para remover: ")
                server.eliminar_xml(id_to_remove)

            elif '3' <= choice <= '7':
                server.routinas_query(int(choice))

            elif choice == '8':
                print("Saindo do programa.")
                break

            else:
                print("Opção inválida. Tente novamente.")
    except Exception as e:
        print(f"Erro durante a execução do cliente: {e}")
