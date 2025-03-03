import requests
from bs4 import BeautifulSoup
import pandas as pd  # New dependency
import re

def extract_netflix_data(input_file, output_file):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }

    # Create a list to store all entries
    data = []
    
    with open(input_file, 'r') as infile:
        for url in infile:
            url = url.strip()
            if not url:
                continue

            try:
                n_id = url.split('/')[-1].split('?')[0]
                if not n_id.isdigit():
                    print(f"Skipping invalid URL: {url}")
                    continue

                response = requests.get(url, headers=headers)
                if response.status_code != 200:
                    print(f"Failed to fetch {url} - Status code: {response.status_code}")
                    continue

                soup = BeautifulSoup(response.content, 'html.parser')

                # --- Existing extraction logic (unchanged) ---
                title = soup.find('h1', class_='title-title')
                title = title.get_text(strip=True) if title else 'N/A'

                # Main Genre
                main_genre_element = soup.find('a', class_='title-info-metadata-item item-genre')
                main_genre = main_genre_element.get_text(strip=True).strip('= $0') if main_genre_element else 'N/A'

                # Sub Genres
                sub_genres_elements = soup.select('div.more-details-cell.cell-genres a.more-details-item.item-genres')
                sub_genres = ', '.join([g.get_text(strip=True).replace('Movies', '').strip() 
                                      for g in sub_genres_elements]) if sub_genres_elements else 'N/A'

                # Release Year
                year_element = soup.find('span', class_='title-info-metadata-item item-year')
                release_year = year_element.get_text(strip=True) if year_element else 'N/A'

                # Maturity Rating
                maturity = soup.find('span', class_='maturity-number')
                maturity = maturity.get_text(strip=True) if maturity else 'N/A'

                # Audio Languages
                audio_elements = soup.select('div.more-details-cell.cell-audio span.more-details-item.item-audio')
                languages = set()
                for element in audio_elements:
                    text = element.get_text(strip=True)
                    cleaned_text = re.sub(r'[^a-zA-Z\s\-\[\]]', '', text).strip()
                    if cleaned_text:
                        languages.add(cleaned_text)
                audio = ', '.join(languages) if languages else 'N/A'

                # Recommendations
                recommendations = set()
                for link in soup.find_all('a', href=True):
                    href = link['href']
                    if '/title/' in href:
                        parts = href.split('/')
                        rec_id = parts[parts.index('title') + 1].split('?')[0]
                        if rec_id.isdigit() and rec_id != n_id:
                            recommendations.add(rec_id)
                recommendations = ', '.join(recommendations) if recommendations else 'N/A'

                # Add to data list
                data.append({
                    'N_id': n_id,
                    'Title': title,
                    'Main Genre': main_genre,
                    'Sub Genres': sub_genres,
                    'Release Year': release_year,
                    'Maturity Rating': maturity,
                    'Original Audio': audio,
                    'Recommendations': recommendations
                })

                print(f"Processed: {title}")

            except Exception as e:
                print(f"Error processing {url}: {str(e)}")
                continue

    # Create DataFrame and save to Excel
    df = pd.DataFrame(data)
    df.to_excel(output_file, index=False, sheet_name='Netflix Data')
    print(f"\nData saved to {output_file} with {len(df)} entries")

if __name__ == "__main__":
    input_file = "links.txt"
    output_file = "netflix_data.xlsx"  # Changed to .xlsx
    extract_netflix_data(input_file, output_file)



#this is used to generate the excel sheet with ids, titles, recommendations, etc. 