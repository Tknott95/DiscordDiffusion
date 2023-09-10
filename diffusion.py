# from diffusers import StableDiffusionXLPipeline
from diffusers import StableDiffusionPipeline, EulerDiscreteScheduler

import torch

from colors import clr

from PIL import Image 
import PIL 

model_id = "stabilityai/stable-diffusion-2"

class Diffusion():
    # pipe = StableDiffusionXLPipeline.from_pretrained(
    # "stabilityai/stable-diffusion-xl-base-1.0",
    # torch_dtype=torch.float16, 
    # variant="fp16",
    # use_safetensors=True,
    # add_watermarker=False
    # )
    scheduler = EulerDiscreteScheduler.from_pretrained(model_id, subfolder="scheduler")
    pipe = StableDiffusionPipeline.from_pretrained(
      model_id, 
      scheduler=scheduler, 
      torch_dtype=torch.float16,
      add_watermarker=False)
    pipe.to("cuda:0")

    # _input = input(clr.bar + "\n  Type what kind of image you would like\n:  " + clr.clear)

    def run(self, file_name, _input):
        # prompt = "Astronaut in a jungle, cold color palette, muted colors, detailed, 8k"
        image = self.pipe(prompt=_input).images[0]

        image_to_send = image.save(f'{file_name}.jpg')
        print(clr.cyan + f'\n  {file_name}.jpg MADE and SAVED \n' + clr.clear)

        return image_to_send
