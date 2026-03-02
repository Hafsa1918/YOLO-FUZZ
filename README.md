# YOLO-FUZZ
This repository provides modified YOLO framework with fuzzy based anchor selection for tiny traffic sign detection.

This work is adaption from [Ultralytics/yolov5](https://github.com/ultralytics/yolov5), modifying standard YOLOv5 network for optimized detection of small traffic signs in complex road scenes.

# Author
[Hafsa Amanullah] - 🌐 [Github](https://github.com/Hafsa1918) - 🌐 [LinkedIn Profile](https://www.linkedin.com/in/hafsa-amanullah) - [Google scholar](https://scholar.google.com/citations?user=up19UMQAAAAJ&hl=en)

# Collaborators
[Prof. Dr. Min Young Kim] - 🌐 [Google scholar](https://scholar.google.com.pk/citations?user=Xhawz8EAAAAJ&hl=en)

[Dr. Yawar Rehman] - 🌐 [Github](https://github.com/YawarGuguma) - 🌐 [LinkedIn Profile](https://www.linkedin.com/in/yawar-rehman-820118b/) - [Google scholar](https://scholar.google.com/citations?hl=en&user=VclpjuIAAAAJ)

# Datasets used

The proposed work is tested on German and Swedish traffic sign dataset. Both of the datasets are open-source and easily accessible through the following links:

[GTSDB](https://benchmark.ini.rub.de/gtsdb_dataset.html)

[STS](https://www.cvl.isy.liu.se/research/datasets/traffic-signs-dataset/)


# Usage steps

You may use this code for small traffic sign detection by following these simple steps.

1- Estimate anchors using anchorboxSortScale_fuzzy.m file

2- Copy test and train images(with .jpg file extension) in datasets/gtsdb_Test and datasets/gtsdb_Train respectively

3- Generate and save .yaml file in **Data** folder

4- Install dependencies, stated in [requirements.txt](https://github.com/Hafsa1918/YOLO-FUZZ/blob/main/requirements.txt)

5- Use [train.py](https://github.com/Hafsa1918/YOLO-FUZZ/blob/main/train.py) to train your network. 

6- Use [detect.py](https://github.com/Hafsa1918/YOLO-FUZZ/blob/main/detect.py) to test the trained network with test images.



# Test results of the proposed algorithm on German Traffic Sign Dataset Benchmark
![amanu8](https://github.com/ha007-aman/SmallObjectDetection/assets/73087518/480464da-9626-47aa-b4b3-7fa2e479ae8b)

Traffic sign detection in GTSDB dataset (a) Traffic sign size variation in an image (b \& d) Small traffic sign detection (c) A larger traffic sign recognition

# Test results of the proposed algorithm on Swedish Traffic Sign Dataset 
![amanu9](https://github.com/ha007-aman/SmallObjectDetection/assets/73087518/66cc4035-8c93-49fc-b995-a302b03383d7)

Traffic sign detection in STS dataset (a-c) Small-sized traffic sign detection (d) A large-sized traffic sign detection
