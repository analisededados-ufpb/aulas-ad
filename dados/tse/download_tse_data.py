from pathlib import Path
import requests
import wget

URLS = [
    'https://cdn.tse.jus.br/estatistica/sead/odsele/consulta_cand/consulta_cand_2022.zip',
    'https://cdn.tse.jus.br/estatistica/sead/odsele/consulta_cand/consulta_cand_2018.zip'
]

OUTPUT_DIR = '.'

def download_file(url, output_dir='.'):
    local_filename = Path(output_dir) / url.split('/')[-1]
    with requests.get(url, stream=True, headers={'User-agent': 'Mozilla/5.0'}) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192): 
                f.write(chunk)
    return local_filename

for url in URLS:
    print("Downloading ", url)
    download_file(url)
