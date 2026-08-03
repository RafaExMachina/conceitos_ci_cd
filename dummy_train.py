import sys

import pandas as pd
from sklearn.tree import DecisionTreeClassifier


def main():
    print("Iniciando Dummy Training (Treinamento de Sanidade)...")

    try:
        # Carrega os dados gerados pelo pipeline
        df = pd.read_csv("dataset_processado.csv")

        # Separa features e target
        X = df[["feature1", "feature2"]]
        y = df["target"]

        # Treina um modelo simples
        clf = DecisionTreeClassifier(
            max_depth=2,
            random_state=42,
        )
        clf.fit(X, y)

        score = clf.score(X, y)

        print(
            "SUCESSO: Modelo treinado sem erros! "
            f"Acurácia no micro-dataset: {score:.2f}"
        )

    except FileNotFoundError as error:
        print(
            "ERRO: O arquivo dataset_processado.csv "
            f"não foi encontrado. Detalhes: {error}"
        )
        sys.exit(1)

    except (
        pd.errors.EmptyDataError,
        pd.errors.ParserError,
        KeyError,
        TypeError,
        ValueError,
    ) as error:
        print(
            "ERRO DE TREINAMENTO: Não foi possível carregar os dados "
            f"ou treinar o modelo. Detalhes: {error}"
        )
        sys.exit(1)

    sys.exit(0)


if __name__ == "__main__":
    main()