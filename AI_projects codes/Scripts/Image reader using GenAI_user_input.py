from IPython.display import display, Audio
import google.generativeai as genai
from google.colab import files
from PIL import Image
import matplotlib.pyplot as plt

genai.configure(api_key=" ")
model = genai.GenerativeModel("gemini-2.5-flash")

uploaded = files.upload()
image_path = list(uploaded.keys())[0]
image = Image.open(image_path)

while True:
    q = input("\nAsk something about the image (or type 'exit'): ")
    if q.lower() == "exit":
        break

    ans = model.generate_content([image, q])
    print("\nAnswer:\n", ans.text)
for i in response.text:
  if i.isalpha()==True or i==" " or i=="\n":
    response1=response1+i
response=response1
print(response)