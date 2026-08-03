import pandas as pd


def main():
    print("Extraindo e processando dados brutos...")

    # Simulando a criação de um dataset processado
    dados = {
        "feature1": [1.2, 3.4, 5.5, 7.1],
        "feature2": [0.1, 0.2, 0.5, 0.9],
        "target": [0, 1, 0, 1],
    }

    df = pd.DataFrame(dados)

    # Salva o arquivo CSV no diretório atual
    df.to_csv("dataset_processado.csv", index=False)

    print("SUCESSO: dataset_processado.csv gerado com sucesso!")


if __name__ == "__main__":
    main()