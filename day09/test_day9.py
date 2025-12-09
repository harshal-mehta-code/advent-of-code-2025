import day9_solution
import os

def test_example():
    example_input = """7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3
"""
    with open('test_input.txt', 'w') as f:
        f.write(example_input)
    
    result = day9_solution.solve('test_input.txt')
    print(f"Test Result: {result}")
    
    assert result == 50, f"Expected 50, got {result}"
    print("Test Passed!")
    
    os.remove('test_input.txt')

if __name__ == "__main__":
    test_example()
