import torch
import torchvision

# Load the pre-trained model
model = torchvision.models.resnet18(weights=torchvision.models.resnet.ResNet18_Weights.IMAGENET1K_V1)

# Set the model to evaluation mode
model.eval()

# Load an image and preprocess it
image = torchvision.io.read_image("image.jpg")
image = torchvision.transforms.functional.resize(image, (224, 224), antialias=True)
image = image.float()
image = torchvision.transforms.functional.normalize(image, [0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
image = image.unsqueeze(0)

# Make a prediction
with torch.no_grad():
    output = model(image)

# Get the predicted class label
_, predicted = torch.max(output.data, 1)
import json
import urllib.request

# Load the class labels for the ImageNet dataset
with urllib.request.urlopen("https://raw.githubusercontent.com/anishathalye/imagenet-simple-labels/master/imagenet-simple-labels.json") as url:
    classes = json.loads(url.read().decode())

# Print the predicted class name
print(classes[predicted.item()])
print(predicted)

