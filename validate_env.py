import sys


def main():
    print("Iniciando a validação de ambiente para MLOps...")

    # Valida a versão do Python
    version = sys.version_info
    print(
        f"Versão do Python: "
        f"{version.major}.{version.minor}.{version.micro}"
    )

    if version.major < 3 or (
        version.major == 3 and version.minor < 8
    ):
        print(
            "ERRO: O pipeline exige Python 3.8 ou superior "
            "para Machine Learning."
        )
        sys.exit(1)

    print(
        "SUCESSO: Ambiente validado e pronto "
        "para os próximos passos."
    )
    sys.exit(0)


if __name__ == "__main__":
    main()