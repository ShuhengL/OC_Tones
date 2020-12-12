from scipy.stats import binom

# Probability of words from each tone appearing
ruh = 53 / 75
chiuh = 22 / 75

# Get the probabilities for each (i+2)-word unmixed sequence
unmixed = [0, 0, 0, 0, 0]
for i in range(0, 5):
    unmixed[i] = (ruh ** (i + 2) + chiuh ** (i + 2))

# Get the probabilities for mixed sequence, which is simply 1 - unmixed prob
mixed = [1 - x for x in unmixed]

# Calculate the extreme to compare
extreme = binom.cdf(0, 21, mixed[0]) * binom.cdf(3, 4, mixed[1]) * binom.cdf(
    1, 3, mixed[2]) * binom.cdf(1, 1, mixed[3]) * binom.cdf(0, 1, mixed[4])

m_list = []
counter = 0
point_counter = 0
for a in range(22):
    for b in range(5):
        for c in range(4):
            for d in range(2):
                for e in range(2):
                    counter += 1
                    curr_extreme = binom.cdf(a, 21, mixed[0]) * binom.cdf(b, 4, mixed[1]) * binom.cdf(
                        c, 3, mixed[2]) * binom.cdf(d, 1, mixed[3]) * binom.cdf(e, 1, mixed[4])
                    if curr_extreme <= extreme:
                        # If more extreme
                        m_list.append((a, b, c, d, e))
                        print('{}. {}, {}, {}, {}, {}, extreme = {} < {}'.format(
                            counter, a, b, c, d, e, curr_extreme, extreme))
                        point_counter += 1
                    else:
                        print('{}. {}, {}, {}, {}, {}, extreme = {}'.format(
                            counter, a, b, c, d, e, curr_extreme))

final_prob = 0
for (a, b, c, d, e) in m_list:
    final_prob += binom.pmf(a, 21, mixed[0]) * binom.pmf(b, 4, mixed[1]) * binom.pmf(
        c, 3, mixed[2]) * binom.pmf(d, 1, mixed[3]) * binom.pmf(e, 1, mixed[4])

print('There are {} pairs in total'.format(point_counter))
print('Final probability = {}'.format(final_prob))
