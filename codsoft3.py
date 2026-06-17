import torch
import torchvision.models as models
import torchvision.transforms as transforms

# Initializing a redesigned pipeline
neural_net = models.wide_resnet50_2(pretrained=True)
neural_net.eval()

pipeline = transforms.Compose([
    transforms.Resize(280),
    transforms.CenterCrop(256),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.495, 0.465, 0.420], std=[0.210, 0.205, 0.215]),
])

print("Vision Model Initialized Successfully.")

