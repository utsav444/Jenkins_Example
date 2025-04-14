import sys
import io

def main():
    # Configure stdout to handle UTF-8 encoding
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    
    print("\U0001f527 Jenkins CI/CD Demo Running...")
    print("This is a simple Jenkins pipeline demo!")
    print("All systems go!")

if __name__ == "__main__":
    main()
