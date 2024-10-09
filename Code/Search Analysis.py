import os
import sys
import subprocess
import pandas as pd

from scrape_and_process import (
    searchanalysis_makemodel_depre_motorist,
    searchanalysis_makemodel_depre_sgcar,
    write_to_csv_motorist,
    write_to_csv_sgcar,
    create_top_bottom_slides
)

from pptx import Presentation

def main(working_directory):  # Receive the working directory as a parameter
    print("Starting main function.")

    # Use the working directory for file operations
    script_dir = working_directory

    with open(os.path.join(working_directory, "urls.txt"), "r") as file:
        urls = [line.strip() for line in file.readlines()]

    motorist_urls = urls[:4]
    sgcar_urls = urls[4:]

    motorist_top3_dfs = []
    motorist_bottom3_dfs = []
    sgcar_top3_dfs = []
    sgcar_bottom3_dfs = []

    for url in motorist_urls:
        print(f"Processing URL: {url}")
        result = searchanalysis_makemodel_depre_motorist(url)
        make_model = url.split('keywords=')[1].split('&')[0].replace('+', ' ')
        output_filename = os.path.join(script_dir, f"Motorist_{make_model}.csv")
        write_to_csv_motorist(result, output_filename, script_dir)
        print(f"Data written to CSV: {output_filename}")
        df = pd.read_csv(output_filename)
        top3 = df.sort_values(by='Depreciation').head(3)
        bottom3 = df.sort_values(by='Depreciation').tail(3)
        motorist_top3_dfs.append((top3, f"Top 3 {make_model} on Motorist"))
        motorist_bottom3_dfs.append((bottom3, f"Bottom 3 {make_model} on Motorist"))

    for url in sgcar_urls:
        print(f"Processing URL: {url}")
        result = searchanalysis_makemodel_depre_sgcar(url)
        make_model = url.split('MOD=')[1].split('&')[0].replace('+', ' ')
        output_filename = os.path.join(script_dir, f"SGCM_{make_model}.csv")
        write_to_csv_sgcar(result, output_filename, script_dir)
        print(f"Data written to CSV: {output_filename}")
        df = pd.read_csv(output_filename)
        top3 = df.sort_values(by='Depreciation').head(3)
        bottom3 = df.sort_values(by='Depreciation').tail(3)
        sgcar_top3_dfs.append((top3, f"Top 3 {make_model} Listings on SGCM"))
        sgcar_bottom3_dfs.append((bottom3, f"Bottom 3 {make_model} Listings on SGCM"))

    prs = Presentation()
    create_top_bottom_slides(prs, motorist_top3_dfs, motorist_bottom3_dfs)
    create_top_bottom_slides(prs, sgcar_top3_dfs, sgcar_bottom3_dfs)
    pptx_filename = os.path.join(script_dir, "top_bottom_listings.pptx")
    prs.save(pptx_filename)
    print(f"PowerPoint presentation saved successfully: {pptx_filename}")

if __name__ == "__main__":
    main(sys.argv[1]) 
