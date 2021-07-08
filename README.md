# RAS-Pets

O projeto **RAS-Pets** é um comedouro automático que tem como objetivo inovar e facilitar a alimentação de cachorros e gatos, sem que seja necessária a ação direta  e constante de um humano.

### Como funciona?

> A rede neural do YOLOv5 será capaz de identificar e diferenciar essas duas espécies, de modo que, quando algum pet se aproximar do alimentador, uma quantidade de ração própria para o tipo identificado será liberada para o consumo imediato. O hardware utilizado para que essa aplicação seja possível será o Raspberry Pi, que nada mais é do que um microcomputador.

### Aplicação

> É destinado para uso restrito, como em residências, centros de zoonoses e abrigo para animais abandonados.

## Processo de estruturação

Em seguida, detalharemos por tópicos cada parte constituinte desse projeto. Acompanhe:

### Microcontroladores

- Protótipo
  - Arduíno
- Versão oficial
  - Raspberrry Pi
  
### Materiais utilizados

- Protótipo
  - Madeira;
  - Serra tico-tico;
  - Parafusos;
  - Furadeira;
  - Cano PVC;
  - Cap PVC;
  - Arduíno.
- Versão oficial


### Ferramentas utilizadas para o software

- YOLOv5;
- Anaconda.

## Instalação do YOLOv5

1° - Criar o environment do Conda com o python 3.7:

`conda create -n myenv python=3.7`


2° - Clonar o Repositório:

`git clone https://github.com/RAS-Unesp-Bauru/Ras-pets`


3° - Instalar o arquivo "requirements.txt":

`pip install -r requirements.txt`


4° - Instalar a biblioteca pandas:

`pip install pandas`


5° - Instalar a biblioteca seaborn:

`pip install seaborn`


6° - Instalar o "cocotools":

`pip install pycocotools`


7° - Instalar a biblioteca thop:

`pip install thop`


8° - Rodar o código:

`python detect.py --source 0 --weights yolov5s.pt --conf 0.25 --classes 0`

