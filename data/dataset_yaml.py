import csv
import os

def generate_ground_truth(csv_file, output_dir):
    # Create output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
   
    with open(csv_file, 'r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  # Skip header row if exists
       
        for row in csv_reader:
            image_file = row[0]  # Assuming first column contains image file name
            ground_truth = row[1:]  # Assuming subsequent columns contain ground truth information
           
            # Create ground truth file
            ground_truth_file = os.path.splitext(image_file)[0] + '.txt'
            with open(os.path.join(output_dir, ground_truth_file), 'w') as gt_file:
                for item in ground_truth:
                    gt_file.write("%s " % item)

# Example usage
csv_file = 'annotations_patches_yaml.csv'
output_directory = 'labels'
generate_ground_truth(csv_file, output_directory)
