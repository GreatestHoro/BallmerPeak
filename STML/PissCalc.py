import datetime
import statistics

def time_difference(tOne, tTwo):
    dif = tTwo - tOne
    return dif.total_seconds()

def avg_time_betweeen_all_piss(session):
    times = []
    if len(session.piss_times) > 1:
        i = 0
        while i + 1 < len(session.piss_times):
            times.append(time_difference(session.piss_times[i], session.piss_times[i + 1]))
            i += 1
        return datetime.timedelta(seconds=round(statistics.mean(times), 0))
    print("You have not registered enough pisses to find an average time")
    return -1