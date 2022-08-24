import matplotlib.pyplot as plt
from utils.configuration import Configuration
from utils.data_generator import DataGenerator
from utils.model import Mask2FaceModel

def predict(img_path):
    configuration = Configuration()
    dg = DataGenerator(configuration)

    model = Mask2FaceModel.load_model('models/model.h5')
    generated_output = model.predict(img_path)
    
    plt.imshow(generated_output)
    plt.axis("off")
    plt.savefig("tmp//mask_remove.png")
