# Climbing Related AI Model
A fine-tuned AI model to detect whether or not there is a link with climbing.  
  
## Install the project
To install the project, there is some requirements :  
- Python
- Nodejs

**Step 1** : Clone the repository  
**Step 2** : Install the node dependencies  
**Step 3** : Go in the Model directory and generate the model and the tokenizer.  
```bash
cd Model/  
python train.py
```  
**Step 4** : Go back to root directory and run the api.  
```bash
cd ..  
python app.py
```  