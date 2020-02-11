This notebook trained a BERT based classifier to predict the toxicity score of various texts. We implement a simple binary
classifier that predicts if a piece of text is toxic or not. We use the Huggingface BERT implementation in PyTorch. 
Huggingface has a pre-trained model called BertForSequenceClassification that is used.


|                | P100                   | V100                    | P100 (2 Epochs)         |
|----------------|------------------------|-------------------------|-------------------------|
| Data Load Time | Wall time: 34min 4s    | Wall time: 33min 53s    | Wall time: 34min 8s     |
| Training Time  | Wall time: 6h 4min 16s | Wall time: 1h 51min 21s | Wall time: 12h 8min 25s |
| Inference Time | Wall time: 1h 42s      | Wall time: 15min 39s    | Wall time: 1h 42s       |
| AUC score      | 0.97000                | 0.96990                 | 0.96971                 |
