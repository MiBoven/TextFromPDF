from os import path, makedirs
import os
import fitz     # PyMuPDF

def extract_images_from_pdf(pdf_file_path, output_folder):
    if not path.exists(pdf_file_path):
        print("File does not exist.")
        return []

    # create folder if not exists
    makedirs(output_folder, exist_ok=True)

    extracted_images = []
    pdf_file = fitz.open(pdf_file_path)

    for page_number, page in enumerate(pdf_file):
        # iteration over every page
        # and put it in a image list
        image_list = page.get_images(full=True)
        for image_index, img in enumerate(image_list):
            xref = img[0]     # reference number of the current image
            base_image = pdf_file.extract_image(xref)
            image_bytes = base_image["image"]

            # save the image in a file
            image_file_name = path.join(image_folder, f"page_{page_number + 1}_image_{image_index + 1}.png")
            with open(image_file_name, "wb") as image_file:
                image_file.write(image_bytes)

            # Infos to the extracted images
            extracted_images.append({
                "page_number": page_number + 1,
                "image_index": image_index + 1,
                "image_file_name": image_file_name,
            })

    return extracted_images

#pdf_file_path = "files/spin.pdf"
pdf_file_path = "files/BA_Michel_Bovender_2015.pdf"

image_folder = "images"

extracted_images_info = extract_images_from_pdf(pdf_file_path, image_folder)

for info in extracted_images_info:
    print(info)

print(f"{len(extracted_images_info)} Bilder extrahiert und im Unterordner {image_folder} gespeichert." )
