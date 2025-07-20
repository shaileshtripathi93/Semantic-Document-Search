# 🧠 Semantic Document Search with Streamlit & HuggingFace Embeddings
[Watch Demo Video](./Screen Recording 2025-07-20 101016.mp4)

This is a simple yet powerful **semantic search web app** built using **Streamlit** and **LangChain's HuggingFace embeddings**. It allows users to enter natural language queries and find the most relevant document from a predefined list using **cosine similarity**.

---

## 🚀 Features

- Natural language search (semantic matching)
- Real-time results via Streamlit
- HuggingFace Sentence Transformer embeddings
- Cosine similarity scoring
- Top matching document with score display

---

## 📸 Demo

![App Screenshot](https://user-images.githubusercontent.com/your-screenshot.png) <!-- optional -->

---

## 🛠 Tech Stack

| Tool              | Description                                 |
|-------------------|---------------------------------------------|
| `Streamlit`       | Python web app framework                    |
| `LangChain`       | Framework for LLM applications              |
| `HuggingFace`     | Pre-trained sentence transformer embeddings |
| `scikit-learn`    | Cosine similarity from sklearn              |
| `NumPy`           | Numerical operations                        |

---

## 📂 Project Structure


---

## 📝 How It Works

1. A set of cricket player descriptions is hardcoded.
2. A query is entered by the user in natural language.
3. Each document and query is embedded using `all-MiniLM-L6-v2`.
4. Cosine similarity is calculated between the query and documents.
5. The top matching document is displayed with a similarity score.

---

## ▶️ Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/shaileshtripathi93/semantic-search-streamlit.git
cd semantic-search-streamlit
