import pymupdf
import json

# Load configuration from config.json
with open("config.json", "r") as f:
    config = json.load(f)

doc = pymupdf.open(f'files/{config["pdf"]["input_file"]}')
number = config["pdf"]["page_number"]
page = doc[number]  # page number 0-based

# Extract replacements from config
disliked_list = [item["find"] for item in config["replacements"]]
better_list = [item["replace"] for item in config["replacements"]]

# search the text to be replaced
for index, disliked in enumerate(disliked_list):
    hits = page.search_for(disliked)
    # add redactions
    for rect in hits:
        rect.x1 += config["redaction"]["adjust_x1"]
        rect.y1 += config["redaction"]["adjust_y1"]  # make rectangle a bit taller

        page.add_redact_annot(rect,
        align=pymupdf.TEXT_ALIGN_CENTER)

    page.apply_redactions(images=pymupdf.PDF_REDACT_IMAGE_NONE)



    # add texts
    for rect in hits:
        rect.x1 += config["insertion"]["adjust_x1"]
        rect.y1 += config["insertion"]["adjust_y1"]
        
        # Parse alignment from config
        align_map = {
            "CENTER": pymupdf.TEXT_ALIGN_CENTER,
            "LEFT": pymupdf.TEXT_ALIGN_LEFT,
            "RIGHT": pymupdf.TEXT_ALIGN_RIGHT
        }
        align = align_map.get(config["insertion"]["align"], pymupdf.TEXT_ALIGN_CENTER)
        
        result = page.insert_textbox(
            rect,
            better_list[index],
            fontfile=f'fonts/{config["font"]["fontfile"]}',
            fontname=config["font"]["fontname"],
            fontsize=config["font"]["fontsize"],
            color=config["font"]["color"],
            align=align,
        )
        print(f"Inserted text '{better_list[index]}' in rectangle {rect}, result={result}")

doc.save(f"files/{config['pdf']['output_file']}", garbage=3, deflate=True)
