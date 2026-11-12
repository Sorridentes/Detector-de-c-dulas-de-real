import cv2
import numpy as np

# Função que não faz nada, apenas para o trackbar (obrigatório no OpenCV)
def nothing(x):
    pass

# 1. Carregar a imagem
image_path = 'Exemplo1.png'
img = cv2.imread(image_path)

if img is None:
    print(f"Erro: Não foi possível carregar a imagem '{image_path}'.")
    exit()

# Converter para HSV
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Reduzir apenas a visualização quando a imagem for muito grande
height, width = img.shape[:2]
max_display_width = 900
max_display_height = 650
scale = min(1, max_display_width / width, max_display_height / height)
display_size = (int(width * scale), int(height * scale))
display_img = cv2.resize(img, display_size, interpolation=cv2.INTER_AREA) if scale < 1 else img

# 2. Criar as janelas
cv2.namedWindow('Imagem Original')
cv2.namedWindow('Mascara Ajustavel')

# 3. Criar os Trackbars (Sliders)
# cv2.createTrackbar('H Lower', 'Mascara Ajustavel', 0, 179, nothing)
# cv2.createTrackbar('H Upper', 'Mascara Ajustavel', 179, 179, nothing)
# cv2.createTrackbar('S Lower', 'Mascara Ajustavel', 0, 255, nothing)
# cv2.createTrackbar('S Upper', 'Mascara Ajustavel', 255, 255, nothing)
# cv2.createTrackbar('V Lower', 'Mascara Ajustavel', 0, 255, nothing)
# cv2.createTrackbar('V Upper', 'Mascara Ajustavel', 255, 255, nothing)
cv2.createTrackbar('H Lower', 'Mascara Ajustavel', 13, 179, nothing)
cv2.createTrackbar('H Upper', 'Mascara Ajustavel', 90, 179, nothing)
cv2.createTrackbar('S Lower', 'Mascara Ajustavel', 0, 255, nothing)
cv2.createTrackbar('S Upper', 'Mascara Ajustavel', 40, 255, nothing)
cv2.createTrackbar('V Lower', 'Mascara Ajustavel', 0, 255, nothing)
cv2.createTrackbar('V Upper', 'Mascara Ajustavel', 165, 255, nothing)

print("Ajuste os sliders na janela 'Mascara Ajustavel'. Pressione 'q' ou 'ESC' para sair.")

while True:
    # 4. Ler os valores atuais dos trackbars
    h_lower = cv2.getTrackbarPos('H Lower', 'Mascara Ajustavel')
    h_upper = cv2.getTrackbarPos('H Upper', 'Mascara Ajustavel')
    s_lower = cv2.getTrackbarPos('S Lower', 'Mascara Ajustavel')
    s_upper = cv2.getTrackbarPos('S Upper', 'Mascara Ajustavel')
    v_lower = cv2.getTrackbarPos('V Lower', 'Mascara Ajustavel')
    v_upper = cv2.getTrackbarPos('V Upper', 'Mascara Ajustavel')

    # Montar os arrays atualizados
    lower = np.array([h_lower, s_lower, v_lower])
    upper = np.array([h_upper, s_upper, v_upper])

    # 5. Gerar a máscara
    mask = cv2.inRange(img_hsv, lower, upper)

    # 6. Mostrar os resultados
    display_mask = cv2.resize(mask, display_size, interpolation=cv2.INTER_NEAREST) if scale < 1 else mask
    cv2.imshow('Imagem Original', display_img)
    cv2.imshow('Mascara Ajustavel', display_mask)

    # 7. Condição de saída
    key = cv2.waitKey(1) & 0xFF
    if key == 27 or key == ord('q'):
        print("\n" + "="*50)
        print("--- ARRAYS NUMPY ---")
        print("="*50)
        print(f"lower = np.array([{h_lower}, {s_lower}, {v_lower}])")
        print(f"upper = np.array([{h_upper}, {s_upper}, {v_upper}])")
        
        print("\n" + "="*50)
        print("--- LINHAS DO CREATETRACKBAR ---")
        print("="*50)
        print(f"cv2.createTrackbar('H Lower', 'Mascara Ajustavel', {h_lower}, 179, nothing)")
        print(f"cv2.createTrackbar('H Upper', 'Mascara Ajustavel', {h_upper}, 179, nothing)")
        print(f"cv2.createTrackbar('S Lower', 'Mascara Ajustavel', {s_lower}, 255, nothing)")
        print(f"cv2.createTrackbar('S Upper', 'Mascara Ajustavel', {s_upper}, 255, nothing)")
        print(f"cv2.createTrackbar('V Lower', 'Mascara Ajustavel', {v_lower}, 255, nothing)")
        print(f"cv2.createTrackbar('V Upper', 'Mascara Ajustavel', {v_upper}, 255, nothing)")
        print("="*50 + "\n")
        break

cv2.destroyAllWindows()