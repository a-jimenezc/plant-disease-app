# Plant Disease Detector

English | [Español](README_es.md)

## Project Summary

* This is the repo for a web application that allows users to upload a photograph of a plant's leaves and, based on this, detect the type of leaf and any diseases present.
* For this purpose, the object detection algorithm [**YOLOv7**](https://arxiv.org/abs/2207.02696) and its open-source implementation by [Wong Kin Yiu](https://github.com/WongKinYiu/yolov7) were used.
* The algorithm is implemented in PyTorch, but inference is done using the **ONNX** format. For details on the training process, visit: [yolov7_plantdoc](https://github.com/a-jimenezc/yolov7_plantdoc).
* The database used is: [PlantDoc: A Dataset for Visual Plant Disease Detection](https://github.com/pratikkayal/PlantDoc-Dataset). It contains **13 species** and up to **17 different diseases**.
* The website was deployed using **Docker** and Google Cloud Platform's **serverless** service: Cloud Run.

## Requirements

* **Python Version:** 3.9
* **Libraries:** numpy, pandas, open-cv, dash, ONNX runtime.
* **Installation:** requirements.txt

## Website

Here is the link to the website, hosted by Google Cloud:

[plant-disease.dsapp.me](https://plant-disease.dsapp.me/)

<img src="images/app.png" alt="Screenshot" width="500"/> 

## Database: Plantdoc
* There are 28 different classes, distributed as follows.
  
  <img src="images/distr.png" alt="Distribution" width="500"/>

* The original database is in English, so it was necessary to translate it to Spanish. Below are the translations used:

  <img src="images/trad.png" alt="Translations" width="500"/>

## Next Steps

It is necessary to collect data from different species and relevant diseases in Bolivia to ensure greater utility of the tool.

It is also necessary to apply data augmentation techniques to improve the model's performance.

## License 

GNU Affero General Public License v3.0

## Author

Antonio Jimenez Caballero

## Contact

[LinkedIn](https://www.linkedin.com/in/antonio-jimnzc/)
