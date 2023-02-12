def division_by_one(n: int) -> str:
    try:
        return str(1 / n)
    except ZeroDivisionError:
        return "Division by zero is not allowed"
    except TypeError:
        return "Only numbers are allowed"
    except Exception:
        return "Something went wrong"
    finally:
        print("\nAthos Balmant")


def main():
    print(division_by_one(2))
    print(division_by_one(0))
    print(division_by_one("0"))
    print(division_by_one(1))


if __name__ == "__main__":
    main()
