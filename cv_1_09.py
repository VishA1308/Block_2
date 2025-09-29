import numpy as np
import cv2 
import matplotlib.pyplot as plt
import os
from cv_1_07 import *

def get_image_path():
    """
    Запрашивает путь к изображению с проверкой его существования и корректности.
    
    Returns:
        str: Путь к корректному изображению
        
    """
    while True:
        image_path = input("Введите название изображения (путь): ").strip()
        
        
        if not image_path:
            print("Ошибка: Путь не может быть пустым.")
            continue
            
        
        if not os.path.exists(image_path):
            print(f"Ошибка: Файл '{image_path}' не существует.")
            continue
            
            
        test_img = cv2.imread(image_path)
        if test_img is None:
            print(f"Ошибка: Не удалось открыть изображение '{image_path}'.")
            continue
            
        return image_path

def main()->None:

    """
    Основная функция программы.
    
    Загружает два изображения, строит их гистограммы и сравнивает их.
    Выводит результаты сравнения в консоль.
    """

    src1 = get_image_path()
    img1 = load_img_color(src1)
    
    if img1 is None:
       raise ValueError(f"Could not open image: {src1}")

    img1 = cv2.resize(img1, (400, 400))
    
    fig_1, axes_1, histograms_1 = plot_color_histograms(img1)

    src2 = get_image_path()
    img2 = load_img_color(src2)
    
    if img2 is None:
       raise ValueError(f"Could not open image: {src2}")

    img2 = cv2.resize(img2, (400, 400))
    
    fig_2, axes_2, histograms_2 = plot_color_histograms(img2)

    similar, avg_cor = compare_histograms(histograms_1, histograms_2)
    print(f"Average correlation coefficient: {avg_cor}")


def compare_histograms(hist_1, hist_2):

    """
    Сравнивает гистограммы двух изображений по каналам.
    
    Parameters:
        hist_1 (list): Список гистограмм для первого изображения 
        hist_2 (list): Список гистограмм для второго изображения 
        
    Returns:
        tuple: (similarity, avg_correlation)
            - similarity (list): Коэффициенты корреляции для каждого канала
            - avg_correlation (float): Средний коэффициент корреляции по всем каналам

    """
     
    similarity = []
    
    for i in range(3):

        hist1 = hist_1[i].flatten().astype(np.float32)
        hist2 = hist_2[i].flatten().astype(np.float32)
        

        if np.sum(hist1) == 0 or np.sum(hist2) == 0:
            print(f"Warning: Channel {i} has zero histogram")
            similarity.append(0.0)
            continue
            
        # Нормализация
        hist1_norm = cv2.normalize(hist1, None, 1, 0, cv2.NORM_L1)
        hist2_norm = cv2.normalize(hist2, None, 1, 0, cv2.NORM_L1)
    

        # Сравниваем гистограммы
        similar = cv2.compareHist(hist1_norm, hist2_norm, cv2.HISTCMP_CORREL)
        similar_abs = abs(similar)
        similarity.append(similar)

        print(f"Channel {i} correlation: {similar:.4f}")

    avg_correlation = np.mean(similarity)
 
    
    return similarity, avg_correlation

if __name__ == "__main__":
    main()
