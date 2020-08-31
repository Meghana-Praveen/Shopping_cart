import unittest
import inventory_allocator as ia

class TestInventoryAllocator(unittest.TestCase):

    def test_case_one(self):
        orderDetails = "{\"apple\":2,\"banana\":6}"
        warehouseDetails = "[{\"name\":\"owd\",\"inventory\":{\"apple\":5,\"banana\":5}},{\"name\":\"dm\",\"inventory\":{\"banana\":5,\"orange\":10,\"apple\":10}}]"
        expectedresult = "[{'owd': {'apple': 2, 'banana': 5}}, {'dm': {'banana': 1}}]"
        actualtresult = ia.allocate(orderDetails, warehouseDetails)
        self.assertEqual(expectedresult, str(actualtresult))

    def test_case_two(self):
        orderDetails = "{\"strawberry\":5,\"blueberry\":7}"
        warehouseDetails = "[{\"name\":\"owd\",\"inventory\":{\"apple\":5,\"banana\":5}}]"
        expectedresult = "[]"
        actualtresult = ia.allocate(orderDetails, warehouseDetails)
        self.assertEqual(expectedresult, str(actualtresult))
        
    def test_case_three(self):
        orderDetails = "{\"blueberry\":1}"
        warehouseDetails = "[{\"name\":\"owd\",\"inventory\":{\"blueberry\":0}}]"
        expectedresult = "[]"
        actualtresult = ia.allocate(orderDetails, warehouseDetails)
        self.assertEqual(expectedresult, str(actualtresult))
        
    
    def test_case_four(self):
        orderDetails = "{\"apple\":10}"
        warehouseDetails = "[{\"name\":\"owd\",\"inventory\":{\"apple\":5}},{\"name\":\"dm\",\"inventory\":{\"apple\":5}}]"
        expectedresult = "[{'owd': {'apple':5}},{'dm': {'apple': 5}}]"
        actualtresult = ia.allocate(orderDetails, warehouseDetails)
        self.assertEqual(expectedresult, str(actualtresult))
    def test_case_five(self):
        orderDetails = "{\"apple\":5}"
        warehouseDetails = "[{\"name\":\"dm\",\"inventory\":{\"apple\":4}}]"
        expectedresult = "[]"
        actualtresult = ia.allocate(orderDetails, warehouseDetails)
        self.assertEqual(expectedresult, str(actualtresult))

if __name__ == '__main__':
    unittest.main()
