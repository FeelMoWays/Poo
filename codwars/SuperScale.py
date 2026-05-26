def identify_bb(bearings, weigh):
    samples = []
    for i,bearing in enumerate(bearings):
        samples.extend([bearing] * (i+1))
    expected = 10 * sum(range(1,len(bearings) +1))
    actual = weigh(*samples)
    return bearings[actual - expected -1]

