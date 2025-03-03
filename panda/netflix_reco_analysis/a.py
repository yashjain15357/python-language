import requests
from bs4 import BeautifulSoup
import time
import re

def find_netflix_links(input_file='links.txt'):
    # 📁 Read existing links first
    try:
        with open(input_file, 'r') as f:
            existing_links = set(f.read().splitlines())
    except FileNotFoundError:
        existing_links = set()

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }

    visited = set()
    base_url = 'https://www.netflix.com'
    session = requests.Session()
    total_processed = 0

    print(f"🚀 Starting crawler with {len(existing_links)} initial links!")

    while True:
        current_batch = list(existing_links - visited)
        batch_size = len(current_batch)
        
        if not batch_size:
            print("🏁 No more links to process!")
            break

        print(f"\n📦 Processing batch of {batch_size} links (Total discovered: {len(existing_links)})")

        for idx, url in enumerate(current_batch, 1):
            if url in visited:
                continue

            total_processed += 1
            print(f"\n🔍 [{total_processed} processed] Processing ({idx}/{batch_size}): {url}")
            visited.add(url)

            try:
                # ⏳ Respectful delay between requests
                time.sleep(1.5)
                
                response = session.get(url, headers=headers, timeout=15)
                if response.status_code != 200:
                    print(f"⚠️  Status {response.status_code} for {url}")
                    continue

                soup = BeautifulSoup(response.text, 'html.parser')

                # 🎯 Find title links pattern
                new_links = 0
                for link in soup.find_all('a', href=re.compile(r'/title/\d+$')):
                    full_url = base_url + link['href']

                    if full_url not in existing_links:
                        print(f"🎉 New link found: {full_url}")
                        
                        # ✍️ Immediately append to file
                        with open(input_file, 'a') as f:
                            f.write(full_url + '\n')
                        
                        existing_links.add(full_url)
                        new_links += 1
                    else:
                        print(f"🔗 Already exists: {full_url}")

                if new_links:
                    print(f"✨ Found {new_links} new links from this page")

            except Exception as e:
                print(f"❌ Error processing {url}: {str(e)}")

        # Check if we should continue
        if len(existing_links - visited) == 0:
            print("\n🏁 No new links found. Exiting...")
            break

if __name__ == '__main__':
    print("🌟 Netflix Link Crawler 9000 🌟")
    find_netflix_links()
    print("✅ All done! Check your links.txt file")



#This is used to extract all netflix links from a single link put in a txt file(links.txt) use this to add links from your region, I only had access to content available in India. it'll keep searching for new links within that page and append those links to the links.txt file and iterate again and again until it doesn't find any new links.I used spider-man no way home as my first link. it went from 1 to 7 to 26 to 100+ to 600+ to 1000+ to ~800 to ~600 to ~300 to ~150 to ~70 to ~20 to ~2.don't remember exactly how it went but you understand the pattern. got a total of 6413 links