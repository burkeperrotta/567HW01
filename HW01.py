# This is the code for HW 01: Testing triangle Classification

import unittest

# takes 3 parameters for lengths of a triangle 
# and returns the type of triangle
def classify_triangle(a,b,c): 

# checks for 0 or negative values
    if a <= 0 or b <= 0 or c <= 0:
        return 'notTriangle'
    
# checks if triangle is valid
    elif a + b == c or b + c == a or c + a == b: #will cause test_case_9 to fail bc all '==' should be '<='
        return 'notTriangle'

# check for an equilateral triangle
    elif a == b and a == c:
        return 'Equilaperal' #deliberately spelled wrong to cause a failure
        # print('This tringle is equilateral.')

# check for an isosceles triange
    elif a == b != c or b == c != a or c == a != b:
        return 'Isosceles'
        # print('This tringle is isosceles.')

# check for a scalene triangle
    elif a != b and a != c and b != c:
        return 'Scalene'
        # print('This tringle is scalene.')
    
 # check for a right triangle
    if a**2 + b**2 == c**2 or b**2 + c**2 == a**2 or c**2 + a**2 == b**2:
        return 'Right'
        # print('This tringle is right.')

    


# a = float(input("Enter the length of Side 1: "))
# b = float(input("Enter the length of Side 2: "))
# c = float(input("Enter the length of Side 3: "))

# classify_triangle(a,b,c)



def runClassify_triangle(a, b, c):
    """ invoke classify_triangle with the specified arguments and print the result """
    print('classify_triangle(',a, ',', b, ',', c, ')=',classify_triangle(a,b,c),sep="")

class TriangleTypes(unittest.TestCase):
    # tests for equilateral triangle -- will fail deliberately
    def test_case_1(self):
        self.assertEqual(classify_triangle(2,2,2),'Equilateral')

    # tests for isosceles triangle
    def test_case_2(self):
        self.assertEqual(classify_triangle(4,4,5),'Isosceles')

    # tests for scalene triangle
    def test_case_3(self):
        self.assertEqual(classify_triangle(3,7,8),'Scalene')

    # tests for scalene triangle that is also right
    def test_case_4(self):
        self.assertEqual(classify_triangle(3,4,5),'Scalene','Right')

    # tests for isosceles triangle that is also right
    def test_case_5(self):
        self.assertEqual(classify_triangle(3,3,4.24264068712),'Isosceles','Right')

class TriangleValid(unittest.TestCase):
    # tests with 0 side length
    def test_case_6(self):
        self.assertEqual(classify_triangle(0,7,8),'notTriangle')

    # tests with negative side length
    def test_case_7(self):
        self.assertEqual(classify_triangle(-3,4,5),'notTriangle')
    
    # tests with 2 sides = other side
    def test_case_8(self):
        self.assertEqual(classify_triangle(3,4,7),'notTriangle')

    # tests with 2 sides < other side
    def test_case_9(self):
        self.assertEqual(classify_triangle(3,2,6),'notTriangle')
   
if __name__ == "__main__":
    runClassify_triangle(3,4,5)
    runClassify_triangle(4,4,5)
    runClassify_triangle(3,4,5)
    runClassify_triangle(3,7,8)
    runClassify_triangle(3,3,4.24264068712)
    runClassify_triangle(0,7,8)
    runClassify_triangle(-3,4,5)
    runClassify_triangle(3,4,7)
    runClassify_triangle(3,2,6)


unittest.main(exit=True)
