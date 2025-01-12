import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

def preprocess_image(image_path):
    """
    Preprocess the image for analysis: resize, convert to grayscale, and normalize.
    """
    # Load image
    image = cv2.imread(image_path)
    
    # Check if the image was loaded correctly
    if image is None:
        print("Error: Image not found.")
        return None, None
    
    # Resize image for consistent analysis
    image_resized = cv2.resize(image, (500, 500))
    
    
    # Convert to grayscale
    gray_image = cv2.cvtColor(image_resized, cv2.COLOR_BGR2GRAY)
    
    # Normalize pixel values to range [0, 1]
    gray_image = gray_image / 255.0
    
    return image_resized, gray_image

def analyze_soil_condition(image):
    """
    Analyze soil condition based on color/texture. (Example: based on color intensity).
    Returns a text condition like 'Wet', 'Moist', 'Dry', 'Alkaline Soil', 'Sand Soil', etc.
    """
   
    avg_intensity = np.mean(image)
    
    # Print the average intensity to help fine-tune the threshold
    print(f"Average Intensity: {avg_intensity:.3f}")
    
    # Condition based on observations
    if avg_intensity > 0.69:
        condition = "Flooded Soil"
    elif 0.60 <= avg_intensity <= 0.68:
        condition = "Sand Soil"
    elif 0.50 <= avg_intensity <= 0.599:
        condition = "Alkaline Soil"
    elif 0.45 <= avg_intensity <= 0.50:
        condition = "Dry Soil"
    elif 0.30 <= avg_intensity <= 0.45:
        condition = "Moist"
    elif avg_intensity <= 0.25:
        condition = "Wet"
    
    return condition

def get_preventive_measures(condition):
    """
    Return preventive measures based on soil condition.
    """
    preventive_measures = {
        "Flooded Soil": (
            "Prevent flooding by improving drainage systems. Consider installing French drains or surface drains to redirect excess water. \n"
            "Ensure the soil has good aeration to avoid root rot. \nRegularly monitor water levels and avoid over-irrigation."
        ),
        
        "Sand Soil": (
            "Improve moisture retention by adding organic compost or mulch to the soil.\nConsider mixing in loamy soil for better structure. \n"
            "Regular watering and adding fertilizers is essential as sandy soil leaches nutrients quickly."
        ),
        
        "Alkaline Soil": (
            "Add sulfur or organic materials like peat moss to reduce pH levels.\nThis helps make the soil more acidic for better plant growth. \n"
            "Test the pH regularly to avoid drastic changes, which could harm plant roots."
        ),
        
        "Dry Soil": (
            "Increase irrigation frequency, and use drip irrigation to ensure water reaches plant roots. \n"
            "Add organic matter to improve moisture retention. \n"
            "Monitor soil moisture to avoid both overwatering and underwatering."
        ),
        
        "Moist": (
            "Ensure proper drainage to avoid waterlogging.\nIf necessary, improve soil texture with organic compost to maintain optimal moisture levels. \n"
            "Check moisture regularly and adjust watering accordingly."
        ),
        
        "Wet": (
            "Improve drainage by incorporating sand or organic matter, and consider creating raised beds.\nAvoid over-irrigating and ensure proper air circulation around plant roots. \n"
            "Refrain from tilling the soil when wet to prevent compaction."
        )
    }
    
    return preventive_measures.get(condition, "No preventive measures available.")

def write_condition_to_file(condition, preventive_measures):
    """
    Write the soil condition and preventive measures to a separate text file based on the condition,
    and store the file inside a 'solutions' folder.
    """
    
    if not os.path.exists("solutions"):
        os.makedirs("solutions")
    
    # Create a filename based on the soil condition
    filename = f"solutions/{condition.replace(' ', '_')}.txt"
    
    # Write the condition and preventive measures to the file inside the 'solutions' folder
    with open(filename, 'w') as file:
        file.write(f"Soil Condition: {condition}\n")
        file.write(f"Preventive Measures:\n{preventive_measures}\n")
    print(f"Preventive measures written to {filename}")

def display_results(image, condition, gray_image=None):
    """
    Display the image and soil condition.
    """
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title(f"Predicted Soil Condition: {condition}")
    plt.axis('off')  # Turn off axes for better display
    plt.show()
    
    if gray_image is not None:
        # Display the grayscale image to better understand the pixel intensity
        plt.imshow(gray_image, cmap='gray')
        plt.title("Grayscale Image")
        plt.axis('off')
        plt.show()

def main(image_path):
    # Preprocess image
    image_resized, gray_image = preprocess_image(image_path)
    
    # Ensure the image was processed correctly
    if image_resized is None or gray_image is None:
        return
    
    # Analyze soil condition based on grayscale intensity
    condition = analyze_soil_condition(gray_image)
    
    # Get preventive measures for the identified condition
    preventive_measures = get_preventive_measures(condition)
    
    write_condition_to_file(condition, preventive_measures)
    
    # Display results
    display_results(image_resized, condition, gray_image)


image_path = "D:/Dilip/Mini-Project/Soil-image/Dry4.jpg"  # Update this with your image path
main(image_path)
