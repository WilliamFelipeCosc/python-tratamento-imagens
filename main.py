import cv2
import numpy as np

import tkinter as tk
from tkinter import filedialog
from tkinterdnd2 import DND_FILES, TkinterDnD
from PIL import Image, ImageTk

def gaussian_blur(img):
  KSIZE = (15,15)
  sigmax = 0

  return cv2.GaussianBlur(img, KSIZE, sigmax)

def sharpen_image(img):
  kernel = np.array([[0, -1, 0],
                  [-1, 5, -1],
                  [0, -1, 0]])
  return cv2.filter2D(img, -5, kernel)

def rotate_image(img):
  (h, w) = img.shape[:2]
  centro = (w // 2, h // 2)

  # Cria a rotação e aplica ela
  matriz_rotacao = cv2.getRotationMatrix2D(centro, 45, 1.0)
  return cv2.warpAffine(img, matriz_rotacao, (w, h))

def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg *.jpeg *.png")])
    if file_path:
        carregar_imagem(file_path)

def carregar_imagem(caminho):
    global imagem_cv, imagem_tk
    imagem_cv = cv2.imread(caminho)
    imagem_cv = cv2.cvtColor(imagem_cv, cv2.COLOR_BGR2RGB)  # Conversão de BGR para RGB
    imagem_pil = Image.fromarray(imagem_cv)
    imagem_pil.thumbnail((400, 400))
    imagem_tk = ImageTk.PhotoImage(imagem_pil)
    img_label.config(image=imagem_tk)
    img_label.image = imagem_tk

def aplicar_blur():
  global imagem_cv
  img_blur = gaussian_blur(imagem_cv)
  imagem_pil = Image.fromarray(img_blur)
  imagem_pil.thumbnail((400, 400))
  imagem_tk_blur = ImageTk.PhotoImage(imagem_pil)
  img_label.config(image=imagem_tk_blur)
  img_label.image = imagem_tk_blur

def aplicar_sharp():
  global imagem_cv
  img_sharp = sharpen_image(imagem_cv)
  imagem_pil = Image.fromarray(img_sharp)
  imagem_pil.thumbnail((400, 400))
  imagem_tk_sharpen = ImageTk.PhotoImage(imagem_pil)
  img_label.config(image=imagem_tk_sharpen)
  img_label.image = imagem_tk_sharpen

def aplicar_rotate():
  global imagem_cv
  img_rotate = rotate_image(imagem_cv)
  imagem_pil = Image.fromarray(img_rotate)
  imagem_pil.thumbnail((400, 400))
  imagem_tk_rotate = ImageTk.PhotoImage(imagem_pil)
  img_label.config(image=imagem_tk_rotate)
  img_label.image = imagem_tk_rotate

root = TkinterDnD.Tk()
root.title("Importar Imagem")
root.geometry("400x500")

frame = tk.Frame(root)
frame.pack(pady=10)

img_label = tk.Label(frame)
img_label.pack()

btn_open = tk.Button(root, text="Escolher Imagem", command=open_file)
btn_open.pack(pady=5)

btn_action1 = tk.Button(root, text="Aplicar Blur", command=aplicar_blur)
btn_action1.pack(pady=5)

btn_action2 = tk.Button(root, text="Aplicar Sharpen", command=aplicar_sharp)
btn_action2.pack(pady=5)

btn_action3 = tk.Button(root, text="Aplicar Rotação", command=aplicar_rotate)
btn_action3.pack(pady=5)

root.mainloop()