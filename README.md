# Fraud Detection Model using Isolation Forest  
This model implements fraud detection in the system. It uses the Isolation Forest algorithm to identify fraudulent activities based on user behavior. The model is trained on synthetic data generated using the faker library and can be used to predict fraud in new datasets.  

## Installation  
Clone this repository and install dependencies:  

git clone https://github.com/Samuel-ALX23/TrustID.git
cd fraud-detection
pip install -r requirements.txt

## Data Generation  
The dataset is generated using the Faker library.


# File contents
This file contains code that follows the following process 
1. Fist synthetic data is generated to train the unsuperviesd model
2. Then the model is trained on the data
3. Its performance is evaluated using the confusion matrix 

# Arguments
The model takes in the following arguments:
Number of times a user has been verified: num_verifications
Number of failed verification attempts: num_failed_verifications
Number of revoked credentials for a user: num_revocations
Number of unique DIDs the user has : num_dids
Number of times the user has changed their encryption keys: key_rotations