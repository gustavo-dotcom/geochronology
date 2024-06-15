def potassium_argon(argon: float, potassium: float, init_time: int) :
    return (argon / potassium) * (((init_time + 1) * 1.24) / float(5.54e-12 ** -1))


def uranium_lead(lead: float, uranium: float) :
    return (lead / uranium) * (1 ** -1) # qual a constante de decaimento???


def carbon(fossil_age: float, init_activity: float, activity: float) :
    return (fossil_age(init_activity / activity) / float(1.67e-11 ** -1))


    def main():
        pass

    if __name__ == "__main__":
        main()