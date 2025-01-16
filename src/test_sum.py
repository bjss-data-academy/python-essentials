from sum import calculate_sum

def test_sums_three_numbers():
        # Arrange
    input = [1, 2, 3]

    # Act
    actual = calculate_sum( input )

    # Assert
    expected = 1 + 2 + 3
    assert actual == expected

