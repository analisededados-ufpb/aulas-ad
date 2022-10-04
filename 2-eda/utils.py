
import electionsBR
import pandas as pd
import requests

def download_file(url):
    local_filename = url.split('/')[-1]
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192): 
                f.write(chunk)
    return local_filename

def etl_eleicoes(input_dir, output_file):
    eleicoes = load_eleicoes(input_dir)
    eleicoes.to_csv(output_file)
    return eleicoes

def load_candidatos(tse_data_dir, ano, uf='BR', cargo="PRESIDENTE"):
    cand = (
        pd.read_csv(tse_data_dir / f'consulta_cand_{ano}/consulta_cand_{ano}_{uf}.csv',
                    encoding='latin1', delimiter=';')
        .query(f"DS_CARGO == '{cargo}'")
    )
    cand.columns = cand.columns.str.lower()
    return cand

def load_eleicoes_2018():
    rename_votacao_18 = {
        'ano_eleicao': 'ano_eleicao',
        'num_turno': 'nr_turno',
        'numero_candidato': 'nr_candidato',
        'nome_urna_candidato': 'nm_urna_candidato',
        'uf': 'uf',
        'qtde_votos': 'votos'
    }
    votos = electionsBR.get_elections(year=2018, position="President", regional_aggregation="State")
    votos.columns = votos.columns.str.lower()
    votos = votos.rename(columns=rename_votacao_18)
    votos = votos.filter(rename_votacao_18.values())
    votos['votos'] = votos['votos'].astype(int)
    votos = (
        votos
        .groupby(['ano_eleicao', 'nr_turno', 'nr_candidato', 'nm_urna_candidato', 'uf'], as_index=False)
        .agg('sum')
    )
    votos['perc_votos'] = 100 * (votos['votos'] / votos.groupby(['nr_turno', 'uf'])['votos'].transform('sum'))
    return votos

def load_votacao_2022(uf="BR"):
    rename_votacao_22 = {
        'n': 'nr_candidato',
        'vap': 'votos',
        'pvap': 'perc_votos'
    }
    ufl = uf.lower()
    votacao_22 = pd.read_json(f'https://resultados.tse.jus.br/oficial/ele2022/544/dados-simplificados/{ufl}/{ufl}-c0001-e000544-r.json')
    votos_cand_22 = pd.json_normalize(votacao_22.cand)
    votos_cand_22['pvap'] = votos_cand_22['pvap'].str.replace(',', '.').astype(float)
    votos_cand_22['n'] = votos_cand_22['n'].astype(int)
    votos_cand_22 = votos_cand_22.rename(columns=rename_votacao_22).filter(rename_votacao_22.values())
    votacao_22 = votacao_22.drop(columns=['cand']).iloc[0]
    return votos_cand_22, votacao_22

def load_eleicoes_2022(tse_data_dir, uf='BR', cargo="PRESIDENTE"):
    cand = load_candidatos(tse_data_dir, 2022)
    votos_cand, _ = load_votacao_2022(uf)
    eleicoes = (
        cand.merge(votos_cand, on='nr_candidato')
        .assign(uf=uf)
        .filter(['ano_eleicao', 'nr_turno', 'nr_candidato', 'nm_urna_candidato', 'uf', 'votos', 'perc_votos'])
    )
    return eleicoes

def load_eleicoes(tse_data_dir):
    eleicao_18 = load_eleicoes_2018()
    eleicao_22 = pd.concat([load_eleicoes_2022(tse_data_dir, uf) for uf in eleicao_18.uf])
    eleicoes = pd.concat([eleicao_18, eleicao_22]).reset_index(drop=True)
    eleicoes['nr_turno'] = eleicoes['nr_turno'].astype('int64')
    eleicoes['ano_eleicao'] = eleicoes['ano_eleicao'].astype('int64')
    eleicoes['nr_candidato'] = eleicoes['nr_candidato'].astype('int64')
    return eleicoes
