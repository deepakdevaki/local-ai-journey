try:
    import ollama
    print("💬 Week 7: Local Chat (Phi-3)")
    print("Type 'exit' to quit.\n")
    while True:
        q = input("You: ")
        if q.lower() == 'exit': break
        r = ollama.chat(model='phi3', messages=[{'role':'user','content':q}])
        print("Phi-3:", r['message']['content'], "\n")
except ImportError:
    print("Install Ollama + `pip install ollama` to run Week 7.")