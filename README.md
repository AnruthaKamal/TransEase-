# TransEase: English to Hindi Translation Application

TransEase is a simple yet powerful English to Hindi translation application powered by a fine-tuned pretrained model called MarianMT.

## Dataset
TransEase utilizes the cfilt/iitb-english-hindi dataset available on Hugging Face for training and fine-tuning the translation model.

## Model Used
TransEase utilizes the MarianMT model, which has been fine-tuned on a custom dataset to enhance its performance specifically for English to Hindi translation tasks. This fine-tuning process ensures that the model is optimized to provide accurate and contextually relevant translations for the target language. The encoder-decoder architecture of the MarianMT model enables it to effectively capture the nuances of language translation, resulting in high-quality outputs for users.
## Training Loss

![WhatsApp Image 2024-06-03 at 21 40 57_e8e63e22](https://github.com/AnruthaKamal/TransEase-/assets/107014168/2d1361a8-a267-49ac-937f-3830bd0d1321)
The image above shows the training loss curve monitored during the training process.This curve provides insights into the convergence of the training process and the performance of the model over time.

## Application Demo and Screenshots 

![image](https://github.com/AnruthaKamal/TransEase-/assets/107014168/6d15a636-ce0c-4075-9488-5e00721efeaa)

## How to Run the Application

To run the TransEase application on your local machine, follow these steps:

1. **Clone the Repository**: Clone the TransEase repository to your local machine.

2. **Install Dependencies**: Ensure that you have all the required dependencies installed. You can install them using the following command: `pip install -r requirements.txt`

3. **Navigate to the Directory**: Use the `cd` command to navigate to the directory where the Streamlit file is located.

4. **Run the Streamlit App**: Execute the following command to run the Streamlit app : `streamlit run app.py`
