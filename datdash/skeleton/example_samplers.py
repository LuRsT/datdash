import random
import collections

from datdash.datdash_sampler import DatDashSampler


class SynergySampler(DatDashSampler):
    def __init__(self, *args, **kwargs):
        DatDashSampler.__init__(self, *args, **kwargs)
        self._last = 0

    def name(self):
        return 'synergy'

    def sample(self):
        sample_info = {
            'value': random.randint(0, 100),
            'current': random.randint(0, 100),
            'last': self._last,
        }
        self._last = sample_info['current']
        return sample_info


class BuzzwordsSampler(DatDashSampler):
    def name(self):
        return 'buzzwords'

    def sample(self):
        computer_names = [
            'The Machines',
            'MARAX',
            'EPICAC',
            'Mark V',
            'Mima',
        ]
        items = [
            {
                'label': computer_name,
                'value': random.randint(0, 20),
            }
            for computer_name in computer_names
        ]
        random.shuffle(items)
        return {'items': items}


class ConvergenceSampler(DatDashSampler):
    def name(self):
        return 'convergence'

    def __init__(self, *args, **kwargs):
        self.seedX = 0
        self.items = collections.deque()
        DatDashSampler.__init__(self, *args, **kwargs)

    def sample(self):
        self.items.append({'x': self.seedX,
                           'y': random.randint(0,20)})
        self.seedX += 1
        if len(self.items) > 10:
            self.items.popleft()
        return {'points': list(self.items)}

