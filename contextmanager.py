class ContextManager:
    def __init__(self):
        print("inicjacja init()")

    def __enter__(self):
        print("inicjacja enter()")

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("inicjacja exit()")


with ContextManager() as manager:
    print("działanie bloku with...")

print("ciąg dalszy...")

