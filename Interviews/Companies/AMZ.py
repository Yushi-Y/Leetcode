import random
import statistics

# Bootstrap the proportion of vowels in a list of words:
# repeatedly sample k words (with replacement), compute the 
# vowel proportion of each sample, then report the mean and std dev.

def count_vowel_proportions(words):
    string = ''.join(words)
    num_of_vowels = sum(1 for c in string if c in 'aeiou')
    total_letters = len(string)

    return num_of_vowels/total_letters
    

class Bootstrapper:
    def __init__(self, data, stats_func):
        self.data = data
        self.stats_func = stats_func

    def bootstrap(self, num_of_times, k): # k is number of samples to draw (sample with replacement)
        stats = []

        for i in range(num_of_times):
            sampled_data = random.choices(self.data, k) # sampled list of length k
            stat = self.stats_func(sampled_data)
            stats.append(stat)

        return stats
        
    

if __name__ == '__main__':
    words = ['flourished', 'electrode', 'thunders', 'expect', 'loamy', 'masonry', 'wicked', 'mosquito', 'rangers', 'geochemical']

    bootstrapper = Bootstrapper(words, count_vowel_proportions)
    vowel_proportions = bootstrapper.bootstrap(1000, 8)

    mean = statistics.mean(vowel_proportions)
    std = statistics.stdev(vowel_proportions)