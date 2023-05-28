:brazil:**Versão em Português:**


# Projeto Barcode To IMG

Este projeto tem como objetivo realizar a análise de texto OCR em uma tabela e a leitura de um código de barras (barcode) a partir de imagens capturadas por uma câmera IP. Ele utiliza as bibliotecas OpenCV e Tesseract para processamento de imagens e reconhecimento de texto, e a biblioteca Tkinter para criar a interface gráfica.

---

## Pré-requisitos

- Python 3.7 ou superior
- Poetry (gerenciador de dependências)

---

## Instalação do Poetry

O Poetry é necessário para gerenciar as dependências do projeto. Caso ainda não tenha o Poetry instalado, siga as instruções no [site oficial](https://python-poetry.org/) para instalá-lo.

Após a instalação, verifique se o Poetry foi instalado corretamente executando o seguinte comando no terminal:

```shell
poetry --version
```

---

## Instalação

1. Clone este repositório para o seu ambiente local.
2. Acesse o diretório raiz do projeto.
3. Execute o seguinte comando para instalar as dependências e ativar o ambiente virtual usando o Poetry:

```shell
poetry install && poetry shell
```

---

## Uso

Por favor, observe que este projeto ainda está em desenvolvimento, e algumas funcionalidades podem não estar totalmente operacionais. No entanto, a ideia geral de uso é a seguinte:

1. Modifique a variável `url` com o IP e a porta da sua câmera, e certifique-se de que ela está conectada e acessível.
2. Execute o seguinte comando para iniciar o aplicativo:

```shell
python main.py
```

3. A interface gráfica será aberta. Você verá um botão para capturar a imagem e realizar a análise OCR da tabela e do código de barras.
4. Os resultados serão exibidos na interface gráfica.

:us: **English Version:**

# Project Barcode To IMG

This project aims to perform OCR text analysis on a table and read a barcode from images captured by an IP camera. It utilizes the OpenCV and Tesseract libraries for image processing and text recognition, and the Tkinter library to create the graphical interface.

---

## Prerequisites

- Python 3.7 or higher
- Poetry (dependency manager)

---

## Poetry Installation

Poetry is required to manage the project dependencies. If you don't have Poetry installed yet, follow the instructions on the [official website](https://python-poetry.org/) to install it.

After installation, verify if Poetry was installed correctly by running the following command in the terminal:

```shell
poetry --version
```

---

## Installation

1. Clone this repository to your local environment.
2. Navigate to the project's root directory.
3. Run the following command to install the dependencies and activate the virtual environment using Poetry:

```shell
poetry install && poetry shell
```

---

## Usage

Please note that this project is still under development, and some features may not be fully operational. However, the general idea of usage is as follows:

1. Modify the `url` variable with the IP and port of your camera, and ensure it is connected and accessible.
2. Execute the following command to start the application:

```shell
python main.py
```

3. The graphical interface will open. You will see a button to capture the image and perform OCR analysis on the table and barcode.
4. The results will be displayed in the graphical interface.
