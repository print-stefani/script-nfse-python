# Automação de Geração de NFSe com Python (POC)

Este projeto é uma **prova de conceito (POC)** desenvolvida para automatizar a geração de arquivos **XML de NFSe** utilizando **Python**.

O código se baseia em um **template XML**, identifica os placeholders marcados via `${CHAVE}`, e os substitui com dados gerados automaticamente para simular múltiplos cenários.  
📌 *Todos os dados presentes são fictícios e utilizados apenas para fins de teste e estudo.*

---

## 🎯 Objetivos da POC

- Automatizar a geração de XMLs fiscais (NFSe)
- Simular diferentes emissões utilizando variáveis dinâmicas
- Facilitar testes de integração e validação com sistema fiscal
- Comprovar a viabilidade técnica para automação e geração em lote

---

## 🏢 Integração com Sistema Fiscal

Antes da geração dos XMLs, foi realizado o **mapeamento das tags (de–para)** comparativo ABRASF com NFSe para adequação ao **Sistema fiscal**.

🔹 Nos testes realizados, os arquivos XML foram **processados e identificados como NFSe pelo sistema**, validando a estrutura utilizada.

> ⚠️ A integração com o sistema fiscal/ERP não faz parte deste repositório.  
> O foco aqui é **apenas a automação da geração dos XMLs**.

---

## ▶️ Como executar

Clonar o repositório
- git clone https://github.com/print-stefani/script-nfse-python.git
- cd repositorio

Executar o script
- python gerar_nfse.py

Os arquivos XML serão gerados automaticamente na pasta /xmls.

---

🔍 Principais adaptações técnicas

✔ Template XML com variáveis ${CHAVE}
✔ Preenchimento automático com dados simulados
✔ Controle de quantidade de notas geradas
✔ Estrutura preparada para escalabilidade (emissão em lote)

📌 Exemplo de placeholder substituído
<ID_NFSE>${ID_NFSE}</ID_NFSE>
<NOME_PRESTADOR>${NOME_PRESTADOR}</NOME_PRESTADOR>
<VALOR_SERVICO>${VALOR_SERVICO}</VALOR_SERVICO>


Após a automação:

<ID_NFSE>NFS230440001...</ID_NFSE>
<NOME_PRESTADOR>EMPRESA AUTOMÁTICA LTDA</NOME_PRESTADOR>
<VALOR_SERVICO>12500.50</VALOR_SERVICO>

---

>⚠️ Avisos importantes
 - ❗ Este projeto é apenas uma prova de conceito (POC).
 - ❗ Os dados utilizados são simulados e não representam documentos fiscais válidos.
 - ❗ Não utilize este código em ambiente de produção sem adaptações técnicas e validações fiscais.

📣 Contato
Se quiser trocar experiências sobre automação fiscal, integração com sistemas ou desenvolvimento em Python:

stefanibeatrizcv@gmail.com

---

📌 Licença

Este projeto está licenciado sob a MIT License – fique à vontade para utilizar e evoluir o código para estudos.
