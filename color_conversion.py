import numpy as np
import colorsys
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

# Enhanced Base Color Palette with More Semantic Categories
BASE_COLORS = [
    # Warm Colors
    '#FF0000',    # Pure Red
    '#FF7F00',    # Orange
    '#FFD700',    # Gold
    
    # Cool Colors
    '#0000FF',    # Pure Blue
    '#00FFFF',    # Cyan
    '#4B0082',    # Indigo
    
    # Green Family
    '#00FF00',    # Pure Green
    '#90EE90',    # Light Green
    
    # Neutrals & Others
    '#FFFFFF',    # White
    '#000000',    # Black
    '#808080',    # Gray
    '#A52A2A'     # Brown
]

def rgb_to_hsv(rgb_color):
    """
    Convert RGB to HSV color space.
    
    Args:
        rgb_color (array): RGB color values
    
    Returns:
        tuple: HSV color values
    """
    return colorsys.rgb_to_hsv(*rgb_color)

def color_distance(color1, color2):
    """
    Calculate perceptual color distance using HSV color space.
    
    Args:
        color1 (array): First color in RGB
        color2 (array): Second color in RGB
    
    Returns:
        float: Perceptual color distance
    """
    # Convert to HSV
    hsv1 = rgb_to_hsv(color1)
    hsv2 = rgb_to_hsv(color2)
    
    # Weighted distance calculation
    # More weight to hue, less to saturation and value
    hue_diff = min(abs(hsv1[0] - hsv2[0]), 1 - abs(hsv1[0] - hsv2[0]))
    sat_diff = abs(hsv1[1] - hsv2[1])
    val_diff = abs(hsv1[2] - hsv2[2])
    
    # Empirical weighting
    return (hue_diff * 0.7 + sat_diff * 0.2 + val_diff * 0.1)

def semantic_color_mapping(input_colors, base_colors):
    """
    Map input colors to base colors with semantic understanding.
    
    Args:
        input_colors (list): List of input hex color codes
        base_colors (list): List of base hex color codes
    
    Returns:
        list: Mapped base colors with semantic perception
    """
    # Convert input and base colors to RGB
    input_rgb = [mcolors.to_rgb(color) for color in input_colors]
    base_rgb = [mcolors.to_rgb(color) for color in base_colors]
    
    mapped_colors = []
    for color in input_rgb:
        # Calculate distances with semantic weighting
        distances = [color_distance(color, base_color) for base_color in base_rgb]
        
        # Find the index of the closest base color
        closest_index = np.argmin(distances)
        mapped_colors.append(base_colors[closest_index])
    
    return mapped_colors

def visualize_semantic_mapping(input_colors, mapped_colors):
    """
    Visualize color mapping with semantic understanding.
    
    Args:
        input_colors (list): Original input colors
        mapped_colors (list): Semantically mapped colors
    """
    fig, ax = plt.subplots(figsize=(12, len(input_colors) * 0.5))
    
    for i, (orig, mapped) in enumerate(zip(input_colors, mapped_colors)):
        # Plot original color
        ax.add_patch(plt.Rectangle((0, i), 0.5, 1, color=orig))
        
        # Plot mapped base color
        ax.add_patch(plt.Rectangle((0.5, i), 0.5, 1, color=mapped))
        
        # Add text labels
        ax.text(0.25, i+0.5, orig, ha='center', va='center', fontsize=8)
        ax.text(0.75, i+0.5, mapped, ha='center', va='center', fontsize=8)
    
    ax.set_xlim(0, 1)
    ax.set_ylim(0, len(input_colors))
    ax.set_yticks([])
    ax.set_title('Semantic Color Mapping')
    
    plt.tight_layout()
    plt.show()

def main():
    # Expanded sample colors including challenging cases
    input_colors = [
        # Reds and Oranges
        '#FF0000', '#FF4500', '#FF6347', '#DC143C', 
        
        # Greens
        '#00FF00', '#32CD32', '#90EE90', '#00FA9A',
        
        # Blues and Cyans
        '#0000FF', '#4169E1', '#1E90FF', '#87CEEB', '#00FFFF',
        
        # Oranges and Yellows
        '#FFA500', '#FF8C00', '#FFD700', '#DAA520',
        
        # Purples
        '#800080', '#9932CC', '#BA55D3', '#DA70D6',
        
        # Teals and Blue-Greens
        '#008080', '#20B2AA', '#48D1CC', '#40E0D0'
    ]
    
    # Map input colors to base colors
    mapped_colors = semantic_color_mapping(input_colors, BASE_COLORS)
    
    # Print detailed mapping
    print("Semantic Color Mapping:")
    for orig, mapped in zip(input_colors, mapped_colors):
        print(f"{orig} → {mapped}")
    
    # Visualize the mapping
    visualize_semantic_mapping(input_colors, mapped_colors)

if __name__ == '__main__':
    main()
