# YOLO-FUZZ
YOLO-FUZZ is a specialized object detection framework designed for real-world traffic scenarios where signs occupy only 1–2% of the image resolution. This repository contains the implementation of:

- **Modified YOLO Architecture:** Optimized to extract and comprehend small-scale features from vehicle dash-cam perspectives.

- **Fuzzy-Based Anchor Selection:** A novel method that uses size distribution variance to address long-tailed dataset challenges.

- **Benchmarked Results:** High-performance detection validated on the German (GTSDB) and Swedish (STSD) traffic sign datasets.

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

# Code Hierarchy

**anchors** folder contains the matlab script file for anchor box generation

**data** folder holds all dataset related files. Use gtsdb.yaml to train the model on German Traffic Sign Dataset.

**model** folder includes the YOLO-FUZZ architecture model

**utils** folder has all the other required function files in order to run train.py and detect.py

# Usage steps

You may use this code for small traffic sign detection by following these simple steps.

1- Estimate anchors using anchorboxSortScale_fuzzy.m file

2- Copy test and train images(with .jpg file extension) in datasets/gtsdb_Test and datasets/gtsdb_Train respectively

3- Use dataset_yaml.py to generate and save gtsdb.yaml file in **Data** folder. Generate two different files for train and test set. 

4- Clone the repository

      git clone https://github.com/Hafsa1918/YOLO-FUZZ.git
      cd YOLO-FUZZ

5-  Install dependencies stated in [requirements.txt](https://github.com/Hafsa1918/YOLO-FUZZ/blob/main/requirements.txt)

      pip install -r requirements.txt 

6- Use [train.py](https://github.com/Hafsa1918/YOLO-FUZZ/blob/main/train.py) to train your network. 

      python train.py --img 416 --data gtsdb.yaml --weights yolov5s.pt --noautoanchor 

6- Use [detect.py](https://github.com/Hafsa1918/YOLO-FUZZ/blob/main/detect.py) to test the trained network with test images.

      python detect.py --data data/gtsdb_test.yaml --source ../datasets/gtsdb_Test
      
## Results

# Test results of the proposed algorithm on German Traffic Sign Dataset Benchmark
![amanu8](https://github.com/ha007-aman/SmallObjectDetection/assets/73087518/480464da-9626-47aa-b4b3-7fa2e479ae8b)

Traffic sign detection in GTSDB dataset (a) Traffic sign size variation in an image (b \& d) Small traffic sign detection (c) A larger traffic sign recognition

# Test results of the proposed algorithm on Swedish Traffic Sign Dataset 
![amanu9](https://github.com/ha007-aman/SmallObjectDetection/assets/73087518/66cc4035-8c93-49fc-b995-a302b03383d7)

Traffic sign detection in STS dataset (a-c) Small-sized traffic sign detection (d) A large-sized traffic sign detection

# Citation

If you use this code or the YOLO-FUZZ architecture in your research, please cite our PeerJ paper: [DOI we will shared soon]

# License

This project is open-access and available under the gpl-3.0 License
