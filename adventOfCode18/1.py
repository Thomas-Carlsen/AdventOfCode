
# Setup

f = open("1.txt",'r')

freqs_result = 0
freqs_results = [0]
freqs = []

for freq in f:
    freqs.append(int(freq))
    freqs_result = freqs_result + int(freq)
    freqs_results.append(freqs_result)


# First star

print("First Star:", sum(freqs))


# Second star


done = False
while not done:
    for freq in freqs:
        freqs_result = freqs_result + freq
        if freqs_result in freqs_results:
            done = True
            break
print("Second Star:", freqs_result)
