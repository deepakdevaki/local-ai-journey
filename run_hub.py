import os

def main():
    print("🧠 LOCAL AI JOURNEY — Your Sovereign Intelligence")
    print("\nChoose your adventure:")
    print("1. 🚲 Week 1: Bike Rental Predictor")
    print("2. 🔢 Week 3: Handwritten Digit CNN")
    print("3. ⚖️ Week 5: Fair Hiring Simulator")
    print("4. 👕 Week 6: Fashion Classifier")
    print("5. 💬 Week 7: Chat with Phi-3")
    print("6. 👁️ Week 8: Vision Agent")
    print("7. 🔍 Week 9: Knowledge Agent")
    print("8. 🧪 Generate Sample Images")

    choice = input("\nEnter 1-8: ").strip()
    
    scripts = {
        "1": "week1_bike.py",
        "2": "week3_mnist.py",
        "3": "week5_fair_hiring.py",
        "4": "week6_fashion_cnn.py",
        "5": "week7_chat.py",
        "6": "week8_vision_agent.py",
        "7": "week9_knowledge_agent.py",
        "8": "generate_sample_images.py"
    }
    
    if choice in scripts and os.path.exists(scripts[choice]):
        os.system(f"python {scripts[choice]}")
    else:
        print("File not found. Ensure all .py files are in this folder.")

if __name__ == "__main__":
    main()