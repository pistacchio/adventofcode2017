import math

MEMORY_BANKS = [11,11,13,7,0,15,5,5,4,4,1,1,7,1,15,11]

tried_solutions = []

def distribute(banks):
    bank_idx = banks.index(max(banks))
    bank_value = banks[bank_idx]
    bank_tokens = int(math.ceil(float(bank_value)  / len(banks)))

    current_bank_idx = bank_idx + 1
    distruted_tokens = 0
    while True:
        if current_bank_idx == len(banks):
            current_bank_idx = 0

        if current_bank_idx == bank_idx:
            break

        if distruted_tokens < bank_value:
            banks[current_bank_idx] += bank_tokens
            distruted_tokens += bank_tokens
        current_bank_idx += 1

    banks[bank_idx] = max(0, bank_value - (bank_tokens * (len(banks) - 1)))


while True:
    distribute(MEMORY_BANKS)
    if MEMORY_BANKS in tried_solutions:
        break

    tried_solutions.append(MEMORY_BANKS[:])

print len(tried_solutions) + 1
