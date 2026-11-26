line = "One percent left. Before I go: your screen time today was 11 hours — so technically, you killed me."

def validate(text):
    assert len(text) <= 200
    return text

print(validate(line), end="")
