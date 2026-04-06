import torch
import torch.nn as nn
from torchvision import models, transforms
from .calorie_db import CLASS_NAMES


def load_trained_model(model_path="app/model.pth"):
    net = models.mobilenet_v2(weights=None)
    num_ftrs = net.classifier[1].in_features
    net.classifier[1] = nn.Linear(num_ftrs, 10)
    net.load_state_dict(torch.load(model_path, map_location=torch.device('cpu')))
    net.eval()
    return net



preprocess = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(
        mean=[0.485, 0.456, 0.406],
        std=[0.229, 0.224, 0.225]
    )
])

model = load_trained_model("app/model.pth")

def predict(image):

    if image.mode != "RGB":
        image = image.convert("RGB")

    input_tensor = preprocess(image)

    input_batch = input_tensor.unsqueeze(0)

    with torch.no_grad():
        output = model(input_batch)

        probabilities = torch.nn.functional.softmax(output[0], dim=0)

    confidence, index = torch.max(probabilities, 0)

    food_name = CLASS_NAMES[index]
    confidence_score = confidence.item() * 100

    return food_name, confidence_score

