'''
create a custome rename generator python program that works on following algrothim : 

1. read files from the input_folder 
2. genreate a folder named as output_folder
3. create a unique name , file_name = custom_input + current_date_and_time + counter
4. copy the file from the input , rename the file , and paste in output_folder in the same extension and formate 
5. save  the original name change to final name along with location in csv also print it 
6. print the output path loaction , and completed message 




'''


import os
import shutil
from datetime import datetime
import csv


def generate_unique_filename(custom_input, counter, original_filename):
    current_time = datetime.now().strftime("%Y%m%d%H%M%S")
    filename, extension = os.path.splitext(original_filename)
    new_filename = f"{custom_input}_{current_time}_{counter}{extension}"
    return new_filename


def rename_files(input_folder, output_folder, custom_input, csv_filename):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    counter = 1
    with open(csv_filename, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(['Original Name', 'Final Name',
                            'Original Location', 'Final Location'])

        for filename in os.listdir(input_folder):
            input_filepath = os.path.join(input_folder, filename)
            if os.path.isfile(input_filepath):
                new_filename = generate_unique_filename(
                    custom_input, counter, filename)
                output_filepath = os.path.join(output_folder, new_filename)
                shutil.copyfile(input_filepath, output_filepath)
                print(f"Renamed: {filename} -> {new_filename}")
                csv_writer.writerow(
                    [filename, new_filename, input_filepath, output_filepath])
                counter += 1

    print(f"All files renamed and copied to {output_folder}")
    print(f"CSV log saved to {csv_filename}")


'''

Generate without the csv file
'''


# input_folder = "mask_input"
# output_folder = "output_rename"
# custom_input = "rename"
# csv_filename = "rename_log.csv"

# rename_files(input_folder, output_folder, custom_input, csv_filename)


# import os
# import shutil
# from datetime import datetime


# def generate_unique_filename(custom_input, counter, original_filename):
#     current_time = datetime.now().strftime("%Y%m%d%H%M%S")
#     filename, extension = os.path.splitext(original_filename)
#     new_filename = f"{custom_input}_{current_time}_{counter}{extension}"
#     return new_filename


# def rename_files(input_folder, output_folder, custom_input):
#     if not os.path.exists(output_folder):
#         os.makedirs(output_folder)

#     counter = 0
#     for filename in os.listdir(input_folder):
#         input_filepath = os.path.join(input_folder, filename)
#         if os.path.isfile(input_filepath):
#             new_filename = generate_unique_filename(
#                 custom_input, counter, filename)
#             output_filepath = os.path.join(output_folder, new_filename)
#             shutil.copyfile(input_filepath, output_filepath)
#             print(f"Renamed: {filename} -> {new_filename}")
#             counter += 1

#     print(f"All files renamed and copied to {output_folder}")


# # Example usage:
# input_folder = "mask_input"
# output_folder = "output_rename"
# custom_input = "suraj"

# rename_files(input_folder, output_folder, custom_input)
