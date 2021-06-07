import question1

class TestReverse:
    def test_reverse(self):
        assert question1.reverseString("this is simply five words") == "words five simply is this"
        assert question1.reverseString("put some $$$SYmB0ls in there") == "there in $$$SYmB0ls some put"
