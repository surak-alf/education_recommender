
# 🎓 Intelligent Course Recommender System  
**A human-centric AI system that combines knowledge graphs and graph neural networks to deliver interpretable, curriculum-aware course recommendations.**  

This project demonstrates:  

✅ **Knowledge Automation**: Structured prerequisite reasoning via RDF knowledge graphs  

✅ **Human-Centric ML**: Interactive feedback loops and GNNExplainer-driven transparency  

✅ **Scalable Learning**: PyTorch Geometric implementation for real-world deployment  

![project flowchart](mermaid-diagram-2025-04-18-091337.png)

*Fig 1. Knowledge Graph → GNN → Interactive UI Pipeline*

## 🌟 Key Innovations
| Feature                  | Technology Used       | Impact                          |
|--------------------------|-----------------------|----------------------------------|
| **Automated Prerequisite Reasoning** | RDFLib Knowledge Graph | Ensures curriculum compliance |
| **Graph Neural Networks** | PyTorch Geometric (GATConv) | Captures student-course patterns |
| **Explainable AI**       | GNNExplainer           | Shows "why" behind recommendations |
| **Human-in-the-Loop**    | Streamlit UI           | Allows user feedback refinement |

## 🚀 Quick Start
### Installation
```bash
# Clone repository
git clone https://github.com/surak-alf/education_recommender
cd education-recommender

# Install dependencies
pip install -r requirements.txt