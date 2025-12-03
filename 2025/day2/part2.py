with open("input.txt") as f:
    input: list = f.readline().split(",")

def calculate_ngrams(ngram: int, text: str) -> list:
    ngrams = []
    for i in range(len(text)):
        gram = text[i:i+ngram]
        ngrams.append(gram)
    return ngrams


def has_repeating_pattern(number: int) -> bool:
    result = False
    # find all possible ngrams
    ngrams: list = []
    grams = len(str(number)) // 2
    for i in range(1,grams+1):
        ngrams.append(i)
    #print(ngrams)
    for i in range(len(ngrams)):
        ngrams = calculate_ngrams(int(ngrams[i]), str(number))
        #print(f"ngrams: {ngrams}")
        ngram_set = set(ngrams)
        if len(ngram_set) == 1:
            print(ngrams)


    return result

def find_invalid(input) -> list:
    input = input.split("-")
    candidates: list = [candidate for candidate in range(int(input[0]), int(input[1]) + 1)]
    invalid_values = [candidate for candidate in candidates if has_repeating_pattern(candidate)]
    return invalid_values

results = []
for i in enumerate(input):
    results = results + find_invalid(i[1])
    
print(results)
print(f"Sum of invalid IDs: {sum(results)}")

print(calculate_ngrams(4, "1231231"))


