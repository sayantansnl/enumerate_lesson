def clean_and_analyze(readings: list[int]) -> tuple[list[int], list[int]]:
    peaks = []
    
    for idx, num in enumerate(readings):
        if num == -1:
            prev_val = readings[idx - 1]
            next_val = readings[idx + 1]
            readings[idx] = (prev_val + next_val) // 2

    for idx, num in enumerate(readings):
        if idx == 0 or idx == len(readings) - 1:
            continue
            
        prev_val = readings[idx - 1]
        next_val = readings[idx + 1]
        
        if num > prev_val and num > next_val:
            peaks.append(idx)

    return (readings, peaks)
