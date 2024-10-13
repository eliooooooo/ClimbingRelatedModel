# Climbing Related AI Model
A fine-tuned AI model to detect whether or not there is a link with climbing.  
  
## Install the project
To install the project, there is some requirements :  
- Python
- Nodejs

**Step 1** : Clone the repository  
**Step 2** : Install node dependencies  
```bash
npm install
```
**Step 3** : Install python dependencies
```bash
pip install -r requirements.txt
```
**Step 4** : Go in the Model directory and generate the model and the tokenizer.  
```bash
cd Model/  
python train.py
```  
**Step 5** : Go back to root directory and run the api.  
```bash
cd ..  
python app.py
```  