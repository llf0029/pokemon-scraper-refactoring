def test():
    import doctest
    # doctest.testfile("test_createPokemon.txt", verbose=1)
    # doctest.testfile("test_statisticsCalculator.txt", verbose=1)
    doctest.testfile("test_cmdView.txt", verbose=1)

if __name__ == "__main__":
    test()
