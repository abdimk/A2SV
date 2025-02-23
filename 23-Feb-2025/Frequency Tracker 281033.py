# Problem: Frequency Tracker - https://leetcode.com/problems/frequency-tracker/description/

class FrequencyTracker:
    def __init__(self):
        self.freq = {}  # Tracks frequency of each number
        self.freq_count = {}  # Tracks count of numbers with a certain frequency

    def add(self, number: int) -> None:
        if number in self.freq:
            old_freq = self.freq[number]
            self.freq[number] += 1
        else:
            old_freq = 0
            self.freq[number] = 1

        new_freq = self.freq[number]

        # Update frequency count dictionary
        self.freq_count[old_freq] = self.freq_count.get(old_freq, 0) - 1 if old_freq in self.freq_count else 0
        self.freq_count[new_freq] = self.freq_count.get(new_freq, 0) + 1

    def deleteOne(self, number: int) -> None:
        if number in self.freq and self.freq[number] > 0:
            old_freq = self.freq[number]
            self.freq[number] -= 1
            new_freq = self.freq[number]

            # Update frequency count dictionary
            self.freq_count[old_freq] = self.freq_count.get(old_freq, 0) - 1
            self.freq_count[new_freq] = self.freq_count.get(new_freq, 0) + 1 if new_freq > 0 else 0

            # If frequency becomes zero, remove the number from freq dictionary
            if self.freq[number] == 0:
                del self.freq[number]

    def hasFrequency(self, frequency: int) -> bool:
        return self.freq_count.get(frequency, 0) > 0
