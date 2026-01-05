import torch
import torch.nn as nn
from preprocess_url import preprocess_url

class PhishingModel(nn.Module):
    def __init__(self):
        super(PhishingModel, self).__init__()
        self.net = nn.Sequential(
            nn.Linear(20, 32),
            nn.ReLU(),
            nn.Linear(32, 16),
            nn.ReLU(),
            nn.Linear(16, 2)
        )

    def forward(self, x):
        return self.net(x)

def load_model(path):
    model = PhishingModel()
    model.load_state_dict(torch.load(path, map_location=torch.device('cpu')))
    model.eval()
    return model

def predict_url(model, url):
    input_tensor = preprocess_url(url).unsqueeze(0)
    with torch.no_grad():
        output = model(input_tensor)
        probabilities = torch.softmax(output, dim=1)
        predicted_class = torch.argmax(probabilities, dim=1).item()
        confidence = probabilities[0][predicted_class].item()
    result = "Phishing" if predicted_class == 1 else "Legitimate"
    return result, round(confidence * 100, 2)

def get_explanation(result, url):
    if result == "Phishing":
        explanation = "This URL has characteristics often found in phishing links, like obfuscated domain or suspicious patterns."
        suggestion = "⚠️ Avoid clicking this link. Do not enter personal information. Verify the URL manually."
    else:
        explanation = "This URL appears safe based on the model’s checks."
        suggestion = "✅ Still, be cautious before entering sensitive information."
    return explanation, suggestion
