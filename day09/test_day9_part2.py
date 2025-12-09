import day9_part2_solution
import os

def test_part2_example():
    example_input = """7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3
"""
    with open('test_input_part2.txt', 'w') as f:
        f.write(example_input)
    
    result = day9_part2_solution.solve('test_input_part2.txt')
    print(f"Test Result: {result}")
    
    assert result == 24, f"Expected 24, got {result}"
    print("Test Passed!")
    
    os.remove('test_input_part2.txt')

if __name__ == "__main__":
    test_part2_example()
