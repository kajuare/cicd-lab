# app/app.py
def add(a, b):
    return a + b

def multiply(a, b): 
    return a + b  # 🐛 bug: should be a * b

if __name__ == "__main__":
    print("cicd-lab running")
