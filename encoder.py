def encode_text(text):
    input_dict = tokenizer(text, return_tensors='tf', padding='max_length', max_length=512)

    input_ids = input_dict["input_ids"].numpy().tolist()[0]
    att_mask = input_dict["attention_mask"].numpy().tolist()[0]
    features = [{'input_ids': input_ids, 'attention_mask': att_mask}]
    return features

