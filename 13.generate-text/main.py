from transformers import pipeline
model = pipeline("text-generation", model="gpt2")

sentence = model("Hi, My name is John Cenam, I am here", do_sample=True,
                 top_k=50, temperature=0.9, max_length=100, num_return_sentences=2)
for i in sentence:
    print(i["generated_text"])