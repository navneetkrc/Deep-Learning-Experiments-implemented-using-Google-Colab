import streamlit as st
import torch
from transformers import AutoTokenizer, AutoModelForTokenClassification
import numpy as np

def main():
    st.title("Custom NER with modern-gliner-bi-large")
    st.write("This app uses the knowledgator/modern-gliner-bi-large-v1.0 model for named entity recognition with custom labels.")
    
    # Model and tokenizer loading with caching
    @st.cache_resource
    def load_model_and_tokenizer():
        model_name = "knowledgator/modern-gliner-bi-large-v1.0"
        tokenizer = AutoTokenizer.from_pretrained(model_name)
        model = AutoModelForTokenClassification.from_pretrained(model_name)
        return tokenizer, model
    
    with st.spinner("Loading model and tokenizer..."):
        tokenizer, model = load_model_and_tokenizer()
        st.success("Model loaded successfully!")
    
    # Custom labels input
    st.subheader("1. Define Your Custom Labels")
    st.write("Enter each label on a new line")
    custom_labels_text = st.text_area("Custom Labels (one per line)", 
                                      "PERSON\nORGANIZATION\nLOCATION\nDATE", 
                                      height=150)
    custom_labels = [label.strip() for label in custom_labels_text.split("\n") if label.strip()]
    
    # Text input
    st.subheader("2. Enter Text for Entity Recognition")
    text_input = st.text_area("Text to analyze", 
                             "John Smith works at Google in Mountain View since January 2020.", 
                             height=150)
    
    # Prediction function
    def predict_entities(text, labels):
        inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True)
        
        with torch.no_grad():
            outputs = model(**inputs)
            
        # Get the predictions
        predictions = torch.argmax(outputs.logits, dim=2)
        
        # Map token indices to input tokens
        tokens = tokenizer.convert_ids_to_tokens(inputs["input_ids"][0])
        token_predictions = [model.config.id2label[prediction.item()] for prediction in predictions[0]]
        
        # Process results
        results = []
        current_entity = None
        current_text = ""
        
        for i, (token, prediction) in enumerate(zip(tokens, token_predictions)):
            # Skip special tokens
            if token in [tokenizer.cls_token, tokenizer.sep_token, tokenizer.pad_token]:
                continue
                
            # Handle subword tokens
            if token.startswith("##"):
                if current_entity:
                    current_text += token[2:]
                continue
                
            # Check if we have a B- or I- tag
            if prediction.startswith("B-"):
                # If we were tracking an entity, add it to results
                if current_entity:
                    results.append((current_text, current_entity))
                
                entity_type = prediction[2:]
                # Only track entities that match our custom labels
                if entity_type in labels:
                    current_entity = entity_type
                    current_text = token
                else:
                    current_entity = None
                    current_text = ""
                    
            elif prediction.startswith("I-") and current_entity:
                # Continue the current entity
                current_text += " " + token
                
            else:
                # End of entity or O tag
                if current_entity:
                    results.append((current_text, current_entity))
                    current_entity = None
                    current_text = ""
        
        # Add the last entity if there is one
        if current_entity:
            results.append((current_text, current_entity))
            
        return results
    
    # Process and display results
    if st.button("Extract Entities"):
        if not text_input.strip():
            st.error("Please enter some text to analyze.")
        elif not custom_labels:
            st.error("Please enter at least one custom label.")
        else:
            with st.spinner("Extracting entities..."):
                results = predict_entities(text_input, custom_labels)
                
                if results:
                    st.subheader("Extracted Entities")
                    
                    # Create a color map for different entity types
                    colors = {}
                    default_colors = ["#FF9AA2", "#FFB7B2", "#FFDAC1", "#E2F0CB", "#B5EAD7", "#C7CEEA"]
                    
                    for i, label in enumerate(custom_labels):
                        colors[label] = default_colors[i % len(default_colors)]
                    
                    # Display entities with highlighting
                    entities_html = text_input
                    for entity_text, entity_type in results:
                        if entity_text in entities_html:
                            highlight = f'<span style="background-color: {colors[entity_type]}; padding: 2px; border-radius: 3px;">{entity_text} <small>({entity_type})</small></span>'
                            entities_html = entities_html.replace(entity_text, highlight, 1)
                    
                    st.write("Text with highlighted entities:")
                    st.markdown(entities_html, unsafe_allow_html=True)
                    
                    # Display entities in a table
                    st.write("Extracted entities table:")
                    entity_data = {"Entity": [], "Type": []}
                    for entity_text, entity_type in results:
                        entity_data["Entity"].append(entity_text)
                        entity_data["Type"].append(entity_type)
                    
                    st.dataframe(entity_data)
                else:
                    st.info("No entities matching your custom labels were found in the text.")

if __name__ == "__main__":
    main()
