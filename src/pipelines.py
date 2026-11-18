from src.methods import (
    to_grayscale, apply_sobel, threshold_segmentation, 
    histogram_equalization, adjust_brightness
)

def run_pipeline(image, pipeline_name, config):
    if pipeline_name == "student1_p1":
        # Учасник 1: Виявлення замаскованої техніки (контурний аналіз)
        s1 = to_grayscale(image)
        s2 = apply_sobel(s1)
        s3 = threshold_segmentation(s2, config.get("threshold", 100))
        return s3
        
    elif pipeline_name == "student2_p1":
        # Учасник 2: Виявлення цілей в умовах туману/диму (максимізація контрасту)
        s1 = to_grayscale(image)
        s2 = histogram_equalization(s1)
        s3 = threshold_segmentation(s2, config.get("threshold", 120))
        return s3

    elif pipeline_name == "student1_p2":
        # Учасник 1: Покращення темних розвідувальних знімків з БПЛА
        s1 = adjust_brightness(image, config.get("brightness_offset", 40))
        s1_gray = to_grayscale(s1)
        s2 = histogram_equalization(s1_gray)
        return s2
        
    else:
        raise ValueError(f"Невідомий пайплайн: {pipeline_name}")