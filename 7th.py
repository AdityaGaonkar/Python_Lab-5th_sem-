class TIME1:
    def __init__(self, hour=0, min=0, sec=0):
        self.hour = hour
        self.min = min
        self.sec = sec

    def __add__(self, other):
        result = TIME1()
        total_sec = (self.hour * 3600 + self.min * 60 + self.sec + other.hour * 3600 + other.min*60 + other.sec)
        result.hour = total_sec // 3600
        result.min = (total_sec % 3600) // 60
        result.sec = (total_sec % 60)
        return result

    def __sub__(self, other):
        result = TIME1()
        total_sec = abs((self.hour * 3600 + self.min * 60 + self.sec) - (other.hour * 3600 + other.min*60 + other.sec))
        result.hour = total_sec // 3600
        result.min = (total_sec % 3600) // 60
        result.sec = (total_sec % 60)
        return result

    def display(self):
        print(f"{self.hour:02d}:{self.min:02d}:{self.sec:02d}")


def main():
    # Example of TIME class and operator overloading
    time1 = TIME1(10, 30, 45)
    time2 = TIME1(3, 15, 20)

    # Display details of time1 and time2
    print("Time 1:")
    time1.display()

    print("\nTime 2:")
    time2.display()

    # Add and display the result
    result_add = time1 + time2
    print("\nSum of Time 1 and Time 2:")
    result_add.display()

    # Subtract and display the result
    result_sub = time1 - time2
    print("\nDifference of Time 1 and Time 2:")
    result_sub.display()


if __name__ == "__main__":
    main()
