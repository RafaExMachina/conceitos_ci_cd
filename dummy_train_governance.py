import os
import pickle
import sys

import pandas as pd
from sklearn.tree import DecisionTreeClassifier


def main():
    print("Iniciando Dummy Training...")

    try:
        df = pd.read_csv("dataset_processado.csv")

        X = df[["feature1", "feature2"]]
        y = df["target"]

        clf = DecisionTreeClassifier(
            max_depth=2,
            random_state=42,
        )
        clf.fit(X, y)

        # Simulação de salvamento do modelo em disco
        # como um artefato binário
        with open("modelo.pkl", "wb") as arquivo:
            pickle.dump(clf, arquivo)

        # ==========================================
        # GOVERNANÇA: Integração com Model Registry
        # ==========================================
        commit_sha = os.environ.get(
            "GITHUB_SHA",
            "Desconhecido",
        )

        print(
            "\n--- Integrando com o Model Registry "
            "(Ex: MLflow) ---"
        )
        print(
            "Enviando o arquivo modelo.pkl para "
            "o armazenamento central..."
        )
        print(f"Commit SHA associado: {commit_sha}")
        print("Modelo registrado com sucesso!")

        score = clf.score(X, y)

        print(
            "SUCESSO: Modelo treinado sem erros de sintaxe! "
            f"Acurácia no micro-dataset: {score:.2f}"
        )
        sys.exit(0)

    except FileNotFoundError as error:
        print(
            "ERRO: O arquivo dataset_processado.csv "
            f"não foi encontrado. Detalhes: {error}"
        )
        sys.exit(1)

    except (
        KeyError,
        OSError,
        TypeError,
        ValueError,
        pd.errors.EmptyDataError,
        pd.errors.ParserError,
    ) as error:
        print(
            "ERRO DE COMPUTAÇÃO: O código do modelo falhou. "
            f"Detalhes: {error}"
        )
        sys.exit(1)


if __name__ == "__main__":
    main()