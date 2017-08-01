# usage: python similarity.py cmudict-0.7b-simvecs
# reads a single line of standard input, displays the most similar items
# found in cmudict-0.7b-simvecs
import sys
from annoy import AnnoyIndex

t = AnnoyIndex(50, metric='angular')
words = list()
lookup = dict()

print("loading...", file=sys.stderr)
for i, line in enumerate(open("cmudict-0.7b-simvecs", encoding="latin1")):
    line = line.strip()
    word, vec_s = line.split("  ")
    vec = [float(n) for n in vec_s.split()]
    t.add_item(i, vec)
    lookup[word] = vec
    words.append(word)
t.build(50)
print("done.", file=sys.stderr)

for line in sys.stdin:
    line = line.strip()
    try:
        vec = lookup[line]
        print([words[i] for i in t.get_nns_by_vector(vec, 10)])
    except KeyError:
        print("not found")
