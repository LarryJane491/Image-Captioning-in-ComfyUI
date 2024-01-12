This is a custom node pack for ComfyUI.
The LoRA Caption custom nodes, just like their name suggests, allow you to caption images so they are ready for LoRA training. You can find them by right-clicking and looking for the LJRE category, or you can double-click on an empty space and search for "caption".
They were made to work with WD14 Tagger.



Here is the workflow:
![Capture](https://github.com/LarryJane491/Image-Captioning-in-ComfyUI/assets/156431112/89a33c73-32c2-470d-9494-89349ccd76ee)



Simple but elegant x)
This workflow shows both nodes in this pack: LoRA Caption Load and LoRA Caption Save.

The other custom nodes used here are:

WD 1.4 Tagger (mandatory)

Jjk custom nodes (optional)


The Tagger is mandatory as this is the one that actually does the captioning. You also have to download a model, check out the github of that node for more information. My custom nodes are built as a complement for this one.

Jjk is optional, it just lets you see that the software does extract the names of the files.



Here is how it works:

Gather the images for your LoRA database, in a single folder. Make sure the images are all in png (this requirement will be changed in a new version).

Copy that folder’s path and write it down in the widget of the Load node.

Plug the image output of the Load node into the Tagger, and the other two outputs in the inputs of the Save node. Plug the Tagger output into the Save node too.

And that’s it! Just launch the workflow now.



The Load node has two jobs: feed the images to the tagger and get the names of every image file in that folder. The name list and the captions are then fed to the Save node, which creates text files with the image name as its own name and the description of the image as its content (in other words: it creates the caption files).

Once the files are done, your database is ready for LoRA training! The next big step is LoRa Training, which is possible from withing ComfyUI with another custom node of my own creation.





Notes:

The WD 1.4 Tagger is for anime images, so I don’t know how good it is for realistic images. I don’t see why it wouldn’t work though! At least for anime it is extremely impressive imo.

If the text files already exist, Comfy will throw the Out of Range error. I could easily fix that, but I don’t see the point: just make sure the text files don’t exist already. If you want to change them, just delete them and relaunch the workflow.

The widget lets you write a common prefix. It’s useful for creating trigger words for your LoRA. If you use the widget, make sure it ends with a comma. Again, it’s something I could easily fix, but I'm a little lazy x).

This is part of THE LAB ULTIMATE, my personal workflow. I will share it… but I’ll wait for a while because I want to include much more stuff in it before making it public.



I would like to thank the creators of Inspire Pack and YMC Suite Node, as my functions are heavily inspired by theirs. In fact, I had a workflow working with them, without my custom nodes at all. My project is just a rewrite of some of their functions, as a way to train myself for making my own nodes.
