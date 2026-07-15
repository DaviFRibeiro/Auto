# Auto — Inicializador de Aplicativos

Automação de desktop em Python que abre uma sequência de aplicativos com um clique, usando PyAutoGUI para controlar o sistema e Tkinter para a interface.

## Como funciona

1. A janela principal (Tkinter) exibe o botão de início.
2. Ao iniciar, uma contagem regressiva dá tempo de liberar o mouse/teclado.
3. O PyAutoGUI executa a sequência de aberturas automaticamente.

## Tecnologias

- **Python 3**
- **Tkinter** — interface gráfica
- **PyAutoGUI** — automação de mouse/teclado
- **Pillow** — carregamento de imagens da interface

## Como executar

```bash
git clone https://github.com/DaviFRibeiro/Auto.git
cd Auto

pip install pyautogui pillow
python app.py
```

> Projeto de estudo de automação de desktop.
