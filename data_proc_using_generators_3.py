import glob
import logging
import itertools
import os

def log_filter(input):
    log = logging.getLogger("log_filter")
    handler = logging.StreamHandler()
    log.addHandler(handler)
    log.setLevel(logging.INFO)

    for item in input:
        log.info(f"{input} => {item}")
        yield item

def collect_filter(paths):
    for path in paths:
        return itertools.chain(glob.iglob(path + '/**', recursive=True),
                               glob.iglob(path + '/.**', recursive=True))

def size_filter(files):
    for file in files:
        yield os.path.getsize(file)

def sum_filter(size):
    yield sum(size)

def create_processing_pipeline(start_generator, filters):
    generator = start_generator
    for filter in filters:
        generator = filter(generator)
    return generator

filters = [
    collect_filter,
    size_filter,
    log_filter,
    sum_filter
]

pipeline = create_processing_pipeline([r'C:\Users\kanthkr\Documents\work'], filters)

print(next(pipeline))