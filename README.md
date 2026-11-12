# Detector de cédulas de real

Projeto experimental criado com o objetivo de ajudar pessoas com deficiência visual a identificar cédulas de real e saber o valor aproximado de um conjunto de dinheiro.

## Como funciona

O notebook `Detector_de_Notas.ipynb` analisa a imagem `montante.jpg`. Ele compara regiões da imagem com modelos das cédulas disponíveis, usando processamento de imagem e reconhecimento de características. Ao final, exibe as cédulas identificadas e a soma estimada.

O script `analisador_HSV.py` é uma ferramenta auxiliar para ajustar os limites de cor HSV usados na análise. Ele abre a imagem `Exemplo1.png` e permite ajustar os valores pelos controles deslizantes.

As imagens de referência incluídas são do anverso das cédulas de R$ 2, R$ 5, R$ 10, R$ 20, R$ 50, R$ 100 e R$ 200.

## Requisitos

- Python 3
- Jupyter Notebook
- OpenCV, NumPy e Matplotlib

No Windows, abra o PowerShell na pasta do projeto e instale as dependências:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install opencv-python numpy matplotlib jupyter
```

## Como executar

Para executar o detector:

```powershell
jupyter notebook Detector_de_Notas.ipynb
```

No notebook aberto, execute as células em ordem. A imagem a analisar deve estar salva como `montante.jpg` na pasta do projeto.

Para abrir a ferramenta de ajuste HSV:

```powershell
python analisador_HSV.py
```

O script usa `Exemplo1.png`, que também deve estar na pasta do projeto. Ajuste os controles na janela e pressione `q` ou `Esc` para sair.

## Limitações e acessibilidade

Este projeto ainda é um protótipo: analisa imagens estáticas e pode errar conforme a iluminação, o enquadramento, o estado das cédulas e o fundo. O resultado atual é apresentado visualmente; o projeto ainda não anuncia os valores por voz nem oferece uma interface acessível para uso independente por pessoas cegas. Portanto, os valores identificados devem ser conferidos e não devem ser considerados uma confirmação confiável do montante.
