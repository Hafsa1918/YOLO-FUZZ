# YOLO-FUZZ
This repository provides modified YOLO framework with fuzzy based anchor selection for tiny traffic sign detection

# Author
[Hafsa Amanullah] - 🌐 [Github](https://github.com/Hafsa1918) - 🌐 [LinkedIn Profile](https://www.linkedin.com/in/hafsa-amanullah)

# Collaborators
[Prof. Dr. Min Young Kim] - 🌐 [Google scholar](https://scholar.google.com.pk/citations?user=Xhawz8EAAAAJ&hl=en)

[Dr. Yawar Rehman] - 🌐 [Github](https://github.com/YawarGuguma) - 🌐 [LinkedIn Profile](https://www.linkedin.com/in/yawar-rehman-820118b/)

# Steps

You may use this code for small traffic sign detection by following these simple steps.

1- Estimate anchors using anchors.mat file

2- Copy test and train images in datasets/gtsdb_Test and datasets/gtsdb_Train respectively

3- Save gtsdb.yaml file in **Data** folder

4- Install dependencies, stated in [requirements.txt](https://github.com/Hafsa1918/YOLO-FUZZ/blob/main/requirements.txt)

5- Use [train.py](https://github.com/Hafsa1918/YOLO-FUZZ/blob/main/train.py) to train your network. 

6- Use [detect.py](https://github.com/Hafsa1918/YOLO-FUZZ/blob/main/detect.py) to test the trained network with test images.



# Test results of the proposed algorithm on German Traffic Sign Dataset Benchmark
![amanu8](https://github.com/ha007-aman/SmallObjectDetection/assets/73087518/480464da-9626-47aa-b4b3-7fa2e479ae8b)

Traffic sign detection in GTSDB dataset (a) Traffic sign size variation in an image (b \& d) Small traffic sign detection (c) A larger traffic sign recognition

# Test results of the proposed algorithm on Swedish Traffic Sign Dataset 
![amanu9](https://github.com/ha007-aman/SmallObjectDetection/assets/73087518/66cc4035-8c93-49fc-b995-a302b03383d7)

Traffic sign detection in STS dataset (a-c) Small-sized traffic sign detection (d) A large-sized traffic sign detection
