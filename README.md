# YOLO-FUZZ
YOLO-FUZZ is a specialized object detection framework designed for real-world traffic scenarios where signs occupy only 1–2% of the image resolution. This repository contains the implementation of:

- **Modified YOLO Architecture:** Optimized to extract and comprehend small-scale features from vehicle dash-cam perspectives.

- **Fuzzy-Based Anchor Selection:** A novel method that uses size distribution variance to address long-tailed dataset challenges.

- **Benchmarked Results:** High-performance detection validated on the German (GTSDB) and Swedish (STSD) traffic sign datasets.

This work is adaption from [Ultralytics/yolov5](https://github.com/ultralytics/yolov5), modifying standard YOLOv5 network for optimized detection of small traffic signs in complex road scenes.

## Project Objective / Problem Statement

YOLO-FUZZ is developed for **small traffic sign detection in real-world road scenes**, especially from vehicle dash-cam viewpoints where traffic signs often occupy only **1–2% of the full image resolution**. In such cases, standard YOLO-based detectors may struggle because very small objects are weakly represented in deeper feature maps, and conventional anchor selection methods do not adequately model the highly imbalanced size distribution of traffic signs.

To address this problem, YOLO-FUZZ introduces two main contributions:  
1. **a modified YOLO architecture** designed to better preserve and learn small-scale visual features, and  
2. **a fuzzy-based anchor selection strategy** that accounts for size-distribution variance and long-tailed object statistics.  

These modifications improve the detector’s ability to localize and recognize small traffic signs in complex road environments.

## Author
[Hafsa Amanullah] - 🌐 [Github](https://github.com/Hafsa1918) - 🌐 [LinkedIn Profile](https://www.linkedin.com/in/hafsa-amanullah) - [Google scholar](https://scholar.google.com/citations?user=up19UMQAAAAJ&hl=en) - [Email - hafsa@neduet.edu.pk]

## Collaborators
[Prof. Dr. Min Young Kim] - 🌐 [Google scholar](https://scholar.google.com.pk/citations?user=Xhawz8EAAAAJ&hl=en)

[Dr. Yawar Rehman] - 🌐 [Github](https://github.com/YawarGuguma) - 🌐 [LinkedIn Profile](https://www.linkedin.com/in/yawar-rehman-820118b/) - [Google scholar](https://scholar.google.com/citations?hl=en&user=VclpjuIAAAAJ)

## Dataset Details

The proposed method is evaluated on two publicly available traffic sign datasets:

### 1. German Traffic Sign Detection Benchmark (GTSDB)
- **Full name:** German Traffic Sign Detection Benchmark (GTSDB)  
- **Official source:** [GTSDB](https://benchmark.ini.rub.de/gtsdb_dataset.html)
- **Dataset type:** Traffic sign detection  
- **Number of images:** 900 images  
- **Official split:** 600 training images and 300 evaluation images  
- **Number of classes/categories:** 43 traffic sign classes, grouped into major detection categories such as prohibitory, mandatory, and danger signs  
- **Image format in the original release:** `.ppm`  
- **Annotation format in the original release:** `.csv` files containing filename, ROI coordinates, and class ID  
- **Usage in this repository:** Images are converted to `.jpg` format when needed, and annotations are prepared for YOLO-based training and evaluation  

### 2. Swedish Traffic Signs Dataset (STSD)
- **Full name:** Swedish Traffic Signs Dataset (STSD)  
- **Official source:** [STS dataset] (https://www.cvl.isy.liu.se/research/datasets/traffic-signs-dataset/) 
- **Dataset type:** Traffic sign detection  
- **Number of images:** more than 20,000 images  
- **Labeled subset:** approximately 20% labeled  
- **Number of traffic signs:** 3,488 annotated traffic signs  
- **Road coverage:** collected from more than 350 km of Swedish roads  
- **Number of classes:** 3  

### Notes on Data Preparation
- All images should be stored in **`.jpg`** format before training.  
- For **GTSDB**, the original `.ppm` images may need to be converted to `.jpg`.  
- No additional preprocessing is required beyond annotation formatting and dataset organization for training/testing.  
- Dataset YAML files are generated to define image paths, class names, and split configuration for YOLO-FUZZ training.

## Requirements / Environment Details

This repository is based on **Ultralytics YOLOv5** and requires a standard PyTorch-based deep learning environment.

### Minimum software requirements
- **Python:** 3.8 or later  
- **PyTorch:** 1.8.0 or later  
- **Torchvision:** 0.9.0 or later  

### Main Python dependencies
The core dependencies are listed in `requirements.txt`, including:
- `numpy`
- `opencv-python`
- `matplotlib`
- `Pillow`
- `PyYAML`
- `scipy`
- `tqdm`
- `pandas`
- `seaborn`
- `thop`

### Tested environment

The training and testing of models is conducted on Google CoLab using Tesla T4 GPU having 16GB RAM.

### Installation
Install all required packages using:

      pip install -r requirements.txt

## Methodology

**Fuzzy Anchor Selection**

Unlike standard K-means clustering for anchors, our Fuzzy method considers the variance in size distribution. This allows the network to adapt to the inherent imbalance (long-tail) of traffic sign occurrences in different geographical datasets.

**YOLO-FUZZ**

Modified YOLO layers and heads specifically tuned to detect small traffic signs in a complex road scenes. 

## Code Hierarchy

**anchors** folder contains the matlab script file for anchor box generation

**data** folder holds all dataset related files. Use gtsdb.yaml to train the model on German Traffic Sign Dataset.

**model** folder includes the YOLO-FUZZ architecture model

**run** folder stores the trained model weights and test dataset results

**utils** folder has all the other required function files in order to run train.py and detect.py

### Usage steps

You may use this code for small traffic sign detection by following these simple steps. Please note same steps will be used for any other traffic sign dataset as well, for tutorial purpose, german dataset is quoted here.

1- Estimate anchors using anchorboxSortScale_fuzzy.m file

2- Copy test and train images(with .jpg file extension) in datasets/gtsdb_Test and datasets/gtsdb_Train respectively

3- Use dataset_yaml.py to generate .yaml file for train (gtsdb.yaml) and test(gtsdb_test.yaml) images. Save both the files in **Data** folder. 

4- Clone the repository

      git clone https://github.com/Hafsa1918/YOLO-FUZZ.git
      cd YOLO-FUZZ

5-  Install dependencies stated in [requirements.txt](https://github.com/Hafsa1918/YOLO-FUZZ/blob/main/requirements.txt)

      pip install -r requirements.txt 

#### Training

1- Use gtsdb.yaml (generted using train dataset) to train the network, using [train.py](https://github.com/Hafsa1918/YOLO-FUZZ/blob/main/train.py). 

      python train.py --img 416 --data gtsdb.yaml --weights yolov5s.pt --noautoanchor 

2- The trained model weights will be saved to ./run/train/exp/ path.

#### Testing

1- Use [detect.py](https://github.com/Hafsa1918/YOLO-FUZZ/blob/main/detect.py) to test the trained network with test images. Add the path of test-images, and true test results in terms of .yaml file to calculate AP for each class.

      python detect.py --data data/gtsdb_test.yaml --source ../datasets/gtsdb_Test

2- The test results will be saved to ./runs/detect/ path.
      
## Results

### Performance Comparison

| Method Used | mAP | Recall | Precision | FPS |
| :--- | :---: | :---: | :---: | :---: |
| **SegU-Net** | - | 89% | 95% | - |
| **YOLOv5** | - | 89% | 93% | - |
| **YOLOv5s-A2** | 94% | 90% | - | 105 |
| **YOLOF-F** | 74% | - | - | 32 |
| **YOLO-FUZZ** | 83% | 87% | 65% | 145 |
------------------------------

### Test results of the proposed algorithm on German Traffic Sign Dataset Benchmark
![amanu8](https://github.com/ha007-aman/SmallObjectDetection/assets/73087518/480464da-9626-47aa-b4b3-7fa2e479ae8b)

Traffic sign detection in GTSDB dataset (a) Traffic sign size variation in an image (b \& d) Small traffic sign detection (c) A larger traffic sign recognition

### Test results of the proposed algorithm on Swedish Traffic Sign Dataset 
![amanu9](https://github.com/ha007-aman/SmallObjectDetection/assets/73087518/66cc4035-8c93-49fc-b995-a302b03383d7)

Traffic sign detection in STS dataset (a-c) Small-sized traffic sign detection (d) A large-sized traffic sign detection

## Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

Please read our [CONTRIBUTIONs.md](CONNTRIBUTIONS.md) for details on our code of conduct and the process for submitting pull requests.

## Citation

If you use this code or the YOLO-FUZZ architecture in your research, please cite our PeerJ paper: [Citations will be updated after publication]

## License

This project is open-access and available under the gpl-3.0 License
