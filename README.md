# Steps overview :

1. video_frame_extact.py : read the video and extarct frame in every one second
2. custom_name_generartor : rename the files from extracted folder into custom name better for preprocessing and track ( optional step)
3. find_coordinates.py : allows user to generate custom mask and .txt file having coordinates to mask
4. custom_mask_generate.py: generate a dataset having custom mask using .txt file and the folder obatined after renaming or extraction .
5. mask_folder : generate a custom dataset of mask data from the .txt file from custom_mask_generate .py file
6. custom_pixel_find.py : calculate pixel distance between 2 selected file and save result in .txt file .
#   p o l e _ p i x e l _ d i s t a n c e  
 