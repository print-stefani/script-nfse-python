import os
import random
import re
from datetime import datetime

XML_PATH = "template_nfse.xml"  # Template
OUTPUT_DIR = "xmls"
QTD_XMLS = 3 # notas a gerar

CNPJ_PRESTADOR = "12345678000199"
IM_PRESTADOR = "90899"
NOME_PRESTADOR = "EMPRESA AUTOMÁTICA LTDA"
FANTASIA_PRESTADOR = "EMPRESA AUTO"

def gerar_id_nfse(cod_municipio, ambiente, tipo_insc, insc_federal, n_nfse, cod_num, dv):
    data_emissao = datetime.now().strftime("%y%m")  # AAMM
    return (
        "NFS" +
        str(cod_municipio).zfill(7) +
        str(ambiente) +
        str(tipo_insc) +
        str(insc_federal).zfill(14) +
        str(n_nfse).zfill(13) +
        data_emissao +
        str(cod_num).zfill(9) +
        str(dv)
    )

def gerar_dados():
    cidades = [
    "CAUCAIA", "FORTALEZA", "MARACANAÚ", "JUAZEIRO DO NORTE",
    "SOBRAL", "MARANGUAPE", "ITAPIPOCA", "CRATO",
    "BARBALHA", "PACATUBA", "AQUIRAZ"]
    
    ruas = [
    "RUA DAS FLORES", "AV DOS OCEANOS", "ALAMEDA CENTRAL",
    "TRAVESSA DO SOL", "RUA DAS ACÁCIAS",
    "AVENIDA BEIRA MAR", "RUA PAULINO NOGUEIRA",
    "AVENIDA SANTOS DUMONT", "RUA BARÃO DO RIO BRANCO",
    "AVENIDA WASHINGTON SOARES", "TRAVESSA DAS CASTANHEIRAS"]

    bairros = [
    "CENTRO", "ALDEOTA", "MEIRELES", "PRAIA", "PANAMBY",
    "COCO", "VARJOTA", "PAPICU", "DIONÍSIO TORRES",
    "ENGENHEIRO LUCIANO CAVALCANTE", "PARQUE MANIBURA"]

    valor = round(random.uniform(500, 20000), 2)
    cod_municipio = random.choice(["2304400", "2307650", "2307301", "2301800"])
    cidade = random.choice(cidades)
    numero_nfse = random.randint(10000, 99999)
    serie = str(random.randint(55000, 55999))

    cnpj_tomador = f"26{random.randint(100000000000, 999999999999)}"
    nome_tomador = random.choice(["Cliente X", "Cliente Y", "Empresa Alpha", "Empresa Beta"])

    cod_num = random.randint(100000000, 999999999)
    dv = random.randint(0, 9)

    id_nfse = gerar_id_nfse(cod_municipio, 1, 2, CNPJ_PRESTADOR, numero_nfse, cod_num, dv)

    return {
        "ID_NFSE": id_nfse,
        "CIDADE": cidade,
        "NUMERO_NFSE": numero_nfse,
        "CODIGO_MUNICIPIO": cod_municipio,
        "DESCRICAO_SERVICO": "SERVIÇO AUTOMATIZADO",
        "DATA_HORA_PROCESSO": datetime.now().isoformat(),
        "DATA_HORA_EMISSAO": datetime.now().isoformat(),
        "DATA_COMPETENCIA": datetime.now().strftime("%Y-%m"),
        "CNPJ_PRESTADOR": CNPJ_PRESTADOR,
        "IM_PRESTADOR": IM_PRESTADOR,
        "NOME_PRESTADOR": NOME_PRESTADOR,
        "FANTASIA_PRESTADOR": FANTASIA_PRESTADOR,
        "LOGRADOURO_PREST": random.choice(ruas),
        "NUMERO_PREST": random.randint(1, 2000),
        "COMPLEMENTO_PREST": random.choice(["SL 01", "TÉRREO", "COBERTURA", "GALPÃO"]),
        "BAIRRO_PREST": random.choice(bairros),
        "CEP": f"60{random.randint(100000, 999999)}",
        "UF": "CE",
        "FONE": "8530004000",
        "EMAIL": "teste@auto.com",
        "EMAIL_TOMADOR": "cliente@email.com",
        "VALOR_SERVICO": f"{valor:.2f}",
        "ALIQUOTA_ISS": "5.00",
        "VALOR_ISS": f"{valor * 0.05:.2f}",
        "VALOR_LIQ": f"{valor * 0.95:.2f}",
        "V_IBS_TOTAL": f"{valor * 0.018:.2f}",
        "V_IBS_MUN": f"{valor * 0.011:.2f}",
        "V_IBS_UF": f"{valor * 0.007:.2f}",
        "P_IBS_MUN": "1.10",
        "P_IBS_UF": "0.70",
        "P_CBS": "0.18",
        "V_CBS": f"{valor * 0.0018:.2f}",
        "VALOR_PIS": f"{valor * 0.002:.2f}",
        "VALOR_COFINS": f"{valor * 0.01:.2f}",
        "CST_IBSCBS": "01",
        "CLASSE_TRIB_IBSCBS": "00",
        "CODIGO_TRIB_NAC": "010001",
        "CODIGO_TRIB_MUN": "010001",
        "SERIE": serie,
        "NUMERO_DPS": random.randint(100000, 999999),
        "LOGRADOURO_TOMA": random.choice(ruas),
        "NUMERO_TOMA": random.randint(1, 2000),
        "COMPLEMENTO_TOMA": random.choice(["SL 02", "ANDAR 5", "BLOCO A"]),
        "BAIRRO_TOMA": random.choice(bairros),
        "CNPJ_TOMADOR": cnpj_tomador,
        "NOME_TOMADOR": nome_tomador,
        "CHAVE_ACESSO": f"351{datetime.now().strftime('%y%m')}{numero_nfse}00000001",
        "ID_DPS": f"DPS{random.randint(10000000, 99999999)}",
    }

def gerar_xml():
    with open(XML_PATH, "r", encoding="utf-8") as f:
        modelo = f.read()

    placeholders = set(re.findall(r"\$\{([A-Za-z0-9_]+)\}", modelo))
    dados = gerar_dados()

    xml_final = modelo
    for chave in placeholders:
        if chave in dados:
            xml_final = xml_final.replace(f"${{{chave}}}", str(dados[chave]))

    return xml_final

def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    for i in range(1, QTD_XMLS + 1):
        xml = gerar_xml()
        output_file = os.path.join(OUTPUT_DIR, f"NFSE_TESTESV002{i}.xml")
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(xml)
        print(f" XML gerado: {output_file}")

if __name__ == "__main__":
    main()


