import day8_part2_solution
import os

def test_part2_example():
    example_input = """162,817,812
57,618,57
906,360,560
592,479,940
352,342,300
466,668,158
542,29,236
431,825,988
739,650,466
52,470,668
216,146,977
819,987,18
117,168,530
805,96,715
346,949,466
970,615,88
941,993,340
862,61,35
984,92,344
425,690,689
"""
    with open('test_input_part2.txt', 'w') as f:
        f.write(example_input)
    
    result = day8_part2_solution.solve('test_input_part2.txt')
    print(f"Test Result: {result}")
    
    assert result == 25272, f"Expected 25272, got {result}"
    print("Test Passed!")
    
    os.remove('test_input_part2.txt')

if __name__ == "__main__":
    test_part2_example()
