# 🇧🇩 Bengali Data Hub (বাংলা ডেটা হাব)

> The premier open-source catalog of curated, deduplicated, and categorized **Bengali Datasets** across diverse scientific and AI fields.
> Officially hosted at: [github.com/md-muqtadir-fuad/Bengali-Data-Hub](https://github.com/md-muqtadir-fuad/Bengali-Data-Hub)

![Total Datasets](https://img.shields.io/badge/Unique_Datasets-1,772-blue.svg)
![Kaggle Sources](https://img.shields.io/badge/Kaggle_Datasets-1,582-20BEFF.svg?logo=kaggle)
![Zenodo Sources](https://img.shields.io/badge/Zenodo_Records-114-003366.svg?logo=zenodo)
![Hugging Face](https://img.shields.io/badge/Hugging_Face-5-FFD21E.svg?logo=huggingface)
![Mendeley Data](https://img.shields.io/badge/Mendeley_Data-7-E9711C.svg)
![GitHub Repos](https://img.shields.io/badge/GitHub_Community-36-181717.svg?logo=github)
![Awesome-Bangla](https://img.shields.io/badge/Awesome--Bangla-32-orange.svg)
![BanglaNLP](https://img.shields.io/badge/BanglaNLP_BNLP-12-purple.svg)
![Multi-Source Linked](https://img.shields.io/badge/Multi--Source_Linked-16-success.svg)
![License](https://img.shields.io/badge/License-MIT-brightgreen.svg)

---

## 📌 Table of Contents
- [About the Hub](#-about-the-hub)
- [Repository Architecture](#-repository-architecture)
- [Deduplication Strategy & Multi-Source Linking](#-deduplication-strategy--multi-source-linking)
- [Consolidated Master Dataset](#-consolidated-master-dataset)
- [Part 1: Categorization by Task & Modality](#-part-1-categorization-by-task--modality)
- [Part 2: Categorization by Domain & Application Area](#-part-2-categorization-by-domain--application-area)
- [Credits, Sources & Acknowledgements](#-credits-sources--acknowledgements)
- [Dataset Schema & Fields](#-dataset-schema--fields)
- [Quickstart & Python Access](#-quickstart--python-access)

---

## 📖 About the Hub

**Bengali Data Hub** is an open initiative to catalog, deduplicate, and organize all available datasets for the Bengali language and Bangladesh across machine learning, computer vision, natural language processing, speech/audio, healthcare, agriculture, and socio-economic domains.

This repository brings together and harmonizes datasets from:
- **[Kaggle](https://www.kaggle.com)** (Community ML & competition datasets)
- **[Zenodo](https://zenodo.org)** (Open-access research papers & DOI-backed university archives)
- **[Hugging Face Hub](https://huggingface.co)** (Conversational dialogue, NLI benchmarks, reasoning and MMLU datasets)
- **[Mendeley Data / Elsevier](https://data.mendeley.com)** (Peer-reviewed academic datasets with persistent DOIs)
- **[BanglaKit / Awesome-Bangla](https://github.com/banglakit/awesome-bangla)** (Foundational computing tools, speech corpora & OCR resources)
- **[BanglaNLP / bnlp-resources](https://github.com/banglanlp/bnlp-resources)** (Benchmark tasks for POS, NER, MT, Sentiment, Authorship, News)
- **[GitHub Community](https://github.com)** (Leading independent research laboratories, university teams, and NLP authors)

---

## 📂 Repository Architecture

```text
Bengali-Data-Hub/
├── README.md                           # Main catalog and documentation
├── CREDITS.md                          # Full attribution, authors & BibTeX citations
├── LICENSE                             # MIT Open Source License
├── bengali_datasets_consolidated.csv   # Master deduplicated dataset (1,770+ entries)
├── deduplication_audit_log.csv         # Audit trail of merged cross-source duplicates
├── category-wise/                      # Main categorized directory
│   ├── task-and-modality/              # Categorized by AI task & modality (9 CSVs)
│   └── domain-and-application/         # Categorized by real-world domain (14 CSVs)
├── scripts/                            # Processing & deduplication engine
│   ├── process_datasets.py
│   ├── parse_external_sources.py
│   ├── parse_github_datasets.py
│   └── parse_new_batch.py
└── raw/                                # Raw scraped records (git-ignored)
```

---

## 🔍 Deduplication Strategy & Multi-Source Linking

When merging records across multiple platforms, duplicate entries frequently arise. To prevent redundancy while maintaining cross-platform access, the hub applies a **5-Tier Deduplication Pipeline**:

1. **Canonical URL Normalization**: Canonicalizes query parameters (`?fbclid=...`), protocols, trailing slashes, Hugging Face tree paths, and platform-specific IDs.
2. **Cross-Source Entity Fusion**: When an identical dataset exists on multiple platforms (e.g. Mendeley Data, Hugging Face, GitHub, Zenodo, Kaggle, Awesome-Bangla), the records are **fused into a single canonical entry**. The entry retains direct links to all platforms (`kaggle_url`, `zenodo_url`, `github_url`, `huggingface_url`, `mendeley_url`), merges author citations, and combines download/view counts.
3. **Author-Grounded Semantic Fingerprinting**: Normalizes titles (stripping boilerplate words such as `dataset`, `corpus`, `benchmark`, `v1.0`), and verifies author overlap before clustering.
4. **Component Disambiguation Guardrails**: Ensures distinct multi-part datasets (`Part 1` vs `Part 2`, `4-Class` vs `5-Class`) or datasets with identical generic titles by different authors are preserved.
5. **Audit Trail**: Every clustered and merged dataset is recorded in [`deduplication_audit_log.csv`](./deduplication_audit_log.csv) (99 duplicate clusters resolved).

---

## 📊 Consolidated Master Dataset

The master file [`bengali_datasets_consolidated.csv`](./bengali_datasets_consolidated.csv) contains all deduplicated records.

| Source Platform / Repository | Total Indexed | Description |
| :--- | :-: | :--- |
| **Kaggle Datasets** | 1,582 | Direct Kaggle community & competition datasets |
| **Zenodo Academic Datasets** | 114 | Academic papers, DOIs, and institutional archives |
| **Hugging Face Hub** | 5 | Conversational, reasoning & LLM evaluation benchmarks |
| **Mendeley Data / Elsevier** | 7 | Peer-reviewed university datasets with persistent DOIs |
| **GitHub Community Repositories** | 36 | Curated independent research datasets on GitHub |
| **BanglaKit / Awesome-Bangla** | 32 | Curated open-source computing & speech corpora |
| **BanglaNLP / bnlp-resources** | 12 | Standardized benchmark tasks and parallel corpora |
| **Multi-Source Linked Datasets** | **16** | Datasets available on 2 or more platforms simultaneously |
| **Total Consolidated Datasets** | **1,772** | Unified, deduplicated catalog |

---

## 🤖 Part 1: Categorization by Task & Modality

Located in [`category-wise/task-and-modality/`](./category-wise/task-and-modality/):

| # | Category Name | Scope & Modality | Datasets | CSV File Link |
| :-: | :--- | :--- | :-: | :--- |
| 1 | **Computer Vision (Images & Objects)** | Object detection, crop/leaf disease vision, face recognition, satellite imagery | **57** | [`category-wise/task-and-modality/computer-vision-images-objects.csv`](./category-wise/task-and-modality/computer-vision-images-objects.csv) |
| 2 | **Computer Vision (OCR & Handwriting)** | Handwritten characters, isolated numerals, license plates, document HTR/OCR | **133** | [`category-wise/task-and-modality/computer-vision-ocr-handwriting.csv`](./category-wise/task-and-modality/computer-vision-ocr-handwriting.csv) |
| 3 | **Multimodal & Video** | Visual question answering (VQA), image captioning, video datasets, memes, multimodal fake news | **41** | [`category-wise/task-and-modality/multimodal-video.csv`](./category-wise/task-and-modality/multimodal-video.csv) |
| 4 | **NLP - Corpus & Linguistics** | Raw text corpora, newspaper archives, dictionaries, lexicons, POS tagging, NER, punctuation | **188** | [`category-wise/task-and-modality/nlp-corpus-linguistics.csv`](./category-wise/task-and-modality/nlp-corpus-linguistics.csv) |
| 5 | **NLP - Text Classification & Sentiment** | Sentiment analysis, emotion detection, hate speech, offensive text, fake news, NLI, authorship | **200** | [`category-wise/task-and-modality/nlp-text-classification-sentiment.csv`](./category-wise/task-and-modality/nlp-text-classification-sentiment.csv) |
| 6 | **NLP - Translation & Generation** | English-Bangla translation, summarization, paraphrasing, GEC, LLM reasoning, MMLU & QA | **92** | [`category-wise/task-and-modality/nlp-translation-generation.csv`](./category-wise/task-and-modality/nlp-translation-generation.csv) |
| 7 | **Sign Language** | Bangla Sign Language (BdSL/BSL), gesture recognition, finger spelling, isolated signs | **53** | [`category-wise/task-and-modality/sign-language.csv`](./category-wise/task-and-modality/sign-language.csv) |
| 8 | **Speech & Audio** | Automatic Speech Recognition (ASR), Text-to-Speech (TTS), voice recordings, dialect audio corpora | **76** | [`category-wise/task-and-modality/speech-audio.csv`](./category-wise/task-and-modality/speech-audio.csv) |
| 9 | **Tabular & Statistical Data** | Structured tables, surveys, timeseries, census, economics, agriculture & climate stats | **932** | [`category-wise/task-and-modality/tabular-statistical-data.csv`](./category-wise/task-and-modality/tabular-statistical-data.csv) |

---

## 🌍 Part 2: Categorization by Domain & Application Area

Located in [`category-wise/domain-and-application/`](./category-wise/domain-and-application/):

| # | Domain Name | Core Focus & Applications | Datasets | CSV File Link |
| :-: | :--- | :--- | :-: | :--- |
| 1 | **Agriculture & Farming** | Crops, rice/jute yield, leaf disease, soil classification, weather impacts, fisheries | **53** | [`category-wise/domain-and-application/agriculture-farming.csv`](./category-wise/domain-and-application/agriculture-farming.csv) |
| 2 | **Demographics & Society** | Census statistics, population, poverty indices, gender studies, labor perceptions | **41** | [`category-wise/domain-and-application/demographics-society.csv`](./category-wise/domain-and-application/demographics-society.csv) |
| 3 | **Economy, Finance & Real Estate** | Stock prices, commodity OHLC, real estate, inflation, banking, ecommerce (Daraz), trade | **82** | [`category-wise/domain-and-application/economy-finance-real-estate.csv`](./category-wise/domain-and-application/economy-finance-real-estate.csv) |
| 4 | **Education & Academics** | Exam questions (BEnQA), math word problems (SOMADHAN), MMLU benchmarks, admissions, textbooks | **41** | [`category-wise/domain-and-application/education-academics.csv`](./category-wise/domain-and-application/education-academics.csv) |
| 5 | **General & Miscellaneous** | Multipurpose datasets, cross-cutting statistical collections, unspecialized tables | **517** | [`category-wise/domain-and-application/general-miscellaneous.csv`](./category-wise/domain-and-application/general-miscellaneous.csv) |
| 6 | **Governance, Law, Politics & Transport** | Traffic, road safety, crime records, legal statutes, election data, public transit | **102** | [`category-wise/domain-and-application/governance-law-politics-transport.csv`](./category-wise/domain-and-application/governance-law-politics-transport.csv) |
| 7 | **Healthcare & Medicine** | COVID-19, clinical notes, disease classification, hospital records, mental health, medical imaging | **103** | [`category-wise/domain-and-application/healthcare-medicine.csv`](./category-wise/domain-and-application/healthcare-medicine.csv) |
| 8 | **Industry, Energy & Manufacturing** | RMG garment sector, textiles, electricity generation, power grids, solar data | **10** | [`category-wise/domain-and-application/industry-energy-manufacturing.csv`](./category-wise/domain-and-application/industry-energy-manufacturing.csv) |
| 9 | **Linguistics & Language Research** | Grammar, corpora, phonetics, dialects, morphology, lexicons, translation, NLP evaluation | **516** | [`category-wise/domain-and-application/linguistics-language-research.csv`](./category-wise/domain-and-application/linguistics-language-research.csv) |
| 10 | **News & Media** | Newspaper archives (Prothom Alo, Daily Star), headlines, journalism, fake news, fact-checking | **80** | [`category-wise/domain-and-application/news-media.csv`](./category-wise/domain-and-application/news-media.csv) |
| 11 | **Social Media, Arts & Culture** | Social media sentiment, literature, poetry, movies, religion, cultural alignment (BanglaSocialBench) | **110** | [`category-wise/domain-and-application/social-media-arts-culture.csv`](./category-wise/domain-and-application/social-media-arts-culture.csv) |
| 12 | **Sports & Recreation** | Cricket match records (IPL, BPL), football stats, tournament histories, player metrics | **8** | [`category-wise/domain-and-application/sports-recreation.csv`](./category-wise/domain-and-application/sports-recreation.csv) |
| 13 | **Technology & Telecommunications** | Telecom networks, mobile devices, IT usage, software engineering, cyber security | **47** | [`category-wise/domain-and-application/technology-telecommunications.csv`](./category-wise/domain-and-application/technology-telecommunications.csv) |
| 14 | **Weather, Climate & Environment** | Rainfall, temperature, cyclones, air quality (AQI), flood forecasts, environmental sensors | **62** | [`category-wise/domain-and-application/weather-climate-environment.csv`](./category-wise/domain-and-application/weather-climate-environment.csv) |

---

## 🌟 Credits, Sources & Acknowledgements

A complete attribution record with maintainer profiles, affiliations, research paper DOIs, and BibTeX citations is published in [`CREDITS.md`](./CREDITS.md).

Special recognition to upstream catalogs and contributors:
- **BanglaKit / Awesome-Bangla** ([github.com/banglakit/awesome-bangla](https://github.com/banglakit/awesome-bangla))
- **BanglaNLP / bnlp-resources** ([github.com/banglanlp/bnlp-resources](https://github.com/banglanlp/bnlp-resources))
- **Sabbir Hossain Ujjal / Awesome_Bangla_Datasets** ([github.com/sabbirhossainujjal/Awesome_Bangla_Datasets](https://github.com/sabbirhossainujjal/Awesome_Bangla_Datasets))
- **Elite Research Lab / BanglaNLP-Hub** ([github.com/eliteresearchlab/BanglaNLP-Hub](https://github.com/eliteresearchlab/BanglaNLP-Hub))
- **CSE BUET NLP** for pioneering BanglaBERT, DailyDialogue (BN), and XNLI (BN)
- **Mendeley Data authors** from BUBT, IUB, NSU, DU, and international research universities
- **Community Researchers** across GitHub, Hugging Face, and Kaggle

---

## 📋 Dataset Schema & Fields

| Field Name | Description | Example Value |
| :--- | :--- | :--- |
| `id` | Unique ID in the hub | `BD-0128` |
| `title` | Canonical title of dataset | `BanglaRumorCorpus — Bengali Rumor Detection Dataset` |
| `sources` | Platform(s) hosting this dataset | `Zenodo, Kaggle` |
| `task_and_modality` | Primary technical task & data modality | `NLP - Text Classification & Sentiment` |
| `domain_and_application` | Application domain or real-world subject | `News & Media` |
| `author` | Creator, authors, or research team | `Rimon Kanthi Devnath, Md Akash Rahman` |
| `url` | Primary direct URL | `https://zenodo.org/records/17259976` |
| `kaggle_url` | Direct Kaggle link (if available) | `https://www.kaggle.com/datasets/...` |
| `zenodo_url` | Direct Zenodo link (if available) | `https://zenodo.org/records/...` |
| `github_url` | Direct GitHub / repository link | `https://github.com/...` |
| `huggingface_url` | Direct Hugging Face dataset link | `https://huggingface.co/datasets/...` |
| `mendeley_url` | Direct Mendeley Data link | `https://data.mendeley.com/datasets/...` |
| `last_updated` | Latest date or timeframe | `Uploaded on July 29, 2024` |
| `downloads` | Combined download count | `1,240` |
| `upvotes_or_views` | Views / upvotes metric | `520` |
| `rating` | Kaggle usability rating (0-10) | `10.0` |
| `file_size` | Size of dataset | `34 MB` |
| `file_formats` | Data format (CSV, JSON, Images, etc.) | `1 File (CSV)` |
| `description` | Summary or research abstract | `A curated dataset for rumor detection...` |
| `dedup_status` | Deduplication provenance | `Merged (Zenodo + Kaggle)` |

---

## 💻 Quickstart & Python Access

### Load and Filter with Pandas
```python
import pandas as pd

# Load the consolidated master catalog
df = pd.read_csv('bengali_datasets_consolidated.csv')

# Find all cross-platform datasets (available on multiple platforms)
multi_source = df[df['sources'].str.contains(',') ]
print(f'Cross-platform datasets: {len(multi_source)}')
print(multi_source[['title', 'sources', 'url']].head())

# Filter for Reasoning & MMLU Benchmarks
reasoning_df = df[df['description'].str.contains('reasoning|mmlu', case=False, na=False)]
print(f'Reasoning datasets: {len(reasoning_df)}')
```

### Refreshing the Catalog
To re-run the deduplication and update all tables:
```bash
python scripts/process_datasets.py
```
