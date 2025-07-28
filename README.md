# Bank Note Authentication using Machine Learning

## Overview

This Python project implements a machine learning-based system to authenticate banknotes. It uses a preprocessed dataset containing statistical features extracted from genuine and forged currency notes. The system is trained using supervised learning algorithms to classify whether a banknote is real or fake.

## Prerequisites

- Python 3.x  
- Pandas  
- NumPy  
- Scikit-learn  
- Flask (optional, for API deployment)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/your-username/bank-note-authentication.git
```
2. Install the required libraries:
```bash
pip install scikit-learn
pip install numpy
pip install keras
```

3. Download the pre-trained Harcascade XML file (haarcascade_russian_plate_number.xml) and place it in the model directory.

## Dataset
1. data_set:
	bank_note_data.txt

## Project Structure
```
bank-note-authentication/
│
├── model/
│   └── bank_note_authentication_model.keras           # Trained ML model
│
├── bank_note_authentication_model.keras                 # Script to train and save the model
├── bank_note_authentication.ipynb                    # Script to test predictions
├── bank_note_data.txt             # Dataset file
├── README.md                      # Project documentation
└── LICENSE                        # Project license
```
## Additional Notes
You can experiment with other algorithms (e.g., SVM, Random Forest, XGBoost).

Feature scaling or PCA can improve model performance.

Extend the Flask API with more routes like /train or /batch_predict.

#License
This project is licensed under the MIT License.

#Contribution
Contributions are welcome! Feel free to open issues or submit pull requests for improvements or bug fixes.