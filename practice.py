def avg(exam):
    if not exam:
            return 0
    
    return (sum(exam.values())/len(exam))

def count(text):
    counts={}
    for word in text.lower().split():
        if word in counts:
            counts[word]+=1
        else:
            counts[word]=1
    return counts

def summarize_grades(exams):
    if not exams:
        return 0
    high=max(exams.values())
    low=min(exams.values())
    highex=max(exams, key=exams.get)
    lowex=min(exams, key=exams.get)
    above60=0
    for grade in exams.values():
        if grade>60:
            above60+=1
    return {"highest": (highex, high), "lowest": (lowex, low), "average": avg(exams), "above_60": above60}
